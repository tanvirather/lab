# Overview
The following scripts are used to set up and personalize Ubuntu

# Setup for Cli Enviornment
```sh
sudo apt update 
sudo apt upgrade -y
sudo apt install -y build-essential curl
sudo apt install -y curl
sudo apt install -y git
sudo apt install -y postgresql-client

# Create ssh key (https://docs.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops)
ssh-keygen -t rsa -b 4096 -C "tanvirather@zuhid.com" 
git config --global user.name "Tanvir Ather"
git config --global user.email "tanvirather@zuhid.com"

######################### Docker Begin (https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
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
######################### Docker End

######################### kubernetes Begin (https://kubernetes.io/docs/tasks/tools)
# kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" # Download the latest release
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl # Install kubectl
kubectl version --client # verify

# minikube: https://minikube.sigs.k8s.io/docs/start
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64 # Download the latest release
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64 # Install minikube
minikube start
minikube addons enable metrics-server 
minikube addons enable ingress
minikube addons list
######################### kubernetes End

######################### Dotnet Begin
wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
sudo apt update
sudo apt install -y zlib1g
sudo apt update
sudo apt install -y dotnet-sdk-10.0
# dotnet --list-sdks
######################### Dotnet End

######################### Python
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
######################### Python End

# [Install nodejs, npm](https://github.com/nodesource/distributions#debinstall)
curl -fsSL https://deb.nodesource.com/setup_24.x | sudo bash -
sudo apt-get install -y nodejs

## [Install Azure Cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt)
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install angular
sudo npm install -g @angular/cli
```

# Setup for Desktop Enviornment
```sh
# Install Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

# [Install vscode](https://code.visualstudio.com/Download)
sudo snap install --classic code

# [enpass](https://www.enpass.io/support/kb/general/how-to-install-enpass-on-linux/)
sudo -i
echo "deb https://apt.enpass.io/ stable main" > /etc/apt/sources.list.d/enpass.list
wget -O - https://apt.enpass.io/keys/enpass-linux.key | tee /etc/apt/trusted.gpg.d/enpass.asc
apt-get update
apt-get install enpass
exit

# [Install OneDrive](https://linuxhint.com/install-microsoft-onedrive-ubuntu)
sudo add-apt-repository ppa:yann1ck/onedrive
sudo apt-get update
sudo apt install -y onedrive
onedrive

# [Install VirtualBox](https://www.virtualbox.org/wiki/Linux_Downloads)
wget https://download.virtualbox.org/virtualbox/6.1.26/virtualbox-6.1_6.1.26-145957~Ubuntu~eoan_amd64.deb
sudo apt install ./virtualbox-6.1_6.1.26-145957~Ubuntu~eoan_amd64.deb

# Install Office
sudo apt install -y libreoffice
sudo apt install -y libreoffice-writer
sudo apt install -y libreoffice-calc

# [Install Scribus - pdf editor](https://linuxhint.com/install-scribus-ubuntu)
sudo add-apt-repository ppa:scribus/ppa
sudo apt update
sudo apt install -y scribus

# Install OBS
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt update
sudo apt install obs-studio

# remove trashcab icon from toolbar
gsettings set org.gnome.shell.extensions.dash-to-dock show-trash false
```

# Other
```sh
# [Install GO](https://golang.org/doc/install)

# [Configure ssh for ado](https://stackoverflow.com/questions/69875520/unable-to-negotiate-with-40-74-28-9-port-22-no-matching-host-key-type-found-th)
https/dev.azure.com/tzather
put this in ~/.ssh/config

Host ssh.dev.azure.com
    User git
    PubkeyAcceptedAlgorithms +ssh-rsa
    HostkeyAlgorithms +ssh-rsa

# [Install Powershell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux)
sudo apt-get update
sudo apt-get install -y wget apt-transport-https
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo add-apt-repository universe
sudo apt-get install -y powershell
Install-Module -Name SqlServer

# [Install Azure Powershell](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps)

# [InstallSql Server tools](https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver15#ubuntu)
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
sudo apt-get update
sudo apt-get install mssql-tools unixodbc-dev
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc

# [Install SQL Server](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-linux-ver15)
# [install libjemalloc1](http://ftp.osuosl.org/pub/ubuntu/pool/universe/j/jemalloc/libjemalloc1_3.6.0-11_amd64.deb)
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"
sudo apt update
sudo apt install -y mssql-server
sudo /opt/mssql/bin/mssql-conf setup # P@ssw0rd
systemctl status mssql-server

# [Istall MySQL, PHP](https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-ubuntu-18-04)
sudo apt update
sudo apt install php-cgi
sudo apt install php
sudo apt install php-mysql
sudo apt install mysql-server
sudo mysql_secure_installation

# Install Apache
sudo apt install apache2
sudo apt install libapache2-mod-php
sudo a2enmod rewrite
sudo a2enmod ssl
```

# Cleanup 
```sh
sudo apt-get update
sudo apt autoremove -y
```