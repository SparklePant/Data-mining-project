# Final Project for Data Mining CAP4770

Project Name: Customer Churn Prediction

Group Members:
- Daniel Eckman
- Cole Compton
- Melanie Vogt

Project Overview:
The goal of this project is to build a machine learning model that predicts whether a customer will leave a company (churn) based on demographic and service-related features.

In addition to prediction, this project identifies which features contribute most to customer churn. These insights can help businesses improve strategies for retaining customers and reduce revenue loss.

Dataset Used: IBM Telco Dataset
Source: https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset
The dataset contains information on over 7000 customers and includes the following data:
    - Demographics (gender, senior status, dependents)
    - Account Information (tenure, contract type, billing)
    - Services (internet, phone, streaming)
    - Charges (monthly and total)
    - Churn outcome

Technologies Used:
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- OpenPyXL

Steps Taken:
1. Data Cleaning:
    - Removed unnecessary columns as well as columns that may cause data leakage
    - Converted numeric fields
    - Handled missing values
2. Exploratory Data Analysis (EDA)
    - Created plots for visualization of churn distribution
    - Analyzed relationships between churn and monthly charges, tenure, as well as contract types.
3. Data Preprocessing
    - Converted categorical variables using one-hot encoding (pd.get_dummies()).
4. Modeling
    - Logistic Regression
    - Random Forest
5. Evaluated Models Using:
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - Confusion matrix
6. Model Feature Importance
    - Logistic Regression coefficients
    - Random Forest

Key Findings:
- Customers with month-to-month contracts and higher monthly charges are more likely to churn.
- Certain service features influence churn behavior.

Setup Instructions:
1. Create Virtual Environment (venv): run command: python3 -m venv venv
2. Activate Virtual Environment: 
    MacOs/Linux: run command: source venv/bin/activate
    Windows:     run command: venv\Scripts\activate
3. Install Dependencies: run command: pip install -r requirements.txt
4. Running the Project: 
    run command: jupyter notebook
    from jupyter notebook: Run all cells from top to bottom
 
Project Structure
├── .gitignore
├── final_project.ipynb
├── README.md
├── requirements.txt
├── setup_mysql_database.py
└── Telco-Customer-Churn.xlsx

Notes:
- The dataset includes additional fields such as Churn Score, CLTV, and Churn Reason, which were removed to avoid data leaks.
- Logistic Regression required feature scaling for proper convergence.

Conclusion:
This project uses machine learning to predict customer churn and to identify key components of customer behavior, which in turn can aid in creating strategies that reduce the possibility.
