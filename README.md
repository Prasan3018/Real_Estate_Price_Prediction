# Real_Estate_Price_Prediction
Predicting the Land Price for the Real Estate Lands using Machine Learning.

# 🏡 Bangalore House Price Prediction – Data Science Project

This project predicts house prices in Bangalore using **Machine Learning**.  
The goal is to build an **accurate, clean, and explainable ML model** by applying solid data science practices such as EDA, feature engineering, outlier removal, and model selection.

---

## 📌 Project Overview
Bangalore's real-estate market is dynamic and highly location-dependent.  
This project applies data science techniques to estimate house prices based on:

- 📏 Square feet area  
- 🛏 BHK count  
- 🚿 Number of bathrooms  
- 📍 Location within Bangalore  

The final model can predict property prices with strong reliability after cleaning and transforming raw housing data.

---

## 🧹 1. Data Cleaning & Preprocessing
Performed extensive cleaning to prepare raw housing data for modeling:

- Removed inconsistent & duplicate entries  
- Handled missing values  
- Processed categorical features (locations)  
- Converted text-based size fields into numeric values  
- Dropped unrealistic or extreme outliers  
- Scaled important numerical columns where needed  

---

## 🔍 2. Exploratory Data Analysis (EDA)
Performed EDA to understand market patterns:

- Price distribution by location  
- Relationship between sqft, BHK, and price  
- Outlier detection using boxplots & scatter plots  
- Understanding multi-collinearity  
- Visualization of price-per-square-foot trends  

Insights from EDA directly influenced feature engineering and model training.

---

## 🧠 3. Feature Engineering
Applied ML-focused transformations:

- Created **one-hot encoded features** for Bangalore locations  
- Created price-per-square-foot metrics  
- Engineered meaningful filters to remove noisy datapoints  
- Built a clean feature matrix (X) and prediction target (y)

---

## 🤖 4. Model Building
Several regression algorithms were tested:

- Linear Regression  
- Lasso Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

After comparison, the final model was chosen based on:

- RMSE score  
- Cross-validation performance  
- Generalization capability  

The trained model was exported as `.pickle` for deployment.

---

## 🏆 Final Model Performance
- Strong prediction consistency  
- Handles location-based variations accurately  
- Robust to moderate outliers after cleaning  
- Lightweight and fast to infer  

---

## 🌐 5. Deployment (Simple Interactive Web Page)
A lightweight interactive webpage was created to enter:

- Area (sqft)  
- BHK  
- Bathrooms  
- Location  

The model returns the **predicted house price instantly**.

*(Web deployment is minimal — the main focus of this project is the data science and ML pipeline.)*

---

## 📁 Project Structure


