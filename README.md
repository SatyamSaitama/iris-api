
# Iris API - FastAPI on GKE

This project is a machine learning API for the Iris dataset, built with **FastAPI**, containerized with **Docker**, and deployed on **Google Kubernetes Engine (GKE)**. It includes full **CI/CD integration via GitHub Actions**.

## 🚀 Features

- FastAPI backend to serve ML predictions
- Logistic Regression model trained on Iris dataset
- Dockerized application
- Deployed to GKE Autopilot
- GitHub Actions for CI/CD
- Uses Google Artifact Registry for container storage

---

## 📁 Project Structure

```
fastapi/
├── main.py                # FastAPI app
├── model.pkl              # Trained Iris ML model (pickle)
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
├── k8s/
│   ├── deployment.yaml    # Kubernetes deployment config
│   └── service.yaml       # Kubernetes service config
└── .github/
    └── workflows/
        └── deploy.yml     # GitHub Actions CI/CD pipeline
```

---

## 🛠 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iris-api.git
cd iris-api
```

### 2. Build and Run Locally

```bash
docker build -t iris-api .
docker run -d -p 8000:8000 iris-api
```

Access the API at: `http://localhost:8000`

### 3. Push to Google Artifact Registry

Make sure you are authenticated with GCP:

```bash
gcloud auth login
gcloud auth configure-docker
```

Tag and push:

```bash
docker tag iris-api us-central1-docker.pkg.dev/YOUR_PROJECT_ID/my-repo/iris-api
docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/my-repo/iris-api
```

### 4. Deploy to GKE

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 5. CI/CD with GitHub Actions

- GitHub Actions pipeline is defined in `.github/workflows/deploy.yml`
- Push changes to trigger automatic build and deployment

---

## 📫 Contact

Created by **Satyam** – feel free to reach out on GitHub for questions or suggestions.
