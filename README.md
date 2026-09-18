# Loan Prediction System

A Machine Learning project that predicts whether a loan application will be approved or not based on applicant and loan-related information.

## Project Overview

The goal of this project is to build a classification model that can predict loan approval status from historical loan application data.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

## Machine Learning

The project includes:

* Data preprocessing
* Handling categorical data
* Label Encoding
* Replacing `3+` dependents with `4`
* Train-test split
* Stratified sampling
* Classification model
* Model evaluation
* Streamlit web application

## Project Structure

```text
Loan-Prediction/
│
├── main.py
├── model.pkl
├── loan_prediction.csv
└── README.md
```

## Preprocessing

The dataset is cleaned by removing unnecessary columns and converting categorical values into numerical values.

The `Dependents` column is processed by replacing:

```text
3+ → 4
```

Categorical columns are then converted into numerical values using `LabelEncoder`.

The data is divided into training and testing sets using `train_test_split`.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Go to the project folder

```bash
cd Loan-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install pandas numpy scikit-learn streamlit
```

### 6. Run the Streamlit app

```bash
streamlit run main.py
```

## Application

The Streamlit application allows the user to enter loan-related information and receive a prediction:

* Loan Approved
* Loan Not Approved

## Future Improvements

* Improve model accuracy
* Try different classification algorithms
* Add better input validation
* Improve the Streamlit user interface
* Deploy the appl
