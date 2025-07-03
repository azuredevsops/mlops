#!/bin/bash

set -e  # Exit on error

RG="my-visua-1"
WS="my-ml-ws-1"
LOCATION="eastus"

echo "Creating resource group..."
az group create --name $RG --location $LOCATION

echo "Creating Azure ML workspace..."
az ml workspace create --name $WS --resource-group $RG --location $LOCATION


echo "Creating compute cluster..."
az ml compute create --name cpu-cluster \
  --type AmlCompute \
  --size Standard_DS2_v2 \
  --min-instances 0 --max-instances 2

echo "Uploading train.csv and test.csv..."
az ml data upload \
  --path ./data/train.csv \
  --target-path data/train.csv \
  --datastore-name workspaceblobstore

az ml data upload \
  --path ./data/test.csv \
  --target-path data/test.csv \
  --datastore-name workspaceblobstore

echo "Infra setup complete."

