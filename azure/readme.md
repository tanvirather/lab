# Install

- [Azure Cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest&pivots=apt)
```sh
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
```sh
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

# Extensions
- Kubernetes
- Azure kubernetes Service
- Azure Resources

# Commands (aks)
```sh
alias dc='docker container ls'

az aks list --resource-group 'zuhid-rg'
az aks get-credentials --resource-group 'zuhid-rg' --name 'zuhid-aks' # Get access credentials for a managed Kubernetes cluster.
kubectl get node
kubectl get pod -A -o wide

az aks stop --resource-group 'zuhid-rg' --name 'zuhid-aks' # stop the cluster
az aks show --resource-group 'zuhid-rg' --name 'zuhid-aks' --query "powerState"  # show the status
az aks start --resource-group 'zuhid-rg' --name 'zuhid-aks' # start the cluster
```

```sh
az network watcher configure --resource-group $RESOURCE_GROUP --locations $LOCATION --enabled true # Manually create the Network Watcher resource
```
