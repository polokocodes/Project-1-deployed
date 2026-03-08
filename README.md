# Project-1-deployed
# 🏦 Loan Default Prediction App

A machine learning web app that predicts whether a loan applicant is likely to default based on their personal and financial information.

## 🚀 Demo
[Live App](#) <https://project-1-deployed-3sv69zlvdsubudkowgkmej.streamlit.app/)>

## 📋 Features
- Predicts loan default risk (0 = No Default, 1 = Default)
- Searchable profession and state selectors
- Target encoding for profession and state risk mapping


## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **ML:** Scikit-learn, logistic regression
- **Data Processing:** Pandas, NumPy

## ⚙️ Installation

```bash
git clone https://github.com/your-username/project-1-deployed.git
cd project-1-deployed
pip install -r requirements.txt
streamlit run loan_app.py
```

## 📁 Project Structure
```
├── loan_app.py              # Streamlit web app
├── loan_data_model.pkl      # Trained ML model
├── prof_means.pkl           # Profession target encoding
├── state_means.pkl          # State target encoding
├── requirements.txt
└── README.md
```

## 📊 Dataset
- 252,000 loan applicant records
- 13 features including age, experience, profession, state, and ownership details
- Target: `Risk_Flag` (0 = no default, 1 = default)
- Class imbalance: 87.7% no default, 12.3% default 


