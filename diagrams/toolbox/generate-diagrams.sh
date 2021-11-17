#! /bin/sh
######################################################################
#
# Run the Cloudnet TOSCA toolbox.
#
# Copyright (c) 2021 Inria
#
######################################################################

# Check that the CLOUDNET_BINDIR environment variable is set correctly.
if [ ! -f ${CLOUDNET_BINDIR}/cloudnet_rc.sh ]
then
  echo "The CLOUDNET_BINDIR environment variable is not set correctly!"
  exit 1
fi

# Load cloudnet commands.
. ${CLOUDNET_BINDIR}/cloudnet_rc.sh

# Copy the toolbox configuration.
cp diagrams/toolbox/tosca2cloudnet.yaml .

# Compile all xopera-examples service template files.
translate $(grep 'tosca_definitions_version: ' -l -r .)

# Remove useless generated files.
rm diagrams/*-workflow-diagram.plantuml

# Generate UML2 diagrams.
generate_uml2_diagrams diagrams/*.plantuml

# Remove useless generated files.
rm -rf diagrams/Alloy/ \
       diagrams/DeclarativeWorkflows/ \
       diagrams/ToscaDiagrams/ \
       diagrams/NetworkDiagrams/ \
       diagrams/*.plantuml \
       diagrams/*.svg \
       tosca2cloudnet.yaml
