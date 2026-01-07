# [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)

################################################## variables ##################################################L
BASE_NAME="zuhid"
LOCATION="centralus"
RESOURCE_GROUP="${BASE_NAME}-rg"
# NETWORK_WATCHER="my-networkwatcher-rg"
AKS="${BASE_NAME}-aks"
AKS_MC="${BASE_NAME}-managed-cluster-rg"
AKS_NODE_COUNT="1"

################################################## execution ##################################################

clear
# az login
az group delete --name "NetworkWatcherRG" --yes
az group delete --name "zuhid-rg-mc" --yes
az group delete --name $RESOURCE_GROUP --yes # Delete a resource group
# az group create --name $RESOURCE_GROUP --location $LOCATION  # Create a resource group
# az aks create --resource-group $RESOURCE_GROUP --name $AKS --node-resource-group $AKS_MC --node-count $AKS_NODE_COUNT --generate-ssh-keys # Create an AKS cluster


# az network watcher configure --resource-group $RESOURCE_GROUP --locations $LOCATION --enabled true # Manually create the Network Watcher resource


