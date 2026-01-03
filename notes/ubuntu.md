# Setup

## Update
```sh
sudo apt update
sudo apt upgrade --yes
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" # keygen
git config --global user.name "Tanvir Ather"
git config --global user.email  "tanvirather@zuhid.com"
```

## [Install Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
```sh
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update

# Install the latest version
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin --yes

# allow docker to be run wihtout sudo
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

## [Install postgres]
```sh
docker run --name postgres --env POSTGRES_PASSWORD=P@ssw0rd --publish 5432:5432 --detach postgis/postgis:16-3.5 # create postgres 
docker exec -it postgres psql -U postgres -d postgres -c "CREATE USER dbuser WITH SUPERUSER PASSWORD 'P@ssw0rd';" # create user
```

# [Install kubernetes](https://kubernetes.io/docs/tasks/tools)
```sh
# kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" # Download the latest release
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl # Install kubectl
kubectl version --client # verify

# minikube: https://minikube.sigs.k8s.io/docs/start
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64 # Download the latest release
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64 # Install minikube
minikube addons enable metrics-server 
minikube addons enable ingress
minikube addons list
minikube start
```