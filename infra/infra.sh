RESOURCE_GROUP= "my-mlops-group"
LOCATION="eastus2"
WORKSPACE_NAME="ml-mlops-workspace-visualpath"
CLUSTER_NAME= "mlops-cluster-visualpath"

az group create -n $RESOURCE_GROUP -l $LOCATION

az ml workspace create -n $WORKSPACE_NAME -g $RESOURCE_GROUP -l $LOCATION

az ml workspace set -g $RESOURCE_GROUP -w $WORKSPACE_NAME

az ml compute create --name $CLUSTER_NAME \
   --type Amlcompute \
   --size Standard_DS11_v2 \
   --min-instance 0 --max-instance 2

   