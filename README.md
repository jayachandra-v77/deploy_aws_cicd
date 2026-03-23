# 🚀 AI Chatbot Deployment (AWS EC2 + ECR + GitHub Actions)

## 📌 Project Overview

This project is a **FastAPI-based chatbot** powered by OpenAI, deployed using:

* Docker 🐳
* AWS ECR (Elastic Container Registry)
* AWS EC2 (Ubuntu)
* GitHub Actions (CI/CD)

---

## 🏗️ Architecture

1. Build Docker image
2. Push image to AWS ECR
3. GitHub Actions triggers deployment
4. EC2 (self-hosted runner) pulls image
5. Docker container runs chatbot

---

## ⚙️ Tech Stack

* FastAPI
* OpenAI API
* Docker
* AWS EC2
* AWS ECR
* GitHub Actions

---

## 📂 API Endpoints

### ✅ Health Check

```
GET /
```

Response:

```json
{
  "message": "API is running"
}
```

---

### 🤖 Ask Question

```
POST /ask
```

Request:

```json
{
  "question": "What is AI?"
}
```

Response:

```json
{
  "answer": "Artificial Intelligence (AI) is..."
}
```

---

## 🔐 Environment Variables

Set these in GitHub Secrets:

```
AWS_ACCESS_KEY
AWS_SECRET_KEY
AWS_REGION
ECR_REPO
OPENAI_API_KEY
```

---

## 🐳 Run Locally

### 1. Build Docker Image

```
docker build -t chatbot .
```

### 2. Run Container

```
docker run -d -p 8000:8000 \
-e OPENAI_API_KEY=your_key \
chatbot
```

---

## 🚀 Deployment

Deployment is automated using **GitHub Actions**:

* Push to `main` branch
* Image builds and pushes to ECR
* EC2 pulls latest image
* Container restarts automatically

---

## 🌐 Access Application

After deployment, open:

```
http://<EC2-PUBLIC-IP>:8000/docs
```

---

## 🛠️ Troubleshooting

### Check running container

```
docker ps
```

### View logs

```
docker logs chatbot
```

### Restart container

```
docker restart chatbot
```

---


## Author

Jayachandra
