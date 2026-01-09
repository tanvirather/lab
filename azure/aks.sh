# [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)

################################################## variables ##################################################L
BASE_NAME="zuhid"
LOCATION="centralus"

RESOURCE_GROUP="${BASE_NAME}-rg"
RESOURCE_GROUP_AKS="${BASE_NAME}-aks-rg"
RESOURCE_GROUP_NETWORK_WATCHER="NetworkWatcherRG"

AKS="${BASE_NAME}-aks"
AKS_NODE_COUNT="2"

################################################## functions ##################################################L
refresh_resource_groups(){
    az group delete --name $RESOURCE_GROUP_NETWORK_WATCHER --yes 2>/dev/null
    az group delete --name $RESOURCE_GROUP_AKS --yes 2>/dev/null
    az group delete --name $RESOURCE_GROUP --yes 2>/dev/null
    az group create --name $RESOURCE_GROUP --location $LOCATION 1>/dev/null && echo "Resource group created : $RESOURCE_GROUP"
}

################################################## exec ##################################################

clear
# az login
# az account set --subscription "<SUBSCRIPTION_ID>"
# az aks list --resource-group $RESOURCE_GROUP
# az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS --overwrite-existing

# alias k="kubectl"

# time (
#     refresh_resource_groups
#     az aks create --resource-group $RESOURCE_GROUP --name $AKS --node-resource-group $RESOURCE_GROUP_AKS --node-count $AKS_NODE_COUNT --generate-ssh-keys && echo "AKS created : $AKS"
# )






