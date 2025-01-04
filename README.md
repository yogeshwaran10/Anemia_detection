# Anemia Detection Using Machine Learning 🚑

## Overview 🩺
This project implements a **Random Forest Classifier** to predict whether an individual is anemic or non-anemic based on their physiological and blood-related attributes. The project includes:

- A **Flask-based web application** to interact with the model.
- Pre-trained model for predictions.
- A detailed implementation of training, class balancing, and feature importance analysis.

## Features 🚀
1. **Random Forest Classifier** for high accuracy predictions.
2. **SMOTE (Synthetic Minority Oversampling Technique)** for handling class imbalance.
3. **Feature Importance Analysis** to identify the most significant contributors to predictions.
4. Simple **frontend interface** for user input.

## System Architecture 🏗️
![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)
*The system follows a structured pipeline from dataset handling to model predictions.*

## Dataset 📊
The dataset contains the following attributes:
- Hemoglobin Levels
- Mean Corpuscular Volume (MCV)
- Mean Corpuscular Hemoglobin (MCH)
- Mean Corpuscular Hemoglobin Concentration (MCHC)
- Gender

## Steps to Handle Imbalance ⚖️
To ensure balanced predictions, **SMOTE** was applied to generate synthetic samples for the minority class. The result is a perfectly balanced dataset:

![Balanced Dataset](images/After_SMOTE.png)
*801 samples each for anemic and non-anemic classes.*

## Feature Importance 🔍
Analyzing the Random Forest model revealed the most significant features:

![Feature Importance](images/Feature_importance.png)
- **Hemoglobin** is the most influential feature, contributing 83.9% to the prediction.
- Other significant features include **Gender** (9.1%) and **MCH** (2.7%).

## Flask Web Application 🌐
The application provides an easy-to-use interface where users can input their data to receive predictions.

### Application Structure 🛠️
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

## Installation & Usage 💻
Follow these steps to run the application locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd anemia-detection
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. Open the app in your browser at `http://127.0.0.1:5000/`.

## Results 📈
- The model achieved **high accuracy** and robustness due to class balancing and the use of Random Forest.
- Significant features such as hemoglobin levels drive accurate predictions.

## Future Scope 🔮
- **Expand dataset** to include more diverse features.
- Implement advanced models like **XGBoost** or **LightGBM**.
- Deploy on a cloud platform like AWS or Heroku.

## Repository 📂
This project includes:
1. **Training script** (detailed implementation included in the report).
2. **Flask app** for predictions.
3. **Documentation** and visualizations for easy understanding.

---
### Screenshots 📸
#### 1. System Architecture
![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)
#### 2. Balanced Dataset After SMOTE
![Balanced Dataset](images/After_SMOTE.png)
#### 3. Feature Importance Analysis
![Feature Importance](images/Feature_importance.png)

---

## Contributing 🤝
Contributions are welcome! If you find any bugs or have suggestions, feel free to raise an issue or create a pull request.

## License 📜
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
