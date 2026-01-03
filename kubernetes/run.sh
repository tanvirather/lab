################################################## variables ##################################################
dir=my-directory
namespace=my-namespace
product=my-nginx
image="nginx:1.29.4"
deployment="${product}-deployment"
service="${product}-service"
# pod="${product}-pod"

################################################## init ##################################################
clear
# minikube delete # Delete existing minikube cluster
# minikube start # Start minikube cluster

################################################## namesapce ##################################################
# kubectl create namespace $namespace --dry-run=client --output yaml > $dir/namespace.yaml # Create namespace yaml file
# kubectl apply --filename $dir/namespace.yaml # Apply the file
# kubectl get namespaces # List namespaces
# kubectl config set-context --current --namespace=$namespace # Set the default namespace for kubectl

################################################## deployment ##################################################
# kubectl create deployment $deployment --image=$image --dry-run=client --output yaml > $dir/deployment.yaml # Create namespace yaml file
# kubectl delete deployments $deployment # Delete existing deployment
# kubectl apply --filename $dir/deployment.yaml # Apply the file
# kubectl get deployments -o wide # List deployments
# kubectl describe deployment $deployment # Describe the deployment
# kubectl port-forward deployment/${deployment} 8080:80 # Forward port and access Nginx at http://localhost:8080

################################################## services ##################################################
# kubectl create service clusterip $service --tcp=8080:80 --dry-run=client --output yaml > $dir/service.yaml # Create service yaml file
# kubectl delete service $service # Delete existing service
# kubectl apply --filename $dir/service.yaml # Apply the file
# kubectl get services -o wide # List services

################################################## logs ##################################################
# kubectl logs deployment/${deployment} --follow=true --tail=10 # Stream logs from all pods in the deployment
# kubectl logs pod/${pod} --follow=true --tail=10 # Stream logs from all pods in the deployment

################################################## pods ##################################################
# kubectl run $pod --image=${image} --dry-run=client --output yaml > $dir/pod.yaml # Create pod yaml file
# kubectl delete pod $pod # Delete existing pod
# kubectl apply -f $dir/pod.yaml # Apply the file
# kubectl get pods -o wide # List pods
# kubectl describe pod ${pod} # Describe the pod
# kubectl port-forward pod/${pod} 8080:80 # Forward port and access Nginx at http://localhost:8080
# kubectl exec -it $pod -- /bin/bash # run bash inside the pod
# kubectl exec -it $pod -c ${product}-container -- /bin/bash # run bash inside the pod

