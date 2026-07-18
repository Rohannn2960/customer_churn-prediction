# 📊 Customer Churn Prediction using Machine Learning

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, account information, and subscribed services. The project includes data preprocessing, exploratory data analysis (EDA), model comparison, and deployment using Streamlit.

---

## 🚀 Live Demo

🌐 **Streamlit App:**  
https://rohannn2960-customer-churn-prediction-app-jnm2lf.streamlit.app/

📂 **GitHub Repository:**  
https://github.com/Rohannn2960/customer_churn-prediction

---

## 📌 Problem Statement

Customer churn is one of the biggest challenges faced by telecommunication companies. Losing existing customers directly impacts revenue and increases customer acquisition costs.

The objective of this project is to build a machine learning model that predicts whether a customer is likely to churn. By identifying at-risk customers early, businesses can take proactive measures such as offering discounts, improving customer support, or introducing personalized retention strategies.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer information such as:

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- Churn (Target Variable)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

---

## 📈 Project Workflow

### 1. Data Cleaning
- Converted `TotalCharges` to numeric
- Handled missing values
- Removed unnecessary columns

### 2. Exploratory Data Analysis
- Distribution of churn
- Correlation heatmap
- Tenure vs Churn
- Monthly Charges vs Churn
- Customer insights

### 3. Data Preprocessing
- Missing value imputation
- One-Hot Encoding
- ColumnTransformer
- Scikit-learn Pipeline

### 4. Model Building
The following machine learning models were trained and evaluated:

- Logistic Regression
- Random Forest
- XGBoost

### 5. Model Evaluation
Models were compared using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- ROC Curve

---

## 📊 Model Performance

| Model | Accuracy | ROC-AUC |
|--------|----------|----------|
| Logistic Regression | **75.5%** | **0.858** |
| Random Forest | 74.4% | 0.854 |
| XGBoost | **79.9%** | 0.834 |

Although **XGBoost achieved the highest accuracy**, **Logistic Regression** was selected as the final model because customer churn prediction prioritizes identifying customers at risk of leaving. Logistic Regression achieved the highest ROC-AUC and the best recall for the churn class, making it the most suitable model for customer retention.

---

## 🌐 Streamlit Application

The trained Logistic Regression pipeline was saved using **Joblib** and deployed with **Streamlit**, allowing users to enter customer details and receive churn predictions in real time.

---

## 📁 Project Structure

```
customer-churn-prediction/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── models/
│   └── customer_churn_model.pkl
│
├── notebooks/
│   └── Customer_Churn_Prediction_End_to_End_ML.ipynb
│
└── src/
```

---

## ▶️ How to Run Locally

Clone the repository:

```bash
git clone https://github.com/Rohannn2960/customer_churn-prediction.git
```

Navigate to the project folder:

```bash
cd customer_churn-prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🔮 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Feature importance analysis
- SHAP explainability
- Docker deployment
- REST API using FastAPI
- Cloud deployment with AWS/Azure

---

## 👨‍💻 Author

**Rohan Tammana**

GitHub: https://github.com/Rohannn2960

---

⭐ If you found this project useful, consider giving it a star!
