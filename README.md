# Diabetes Predictor 🏥🔬

## 📌 Overview
Diabetes Predictor is a **machine learning model** that predicts the likelihood of diabetes in individuals based on medical parameters. Using **Multiple Linear Regression**, this project provides an accurate risk assessment, enabling early detection and preventive measures.

## 🚀 Features
- **Predicts likelihood of diabetes** using a trained machine learning model.
- **Uses Multiple Linear Regression** to analyze medical variables.
- **Two Versions:**
  - **Hospital Version:** Reads medical reports and applies machine learning.
  - **Manual Version:** Allows users to input common metrics for an estimation.
- **Dataset from the PIMA Indian Study**, ensuring reliability.
- **Web Interface powered by Streamlit** for easy accessibility.

## 🛠️ Technologies Used
- **Programming Language:** Python 🐍
- **Libraries:** Pandas, NumPy, Scikit-learn, Streamlit, Tabula (for PDF report processing)
- **Machine Learning Model:** Multiple Linear Regression
- **Dataset:** PIMA Indian Diabetes Dataset (Kaggle)

## 📊 Model Workflow
1. **Data Preprocessing:**
   - Cleaned dataset from Kaggle.
   - Train-test split (75-25 ratio).
   - Root Mean Squared Error (RMSE) used for accuracy check.
2. **Model Training:**
   - Multiple Linear Regression applied to identify key predictors.
   - Continuous variable scale applied for predictions.
3. **Prediction Outputs:**
   - 0.0 - 0.3: **Unlikely to be Diabetic**
   - 0.3 - 0.49: **At Risk**
   - 0.5 - 0.79: **Likely to be Diabetic**
   - 0.8 - 1.0: **Most Likely to be Diabetic**
4. **Web Interface Implementation:**
   - **Hospital Version:** Reads medical reports via Tabula.
   - **Manual Version:** Users input values manually for estimation.

## 🔍 Results & Accuracy
- **Training Data:** 768 samples (PIMA Indian Diabetes Dataset).
- **RMSE Score:** 0.0035 (indicating strong accuracy for medical applications).
- **Key Contributing Variables:**
  - Diabetes Pedigree Function
  - Number of Pregnancies
  - BMI
  - Glucose Levels
  - Age

## 🏥 Future Scope
- **Integration with Electronic Medical Records (EMR)** for real-time predictions.
- **Expanding dataset** to include multiple ethnicities for a broader scope.
- **Improved deep learning models** to increase accuracy beyond linear regression.
- **Mobile Application Development** for easier accessibility.

## 📂 Installation & Usage
### 1️⃣ Clone the Repository
```bash
  git clone https://github.com/anirudhsengar/DiabetesPredictor.git
  cd DiabetesPredictor
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 📬 Connect with Me!
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/anirudh-sengar-21b9a722a/)  
[![Email](https://img.shields.io/badge/Email-anirudhsengar3%40gmail.com-red?logo=gmail)](mailto:anirudhsengar3@gmail.com)  

---
⭐ **Early detection can save lives – Let’s make healthcare smarter with AI!**
