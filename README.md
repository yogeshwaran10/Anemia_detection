<div align="center">

# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Ambulance.png" alt="Ambulance" width="25" height="25"/> Anemia Detection Using Machine Learning <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Ambulance.png" alt="Ambulance" width="25" height="25"/>

*An intelligent system for predicting anemia using Random Forest Classification*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Stethoscope.png" alt="Stethoscope" width="25" height="25"/> Overview
</div>

This project implements a **Random Forest Classifier** to predict whether an individual is anemic or non-anemic based on their physiological and blood-related attributes. The project includes:
- A **Flask-based web application** to interact with the model
- Pre-trained model for predictions
- A detailed implementation of training, class balancing, and feature importance analysis
- **NEW FEATURE**: Upload a **blood report image** to predict anemia using **Google Gemini 2.0 Flash** for text extraction

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Rocket.png" alt="Rocket" width="25" height="25"/> Features

</div>

1. **Random Forest Classifier** for high accuracy predictions
2. **SMOTE (Synthetic Minority Oversampling Technique)** for handling class imbalance
3. **Feature Importance Analysis** to identify the most significant contributors to predictions
4. Simple **frontend interface** for user input
5. **NEW**: **Image-Based Prediction** – Upload a **blood test report** image to automatically extract relevant values and get predictions

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bar%20Chart.png" alt="Chart" width="25" height="25"/> Performance Evaluation

*Model Comparison Analysis*

| Algorithm            | Accuracy | AUC |
|:-------------------:|:--------:|:---:|
| Random Forest       | 99%      | 99% |
| Logistic Regression | 98%      | 98% |
| SVM                 | 90%      | 90% |
| KNN                 | 87%      | 87% |

</div>

*Random Forest Classifier demonstrates superior performance across both metrics.*

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Classical%20Building.png" alt="Architecture" width="25" height="25"/> System Architecture

![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)

*The system follows a structured pipeline from dataset handling to model predictions.*

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20Index%20Dividers.png" alt="Dataset" width="25" height="25"/> Dataset Attributes

</div>

- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Syringe.png" alt="Syringe" width="20" height="20"/> **Hemoglobin Levels**
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Microscope.png" alt="Microscope" width="20" height="20"/> **Mean Corpuscular Volume (MCV)**
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Test%20Tube.png" alt="Test Tube" width="20" height="20"/> **Mean Corpuscular Hemoglobin (MCH)**
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" alt="Chart" width="20" height="20"/> **Mean Corpuscular Hemoglobin Concentration (MCHC)**
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Bust%20in%20Silhouette.png" alt="Person" width="20" height="20"/> **Gender**

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Balance%20Scale.png" alt="Balance" width="25" height="25"/> Class Balance Management

![Balanced Dataset](images/After_SMOTE.png)

*Achieved perfect balance: 801 samples each for anemic and non-anemic classes using SMOTE*

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Magnifying%20Glass%20Tilted%20Left.png" alt="Magnifying Glass" width="25" height="25"/> Feature Importance Analysis

![Feature Importance](images/Feature_importance.png)

</div>

Key Contributors:
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Red%20Square.png" alt="Red Square" width="20" height="20"/> **Hemoglobin**: 87.0% contribution
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People/Busts%20in%20Silhouette.png" alt="People" width="20" height="20"/> **Gender**: 9.1% contribution
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/DNA.png" alt="DNA" width="20" height="20"/> **MCH**: 2.7% contribution
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Syringe.png" alt="Syringe" width="20" height="20"/> **Others**: 1.2% contribution

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Globe%20with%20Meridians.png" alt="Web" width="25" height="25"/> Flask Web Application

</div>

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" alt="Tools" width="25" height="25"/> Application Structure
```bash
Directory structure:
└── yogeshwaran10-anemia_detection/
    ├── README.md
    ├── Procfile
    ├── app.py
    ├── process_image.py
    ├── requirements.txt
    ├── runtime.txt
    ├── utils.py
    ├── images/
    ├── model/
    │   └── random_forest_classifier.pkl
    ├── static/
    │   └── style.css
    └── templates/
        └── index.html
```

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Desktop%20Computer.png" alt="Computer" width="25" height="25"/> Installation & Usage

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

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Chart%20Increasing.png" alt="Results" width="25" height="25"/> Results

</div>

- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Symbols/Check%20Mark%20Button.png" alt="Check" width="20" height="20"/> **High Accuracy**: Achieved through class balancing and Random Forest optimization
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Direct%20Hit.png" alt="Target" width="20" height="20"/> **Precise Predictions**: Driven by significant features like hemoglobin levels
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Camera.png" alt="Camera" width="20" height="20"/> **New Image Upload Feature**: Extracts blood test attributes automatically for prediction

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Crystal%20Ball.png" alt="Future" width="25" height="25"/> Future Scope

</div>

- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Bar%20Chart.png" alt="Chart" width="20" height="20"/> **Expand dataset** to include more diverse features
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Rocket.png" alt="Rocket" width="20" height="20"/> **Implement advanced models** like XGBoost or LightGBM
- **Address Feature scaling** importance to other features

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Camera%20with%20Flash.png" alt="Camera" width="25" height="25"/> Screenshots

### 1. System Architecture
![System Architecture](images/diagram-export-5-21-2024-4_49_14-PM.png)

### 2. Balanced Dataset After SMOTE
![Balanced Dataset](images/After_SMOTE.png)

### 3. Feature Importance Analysis
![Feature Importance](images/Feature_importance.png)
</div>

---

<div align="center">

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Globe%20with%20Meridians.png" alt="Globe" width="25" height="25"/> **Live Deployment** ☁️ **Deployed on Render**

You can try the deployed version of the application here <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Rocket.png" alt="Rocket" width="20" height="20"/>:

[**Anemia Detection App**](https://anemia-detection-46ji.onrender.com)

---

</div>

### **Outcome Variable Explanation:**

The **outcome variable** in the dataset indicates the final diagnosis or classification for each patient. The outcome is binary, with two possible values:

- **Not Anemic**: The patient is not anemic, based on clinical criteria and test results.
- **Anemic**: The patient is anemic, suggesting a deficiency of red blood cells or hemoglobin in the blood.

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Handshake.png" alt="Handshake" width="25" height="25"/> Contributing

Your contributions are welcome! Feel free to:
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Bug.png" alt="Bug" width="20" height="20"/> Report bugs
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Light%20Bulb.png" alt="Idea" width="20" height="20"/> Suggest features
- <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Wrench.png" alt="Wrench" width="20" height="20"/> Submit pull requests

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Honeybee.png" alt="Bee" width="25" height="25"/> License

This project is licensed under the MIT License. See the `LICENSE` file for details.

</div>
