# Minikube and Kubectl Lab Setup 🚀

Easily set up and manage your own **Kubernetes cluster** locally using **Minikube** and **kubectl**. This guide will walk you through a hands-on approach to deploying applications, scaling them, and managing your Kubernetes cluster in a simplified manner. 

---
## 🎯 Prerequisites
Before getting started, ensure you have the following installed on your system:

1. **Minikube** - A tool to run Kubernetes locally.
2. **kubectl** - A command-line tool to manage Kubernetes clusters.

---
## 📥 Installation Guide

### ✅ Step 1: Install Minikube & kubectl

#### 🔹 Installing Minikube
- **Linux**:
  ```bash
  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
  sudo install minikube-linux-amd64 /usr/local/bin/minikube
  ```
- **macOS**:
  ```bash
  brew install minikube
  ```
- **Windows**:
  Use [Chocolatey](https://chocolatey.org/):
  ```powershell
  choco install minikube
  ```

#### 🔹 Installing kubectl
- **Linux/macOS**:
  ```bash
  curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
  chmod +x kubectl
  sudo mv kubectl /usr/local/bin/
  ```
- **Windows**:
  Download [kubectl for Windows](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/).

---
## 🚀 Setting Up Minikube Cluster

### ✅ Step 2: Start Minikube
To start Minikube, simply run:
```bash
minikube start
```
This initializes a local Kubernetes cluster inside a VM.

### ✅ Step 3: Verify Cluster
Check if Minikube is running:
```bash
kubectl get nodes
```
A successful setup should return a **Ready** node status. 🎉

---
## 🛠 Deploying an Application

### ✅ Step 4: Create a Deployment
Let's deploy an **Nginx web server**:
```bash
kubectl create deployment nginx --image=nginx
```
This will create a deployment named `nginx` using the official `nginx` container image.

### ✅ Step 5: Expose the Deployment
Expose the deployment as a service:
```bash
kubectl expose deployment nginx --type=NodePort --port=80
```
This will allow external access to the application.

### ✅ Step 6: Get the Service URL
Find the URL to access the application:
```bash
minikube service nginx --url
```
You should get a URL like `http://192.168.99.100:30001` to access your running Nginx server.

---
## 📊 Managing Deployments

### ✅ Step 7: View Running Pods
List all running pods:
```bash
kubectl get pods
```

### ✅ Step 8: Scale the Deployment
Increase the number of replicas to **3**:
```bash
kubectl scale deployment nginx --replicas=3
```
Verify scaling:
```bash
kubectl get pods
```

### ✅ Step 9: Delete the Deployment
When you're done, clean up the resources:
```bash
kubectl delete service nginx
kubectl delete deployment nginx
```

---
## 📝 Quick Command Reference

```bash
# Start Minikube
minikube start

# Verify Cluster Status
kubectl get nodes

# Deploy an Application
kubectl create deployment nginx --image=nginx

# Expose the Deployment
kubectl expose deployment nginx --type=NodePort --port=80

# Get Service URL
minikube service nginx --url

# View Running Pods
kubectl get pods

# Scale Deployment
kubectl scale deployment nginx --replicas=3

# Delete Deployment & Service
kubectl delete service nginx
kubectl delete deployment nginx
```

---
## 🎯 Conclusion

By following this guide, you have successfully:
✅ Installed Minikube & kubectl
✅ Created a local Kubernetes cluster
✅ Deployed and scaled an application
✅ Managed Kubernetes resources

Minikube is an excellent tool to test and experiment with Kubernetes before moving to production. Happy Kubernetes-ing! 🚀
