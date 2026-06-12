# 🚀 FastAPI for Machine Learning Engineers

A collection of practical FastAPI tutorials focused on deploying Machine Learning models, building AI APIs, and creating production-ready backend services.

## 📖 About

This repository contains step-by-step FastAPI examples designed specifically for ML practitioners who want to expose models through REST APIs.

Topics covered include:

* FastAPI fundamentals
* Request and response models
* Model serving with Scikit-Learn
* Deep Learning model deployment
* File uploads for inference
* Background tasks
* Authentication and API security
* Dockerization
* Production deployment

---

## 🛠 Tech Stack

* Python 3.11+
* FastAPI
* Uvicorn
* Pydantic
* Scikit-Learn
* PyTorch
* Pandas
* NumPy
* Docker

---

## 📂 Project Structure

```bash
fastapi-ml-tutorials/
│
├── tutorials/
│   ├── 01_basic_api/
│   ├── 02_path_parameters/
│   ├── 03_request_body/
│   ├── 04_ml_prediction_api/
│   ├── 05_file_upload_inference/
│   ├── 06_authentication/
│   └── 07_docker_deployment/
│
├── models/
│   └── sample_model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-ml-tutorials.git

cd fastapi-ml-tutorials
```

Create a virtual environment:

```bash
python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running a Tutorial

Navigate to any tutorial folder:

```bash
cd tutorials/04_ml_prediction_api
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will run at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🤖 Example ML Prediction API

Request:

```json
{
    "feature_1": 5.1,
    "feature_2": 3.5,
    "feature_3": 1.4,
    "feature_4": 0.2
}
```

Response:

```json
{
    "prediction": "setosa",
    "confidence": 0.98
}
```

---

## 🎯 Learning Outcomes

After completing these tutorials, you will be able to:

* Build REST APIs using FastAPI
* Serve Machine Learning models
* Validate requests using Pydantic
* Deploy AI applications
* Containerize ML services with Docker
* Create production-ready inference endpoints

---

## 📚 Recommended Prerequisites

* Basic Python
* Machine Learning fundamentals
* Familiarity with Scikit-Learn or PyTorch
* Basic command-line usage

---

## 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to open an issue or submit a pull request.

---

## ⭐ Support

If you find this repository useful, consider giving it a star.

It helps others discover the project and motivates future content.
# FastAPI
