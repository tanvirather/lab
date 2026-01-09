# Dictionary
- **Node**: Virtual or Physical machine that runs pods
- **Pod**: Smallest unit in kubernetes that run one or more containers
- **Deployment**: object to control the behavior of similar pods 
- **ReplicaSet**: ensures that a specific number of pod replicas are runnning 
- **DaemonSet**: type of controller that ensures that a specified pod runs on all nodes or a specified subset of nodes: 
- **Service**: object used to expose pods via a single IP address from a range called the service CIDR. You may have multiple pods for the same application. You can use a service to load balance traffic between them and connect via a unique IP address: the service’s IP address. There are multiple service types, but the most used are
    - **ClusterIP**: default type. It exposes the service on a cluster-internal IP from the service CIDR and is reachable only inside the cluster
    - **NodePort**: exposes a static port, between 30000-32768 on each node in the cluster. The service will be reachable from outside the cluster using <nodeIP>:<staticPort>
    - **LoadBalancer**: provides an externally IP address for accessing the service through a cloud provider load balancer that usually has a single, static IP address
- **Secret**: allows you to store sensitive information, such as passwords, API keys, certificates, in a secure and reliable manner. The values are encoded using Base64
- **ConfigMap**: allows you to store non-sensitive configuration information, such as environment variables, configuration files. The values are not encoded
- **Namespace**: used to divide cluster resources. Some resources are namespaces, some are not
- **kubectl api-resources**: can be used to see all Kubernetes objects, if they are namespaced and, other information

- ****: 
- ****: 
- ****: 

