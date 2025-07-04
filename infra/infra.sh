#!/bin/bash

set -e  # Exit on error

RG="mlops-training"
WS="mlops-training-visual"
LOCATION="eastus"

echo "Creating resource group..."
az group create --name $RG --location $LOCATION

echo "Creating Azure ML workspace..."
az ml workspace create --name $WS --resource-group $RG --location $LOCATION


echo "Creating compute cluster..."
az ml compute create --name cpu-cluster \
  --type AmlCompute \
  --size Standard_DS2_v2 \
  --min-instances 0 \
  --max-instances 2 \
  --resource-group "$RG" \
  --workspace-name "$WS"

echo "Registering train.csv as dataset..."
az ml data create --name train-csv \
  --type uri_file \
  --path ./data/train.csv \
  --description "Training data" \
  --resource-group "$RG" \
  --workspace-name "$WS"

echo "Registering test.csv as dataset..."
az ml data create --name test-csv \
  --type uri_file \
  --path ./data/test.csv \
  --description "Testing data" \
  --resource-group "$RG" \
  --workspace-name "$WS"

echo "Infra setup complete."

