# Docker Multi-Container Application
## Nginx Reverse Proxy • Flask API • Redis Cache

This project demonstrates a real-world multi-container Docker setup using Docker Compose.
It includes three core services:

- **Nginx** → Reverse proxy (public entrypoint)
- **Flask API** → Backend service
- **Redis** → In-memory key–value store (visit counter)

The entire stack runs with a single command:

```bash
docker compose up -d
```

---

## 📘 Overview

This project simulates a small production-ready microservices architecture.
Traffic flows from:

```
Client → Nginx → Flask API → Redis
```

The Flask API exposes a simple endpoint that increments a counter stored in Redis.
Nginx routes user traffic and protects internal services.

---

## 📁 Project Structure

```
docker-multi-app/
├── docker-compose.yml
│
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
│
└── nginx/
    └── nginx.conf
```

---

## 🧩 Architecture Diagram



```
+---------------+           +---------------+
|    Client     |---------->|     NGINX     |
| (Browser/App) | :8080     | Reverse Proxy |
+---------------+           +-------+-------+
                                    |
                                    v
                            +---------------+
                            |   Flask API   |
                            |  (Backend)    |
                            +-------+-------+
                                    |
                                    v
                            +-------+-------+
                            |     Redis     |
                            |   (Cache/DB)  |
                            +---------------+
```
## 📦 Prerequisites

Before starting, ensure you have:

- Docker installed  
- Docker Compose installed  
- (Optional) AWS EC2 Instance with Docker

---
## 🛠 Steps to Execute (Run Locally)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shatrujit-Biswal/docker-multi-container-app.git
cd docker-multi-container-app
```

### 2️⃣ Start the entire stack
```bash
docker compose up --build -d
```

### 3️⃣ Access the services

- Homepage → http://localhost:8080  
- API → http://localhost:8080/api/visits

Each refresh increments the visit counter stored in Redis.

### 4️⃣ Stop everything
```bash
docker compose down
```
## 🔧 Service Descriptions

### **1. Nginx (Reverse Proxy)**
- Listens on port **80** inside the container  
- Exposed as **8080** on the host  
- Routes:  
  - `/` → Static welcome page  
  - `/api/` → Proxies to Flask API  

### **2. Flask API (Backend)**
Implements:

```
GET /api/visits
```

This increments and returns a counter stored in Redis.  
Runs on port **5000**.

### **3. Redis (Data Store)**
Stores:
- Visit counter (`visits`)
- Fast, in-memory key/value storage

Runs on port **6379**.

---

## 📝 Closing Notes
This project helped me build solid, hands-on DevOps skills such as:

- Multi-container architecture  
- Reverse proxy routing  
- API → cache communication  
- Docker Compose orchestration  
- Local + cloud deployment workflow  

---

## 👨‍💻 Author

**Shatrujit Biswal**  
DevOps & Cloud Learner  
Building automation scripts, cloud deployments, and containerized systems — one project at a time 🚀
