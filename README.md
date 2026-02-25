 🚨 Fraud Detector 💳  
 Online Payment Fraud Detection using Machine Learning & Flask

A real-time web application that detects fraudulent online payment transactions using a trained Machine Learning model.

This project combines:
- Data preprocessing & visualization
- Machine Learning model building
- Flask web application
- Cloud deployment (Render)
- Version control (GitHub)

---

 📌 Project Overview

Online payment fraud is a major issue in digital transactions.  
This project uses historical transaction data to train a classification model capable of identifying fraudulent transactions based on transaction patterns and balance behavior.

The trained model is deployed using Flask and served via Gunicorn on Render.

---

 🚀 Live Demo

https://fraud-detector-nmlq.onrender.com

 🛠️ Technologies Used

🔹 Programming
- Python 3.x

🔹 Libraries
- Flask
- NumPy
- Scikit-learn
- Gunicorn

🔹 Tools
- Anaconda
- Jupyter Notebook
- GitHub
- Render (Cloud Deployment)

📊 Machine Learning Workflow

 1️⃣ Data Collection
- Dataset: Online payment transaction dataset (CSV format)

 2️⃣ Data Preprocessing
- Removed unnecessary columns
- Checked null values
- Handled categorical encoding
- Split into training & testing sets

 3️⃣ Exploratory Data Analysis
- Univariate analysis
- Bivariate analysis
- Correlation heatmap
- Distribution plots
- Outlier detection

 4️⃣ Model Building
Compared multiple classifiers:

- Random Forest
- Decision Tree
- Extra Trees
- Support Vector Machine (SVC)

 5️⃣ Model Selection
SVC was selected based on:
- Accuracy score
- Classification report
- Confusion matrix

 6️⃣ Model Saving
Model saved using:
```python
pickle.dump(model, open("model.pkl", "wb"))

fraud-detector/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Procfile
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── result.html
│
├── static/
│   └── css/
│       └── style.css
│
├── dataset/
│   └── PS_20174392719_1491204439457_log.csv
│
└── training/
    └── model_training.ipynb

# 🎥 Demo Video

Watch the project demo here:

https://drive.google.com/file/d/1Mu-SGven6W-DuSLA6OkPKTyWwwq5iJIf/view?usp=sharing
