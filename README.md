# AIML-TASK3: Housing Price Prediction with Linear Regression

## 📌 Project Overview

This project is part of the AI & ML Internship Task 3. The goal is to predict housing prices based on features like area and number of bedrooms using **Linear Regression**. The model helps understand the relationship between house features and pricing trends.

---

## ⚙️ Tools & Libraries

- **Programming Language**: Python  
- **Libraries**:
  - `pandas` – for data handling
  - `numpy` – for numerical computations
  - `matplotlib` – for data visualization
  - `scikit-learn` – for building the Linear Regression model

---

## 📁 Project Structure

AIML-TASK3/
├── Housing.csv # Dataset containing house features and prices
├── linear_regression.py # Python script implementing the model
├── requirements.txt # List of dependencies
└── README.md # Project documentation

yaml
Copy code

---

## 🧪 Steps Performed

1. **Data Loading & Exploration**: Loaded the dataset and explored its structure to understand features.  
2. **Feature Selection**: Selected `area` and `bedrooms` as input features, `price` as the target variable.  
3. **Data Splitting**: Split data into training and testing sets for evaluation.  
4. **Model Training**: Trained a Linear Regression model on the training data.  
5. **Model Evaluation**: Evaluated the model using:
   - Mean Absolute Error (MAE)  
   - Mean Squared Error (MSE)  
   - R² Score  

---

## 🛠️ Setup & Installation

### Clone the Repository

```bash
git clone https://github.com/Santhoshguthpe/AIML-TASK3.git
cd AIML-TASK3
Install Dependencies
bash
Copy code
pip install -r requirements.txt
🚀 Usage
Run the linear_regression.py script to train the model and see results:

bash
Copy code
python linear_regression.py
📈 Sample Output
Expected output after running the script:

yaml
Copy code
Mean Absolute Error: 5000.00
Mean Squared Error: 25000000.00
R² Score: 0.95
