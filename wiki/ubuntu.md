# Install Software on Ubuntu
```sh
sudo apt update 
sudo apt upgrade --yes
sudo apt install --yes build-essential curl git

######################### [Install vscode](https://code.visualstudio.com/Download)
sudo snap install --classic code 
wget -qO- https://raw.githubusercontent.com/harry-cpp/code-nautilus/master/install.sh | bash # Install "Open in Code" context menu

######################### Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

######################### Install rclone
sudo apt install rclone
rclone config

######################### Install keepassxc
sudo snap install keepassxc

######################### Create ssh key (https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)
ssh-keygen -t rsa -b 4096 -C "EMAIL" 
git config --global user.name "FIRST LAST"
git config --global user.email "EMAIL"

######################### Docker (https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
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

######################### Dotnet
wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
sudo apt update
sudo apt install --yes zlib1g
sudo apt update
sudo apt install --yes dotnet-sdk-10.0
# dotnet --list-sdks # verify

######################### Python
sudo apt update
sudo apt install --yes python3 python3-venv python3-pip
# python3 --version # verify

######################### nodejs and npm Begin (https://github.com/nodesource/distributions#debinstall)
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo bash -
sudo apt-get install --yes nodejs
# npm --version # verify
# node --version # verify

######################### Azure Cli Begin (https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt)
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

######################### postgresql-client tools
sudo apt install --yes postgresql-client

######################### Install Office
# sudo apt install --yes libreoffice
sudo apt install --yes libreoffice-writer
sudo apt install --yes libreoffice-calc

######################### Scribus - pdf editor (https://linuxhint.com/install-scribus-ubuntu)
sudo add-apt-repository ppa:scribus/ppa
sudo apt update --yes
sudo apt install --yes scribus

######################### OBS
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt update --yes
sudo apt install --yes obs-studio

######################### VirtualBox (https://www.virtualbox.org/wiki/Linux_Downloads)
wget https://download.virtualbox.org/virtualbox/7.2.4/virtualbox-7.2_7.2.4-170995~Ubuntu~noble_amd64.deb
sudo apt install ./virtualbox-7.2_7.2.4-170995~Ubuntu~noble_amd64.deb

######################### kubernetes (https://kubernetes.io/docs/tasks/tools)
# kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" # Download the latest release
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl # Install kubectl
# kubectl version --client # verify

######################### minikube (https://minikube.sigs.k8s.io/docs/start)
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64 # Download the latest release
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64 # Install minikube
minikube start
minikube addons enable metrics-server 
minikube addons enable ingress
minikube addons list

######################### Cleanup
sudo apt update --yes
sudo apt upgrade
sudo apt autoremove --yes
```


