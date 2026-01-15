# minikube commands

```sh
minikube start # Starts a local Kubernetes cluster
minikube delete # Deletes a local Kubernetes cluster
minikube dashboard --port=39663 # Access the Kubernetes dashboard running within the minikube cluster
minikube addons enable metrics-server # Enable the Metrics Server Add-On
minikube addons list # display addons
```

# Enable Minikube registry addon (http://127.0.0.1:32770/)
```sh
minikube addons enable registry 
	
kubectl port-forward --namespace kube-system svc/registry 5000:80
kubectl port-forward --namespace kube-system svc/registry 32770:80

# kubectl port-forward -n kube-system svc/registry 5000:80
```
