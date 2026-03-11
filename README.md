# PodShield

### Kubernetes Pod Security Policy Generator

PodShield is a DevOps tool that automatically generates **secure Kubernetes Pod YAML configurations** based on user inputs. It helps developers enforce container security best practices such as running containers as non-root, disabling privilege escalation, and using read-only filesystems.

The application is built using **Python Flask**, containerized using **Docker**, and deployed on a **Kubernetes cluster**.

---

# Project Overview

Writing secure Kubernetes configurations manually can be error-prone. PodShield simplifies this by automatically generating **secure Pod YAML configurations** based on user input.

Users provide parameters such as:

* Container image
* Root access permission

PodShield then generates a **secure Kubernetes Pod specification** that follows container security best practices.

---

# Architecture

User Request
↓
Flask API (PodShield)
↓
Docker Container
↓
Kubernetes Deployment
↓
Secure Pod YAML Output

---

# Tech Stack

* **Python** – Backend logic
* **Flask** – REST API
* **PyYAML** – YAML generation
* **Docker** – Containerization
* **Kubernetes** – Container orchestration
* **GitHub** – Version control

---

# Project Structure

```
podshield
│
├── app.py
├── generator.py
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the Repository

```
git clone https://github.com/yourusername/podshield.git
cd podshield
```

---

# Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Server runs on:

```
http://localhost:5000
```

---

# Docker Setup

Build Docker image:

```
docker build -t podshield .
```

Run container:

```
docker run -p 5000:5000 podshield
```

---

# Kubernetes Deployment

Apply deployment:

```
kubectl apply -f deployment.yaml
```

Apply service:

```
kubectl apply -f service.yaml
```

Check pods:

```
kubectl get pods
```

Check services:

```
kubectl get services
```

---

# API Usage

Endpoint:

```
POST /generate
```

Example request:

```
{
  "image": "nginx",
  "allow_root": false
}
```

Example response:

```
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  containers:
  - image: nginx
    name: app
    securityContext:
      runAsNonRoot: true
      readOnlyRootFilesystem: true
      allowPrivilegeEscalation: false
```

---

# Security Features Generated

PodShield enforces several Kubernetes security best practices:

* Prevent running containers as root
* Disable privilege escalation
* Use read-only root filesystems
* Generate structured Kubernetes YAML automatically

---

# Future Improvements

Possible enhancements include:

* Web UI for policy generation
* Security scoring for configurations
* Integration with container vulnerability scanners
* Support for advanced Kubernetes security policies

---

# Author

**Samridhi Rana**

B.Tech Computer Science
Manipal University Jaipur
