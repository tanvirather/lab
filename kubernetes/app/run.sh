#################### variables
REGISTRY="tzather"
APP="cs-api"
VERSION="v1"
IMAGE="${REGISTRY}/${APP}:${VERSION}"
NAMESPACE="myapp-namespace"
#################### exec

clear

#################### build and publish docker image
# docker rm $IMAGE 2>/dev/null
# docker rmi $IMAGE 2>/dev/null
# docker build --tag $IMAGE --file api/Dockerfile . # run from current folder
# docker run --rm -p 8080:8080 --name $APP $IMAGE # http://localhost:8080
# docker push $IMAGE # push container https://hub.docker.com/u/tzather
# docker image ls

#################### minikube

# minikube delete # Deletes a local Kubernetes cluster
# minikube start # Starts a local Kubernetes cluster

#################### namespace
# kubectl delete namespace $NAMESPACE  # List all namespace
# kubectl apply --filename devops/namespace.yaml # Apply the file
# kubectl get namespace # List all namespace
# kubectl config set-context --current --namespace=myapp-namespace  # Set a context entry in kubeconfig

#################### deployment
# kubectl delete deployment myapi-deployment # delete named pod 
# kubectl apply --filename devops/deployment.yaml # Apply the file
# kubectl get deployments # List all namespace
# kubectl get pods -o wide
# kubectl exec -it "myapi-deployment-675f577995-29nnf" -- /bin/bash # run bash inside the pod
# apt update && apt install curl -y && curl localhost:8080 && echo

#################### services
kubectl delete service myapi-service
kubectl apply --filename devops/service.yaml # Apply the file
# kubectl get services
# kubectl get service myapi-service
kubectl get endpoints myapi-service
# minikube tunnel # http://127.0.0.1:3000


#################### secrets
kubectl apply --filename devops/secret.yaml # Apply the file
kubectl get secrets
# kubectl get secret api-key-secret -o jsonpath="{.data.db_credential}" | base64 --decode
# echo -n "UserId=dbuser;PassworP@ssw0rd" | base64
