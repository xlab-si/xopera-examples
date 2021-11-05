#!/bin/bash

# This is the script that is used to validate that the examples are runnable with xOpera orchestrator.
# The script is meant to be used within the CI/CD configuration, but you can also run it manually with: ./runme.sh opera

# get opera executable
opera_executable="$1"

# initialize variables for testing
tests_run=0
successful=0
failed=0

# function for validating and checking the exit codes of the tested examples
validate_example() {
  # set function arguments
  example_base_path="$1"
  service_template_file_name="$2"
  inputs_file_name="$3"

  # move into folder with example
  cd "$example_base_path" || true

  if [ "$inputs_file_name" == "" ]; then
    validate=$($opera_executable validate --tosca-only "${service_template_file_name}" 2>&1)
    exit_code="$?"
  else
    validate=$($opera_executable validate --tosca-only -i "${inputs_file_name}" "${service_template_file_name}" 2>&1)
    exit_code="$?"
  fi

  # move back
  cd - > /dev/null || true

  tests_run=$((tests_run+1))
  if [ "$exit_code" -eq 0 ]; then
    successful=$((successful+1))
    printf "%-80s OK\n" "$example_base_path"
  else
    failed=$((failed+1))
    printf "%-80s ERROR\n" "$example_base_path"
    echo "$validate"
  fi

  return 0
}

# start testing
printf "Testing opera examples ...\n"

# test an example from tosca/artifacts
validate_example "tosca/artifacts" "service.yaml" ""
# test an example from tosca/attribute-mapping
validate_example "tosca/attribute-mapping" "service.yaml" ""
# test an example from tosca/capability-attributes-properties
validate_example "tosca/capability-attributes-properties" "service.yaml" ""
# test an example from tosca/intrinsic-functions
validate_example "tosca/intrinsic-functions" "service.yaml" ""
# test an example from tosca/outputs
validate_example "tosca/outputs" "service.yaml" ""
# test an example from tosca/policy-triggers
validate_example "tosca/policy-triggers" "service.yaml" ""
# test an example from tosca/relationship-outputs
validate_example "tosca/relationship-outputs" "service.yaml" ""

# test an example from misc/compare-templates
validate_example "misc/compare-templates" "service1.yaml" "inputs1.yaml"
# test an example from misc/concurrency
validate_example "misc/concurrency" "service.yaml" ""
# test an example from misc/hello-world
validate_example "misc/hello-world" "service.yaml" ""
# test an example from misc/nginx-openstack
validate_example "misc/nginx-openstack" "service.yaml" ""
# test an example from misc/scaling
validate_example "misc/scaling" "service.yaml" ""
# test an example from misc/server-client
validate_example "misc/server-client" "service.yaml" ""

# test an example from csars/small
validate_example "csars/small" "service.yaml" "inputs.json"
# test a compressed CSAR example from csars/small
cd csars/small || true
mkdir -p compressed
cp inputs.json compressed/inputs.json
zip -qFSr compressed/small.csar service.yaml playbooks files
cd ../..
validate_example "csars/small/compressed" "small.csar" "inputs.json"
rm -rf csars/small/compressed
# test an example from csars/misc-tosca-types
validate_example "csars/misc-tosca-types" "service.yaml" "inputs.yaml"
# test a compressed CSAR example from csars/misc-tosca-types
cd csars/misc-tosca-types || true
mkdir -p compressed
cp inputs.yaml compressed/inputs.yaml
zip -qFSr compressed/misc-tosca-types.csar service.yaml modules TOSCA-Metadata
cd ../..
validate_example "csars/misc-tosca-types/compressed" "misc-tosca-types.csar" "inputs.yaml"
rm -rf csars/misc-tosca-types/compressed

# test an example from cloud/aws/thumbnail-generator
validate_example "cloud/aws/thumbnail-generator" "service.yaml" "inputs.yaml"
# test an example from cloud/aws/thumbnail-generator-with-api-gateway
validate_example "cloud/aws/thumbnail-generator-with-api-gateway" "service.yaml" "inputs.yaml"
# test an example from cloud/aws/thumbnail-generator-with-vm
validate_example "cloud/aws/thumbnail-generator-with-vm" "service.yaml" "inputs.yaml"
# test an example from cloud/azure/thumbnail-generator
validate_example "cloud/azure/thumbnail-generator" "service.yaml" "inputs.yaml"
# test an example from cloud/gcp/thumbnail-generator
validate_example "cloud/gcp/thumbnail-generator" "service.yaml" "inputs.yaml"
# test an example from cloud/openfaas/thumbnail-generator
validate_example "cloud/openfaas/thumbnail-generator/openfaas-setup" "service.yaml" "inputs.yaml"
validate_example "cloud/openfaas/thumbnail-generator/image-resize" "service.yaml" "inputs.yaml"
# test an example from cloud/platform-connection/aws-azure-connection
validate_example "cloud/platform-connection/aws-azure-connection/aws-azure" "service.yaml" "inputs.yaml"
validate_example "cloud/platform-connection/aws-azure-connection/azure-aws" "service.yaml" "inputs.yaml"

# test an example from kubernetes/docker
validate_example "kubernetes/docker" "service.yaml" "inputs.yaml"
# test an example from kubernetes/rancher
validate_example "kubernetes/rancher" "service.yaml" "inputs.yaml"

# finish testing
printf "\nTesting finished: %d tests runned, %d successful, %d failures\n" "$tests_run" "$successful" "$failed"

# decide the final exit code
if [ "$failed" -ne 0 ]; then
  exit 1
else
  exit 0
fi
