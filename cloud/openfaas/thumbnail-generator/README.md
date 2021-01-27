# xOpera deploy of simple thumbnail generator to OpenFaaS

## Table of Contents
  - [Content](#content)
  - [System installations and configurations](#system-installations-and-configurations)
  - [Thumbnail deploy](#thumbnail-deploy)
  
## Content
There are two main folders here that allow orchestration with xOpera. One is for environment preparation and the second
one is the actual deployment of the thumbnail generator.

## System installations and configurations
The `openfaas-setup` directory explains how to setup your environment on a VM or locally. This includes installing 
docker, MinIO object storage and OpenFaaS with xOpera and Ansible. 

## Thumbnail deploy
The folder `image-resize` contains the main functionality of image-resize which is to create thumbnails from the 
source image. Source image must be uploaded into source bucket and then three thumbnails will be created and saved to 
another bucket.
