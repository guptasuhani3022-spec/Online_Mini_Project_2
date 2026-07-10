# 🏦 Loan Approval Prediction System

A Machine Learning web application built with **Python**, **Streamlit**, and **Decision Tree Classifier** to predict whether a loan application will be approved based on customer details.

---

## 📌 Project Overview

This application predicts the loan approval status using a Decision Tree Machine Learning model.

The user enters:

- 💵 Income
- 🎼 CIBIL Score
- 💰 Loan Amount
- 👱 Employment Years

The model predicts whether the loan is **Approved** or **Rejected**.

If approved, the application also calculates the estimated approved loan amount.

---

## 🚀 Features

- User-friendly Streamlit interface
- Loan Approval Prediction
- Decision Tree Classifier
- Displays Model Accuracy
- Calculates Approved Loan Amount
- Interactive Sidebar Inputs

---

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Scikit-learn

---

## 📂 Dataset

Dataset File:

```
loan.csv
```

Required Columns:

- Income
- CIBIL_Score
- Loan_Amount
- Employment_Years
- Loan_Status

---

## 📊 Machine Learning Model

Algorithm Used:

- Decision Tree Classifier

Parameters:

```python
DecisionTreeClassifier(
    max_depth=3,
    min_samples_split=8,
    min_samples_leaf=4,
    random_state=42
)
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Loan-Approval-Prediction.git
```

Go to project folder

```bash
cd Loan-Approval-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
streamlit run app.py
```

Or run on another port

```bash
streamlit run app.py --server.port 8502
```

---

## 📷 Application Workflow

1. Load Dataset
2. Train Decision Tree Model
3. Calculate Model Accuracy
4. User Enters Loan Details
5. Predict Loan Status
6. Display Result

---

## 📈 Sample Inputs

| Feature | Example |
|---------|---------|
| Income | 40000 |
| CIBIL Score | 700 |
| Loan Amount | 200000 |
| Employment Years | 5 |

---

## 📋 Output

✅ Loan Approved

or

❌ Loan Rejected

If approved:

```
Approved Loan Amount: ₹xxxxxx
```

---

## 📁 Project Structure

```
Loan-Approval-Prediction/
│
├── app.py
├── loan.csv
├── README.md
└── requirements.txt
```

---

## 👩‍💻 Author

**Suhani Gupta**

 Aspiring AI Engineer, Python & Machine Learning Enthusiast

---

## 📄 License

This project is created for educational and learning purposes.
