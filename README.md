Docker Multi-Container Application
Nginx Reverse Proxy • Flask API • Redis Cache

This project demonstrates a real-world multi-container Docker setup using Docker Compose.
It includes three core services:

Nginx → Reverse proxy (public entrypoint)

Flask API → Backend service

Redis → In-memory key–value store (visit counter)

The entire stack runs with a single command:

docker compose up -d

📘 Overview

This project simulates a small production-ready microservices architecture.
Traffic flows from:

Client → Nginx → Flask API → Redis


The Flask API exposes a simple endpoint that increments a counter stored in Redis.
Nginx routes user traffic and protects internal services.

Perfect for DevOps portfolios.

📁 Project Structure
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

🧩 Architecture Diagram (Text-based)
                      http://<ip>:8080
           ┌──────────────────────────────────┐
           │                                  │
           ▼                                  │
     ┌──────────┐                       ┌────────────┐
     │  Client  │ --------------------▶ │   NGINX    │
     └──────────┘                       │ Reverse    │
                                        │   Proxy    │
                                        └─────┬──────┘
                                              │
                                              ▼
                                      ┌────────────┐
                                      │  Flask API │
                                      └─────┬──────┘
                                            │
                                            ▼
                                      ┌────────────┐
                                      │   Redis    │
                                      └────────────┘

🛠 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/<your-username>/docker-multi-container-app.git
cd docker-multi-container-app

2️⃣ Start the entire stack
docker compose up --build -d

3️⃣ Access the services

Homepage → http://localhost:8080

API → http://localhost:8080/api/visits

Each refresh increments the visit counter stored in Redis.

4️⃣ Stop everything
docker compose down

🔧 Service Descriptions
1. Nginx (Reverse Proxy)

Listens on port 80 inside the container

Exposed as 8080 on the host

Routes:

/ → Static welcome page

/api/ → Proxies to Flask API

2. Flask API (Backend)

Implements:

GET /api/visits


This increments and returns a counter stored in Redis.

Runs on port 5000.

3. Redis (Data Store)

Stores:

Visit counter (visits)

Fast, in-memory key/value storage

Runs on port 6379.

🌍 Deploying to AWS EC2
1️⃣ Copy project to EC2
scp -i your-key.pem -r docker-multi-app ubuntu@<EC2-IP>:~

2️⃣ SSH into EC2
ssh -i your-key.pem ubuntu@<EC2-IP>

3️⃣ Run on EC2
cd docker-multi-app
docker compose up -d --build

4️⃣ Access publicly
http://<EC2-IP>:8080
http://<EC2-IP>:8080/api/visits
