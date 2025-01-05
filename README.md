<div align="center">

# 🚑 Anemia Detection Using Machine Learning 🚑

*An intelligent system for predicting anemia using Random Forest Classification*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

<div align="center">

## 🩺 Overview
</div>

This project implements a **Random Forest Classifier** to predict whether an individual is anemic or non-anemic based on their physiological and blood-related attributes. The project includes:
- A **Flask-based web application** to interact with the model
- Pre-trained model for predictions
- A detailed implementation of training, class balancing, and feature importance analysis

<div align="center">

## 🚀 Features

</div>

1. **Random Forest Classifier** for high accuracy predictions
2. **SMOTE (Synthetic Minority Oversampling Technique)** for handling class imbalance
3. **Feature Importance Analysis** to identify the most significant contributors to predictions
4. Simple **frontend interface** for user input

<div align="center">

## 📊 Performance Evaluation

*Model Comparison Analysis*

</div>

<div align="center">

| Algorithm            | Accuracy | AUC |
|:-------------------:|:--------:|:---:|
| Random Forest       | 99%      | 99% |
| Logistic Regression | 98%      | 98% |
| SVM                 | 90%      | 90% |
| KNN                 | 87%      | 87% |

</div>

*Random Forest Classifier demonstrates superior performance across both metrics.*

<div align="center">

## 🏗️ System Architecture

![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)

*The system follows a structured pipeline from dataset handling to model predictions.*

## 📊 Dataset Attributes

</div>

- 💉 **Hemoglobin Levels**
- 🔬 **Mean Corpuscular Volume (MCV)**
- 🧪 **Mean Corpuscular Hemoglobin (MCH)**
- 📈 **Mean Corpuscular Hemoglobin Concentration (MCHC)**
- 👤 **Gender**

<div align="center">

## ⚖️ Class Balance Management

![Balanced Dataset](images/After_SMOTE.png)

*Achieved perfect balance: 801 samples each for anemic and non-anemic classes using SMOTE*

## 🔍 Feature Importance Analysis

![Feature Importance](images/Feature_importance.png)

</div>

Key Contributors:
- 🔴 **Hemoglobin**: 83.9% contribution
- 👥 **Gender**: 9.1% contribution
- 🧬 **MCH**: 2.7% contribution

<div align="center">

## 🌐 Flask Web Application

</div>

### 🛠️ Application Structure
```bash
Directory structure:
└── yogeshwaran10-Anemia_detection/
    ├── README.md
    ├── app.py
    ├── forms.py
    ├── utils.py
    ├── images/
    ├── model/
    │   └── random_forest_classifier.pkl
    ├── static/
    │   └── style.css
    └── templates/
        ├── base.html
        ├── home.html
        └── result.html
```

<div align="center">

## 💻 Installation & Usage

</div>

### 1️⃣ Clone the Repository
```bash
git clone <repository_url>
cd anemia-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
python app.py
```

Then open the app in your browser at `http://127.0.0.1:5000/`

<div align="center">

## 📈 Results

</div>

- ✅ **High Accuracy**: Achieved through class balancing and Random Forest optimization
- 🎯 **Precise Predictions**: Driven by significant features like hemoglobin levels

<div align="center">

## 🔮 Future Scope

</div>

- 📊 **Expand dataset** to include more diverse features
- 🚀 **Implement advanced models** like XGBoost or LightGBM
- ☁️ **Cloud deployment** on AWS or Heroku

<div align="center">

## 📸 Screenshots

</div>

### 1. System Architecture
![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)

### 2. Balanced Dataset After SMOTE
![Balanced Dataset](images/After_SMOTE.png)

### 3. Feature Importance Analysis
![Feature Importance](images/Feature_importance.png)

---

<div align="center">

## 🤝 Contributing

Your contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

</div>
