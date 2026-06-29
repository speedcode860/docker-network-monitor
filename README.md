# 🐳 Docker Network Monitor

## 📌 Description

Docker Network Monitor est un **service API léger** conteneurisé avec Docker.
Il permet de simuler un **service de supervision réseau** exposé via HTTP.

Ce projet a pour objectif de pratiquer :
- Docker (Dockerfile, build, run)
- Isolation applicative
- Exposition réseau via ports
- Tests API avec Postman
- Bonnes pratiques DevOps de base

---

## 🧱 Architecture du projet

```text
docker-network-monitor/
├── service/
│   └── app.py
├── docker/
│   └── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
