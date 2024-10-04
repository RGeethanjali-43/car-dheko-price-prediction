**Car-dheko-price-prediction**
Car Dheko - Used Car Price Prediction
**Objective**:
To develop a Random Forest Regressor model that  predicts car price based on historical data and car features.

**Data Description:**

**Dataset Overview**:

**Source**: Collected from various car listing datasets from car dheko

**Format**: The dataset in CSV format, containing both numerical and categorical features related to car 

specifications and sales

## Features(Columns):

### Numerical Features:

Year: The year in which car was manufactured
km:    Total miles the car has travelled
Owner no: Number of previous owners
Power: Power output of the car

**Categorical Features**:

bt: Body type of the car
Model: Specific model of the car(Mustang, Corolla)
Fuel Type: Type of the fuel used by  the car

**Target variable**:
Price: Selling price of the car(target variable for prediction)

## Data Cleaning:

### Missing Values:

Numerical features like `Mileage` and `Engine` were filled with median values.

Categorical features like `Model`  and `bt` were filled with mode values.

### **Data Type conversion:**

Changed string to correct data type:

Removed unwanted  characters like ‘$’, ’” ”’,’%’

---

## Feature Enginnering:

### Encoding categorical variables:

Used Label Encoder for categorical features like `Model` ,`bt`, `Fuel Type`.

## Data Splitting:

### Train Test split:

The data was split to 80% training  and  20% of  testing using 

`train_test_split()` from scikit learn.

## Model Development:

### Model Selection:

The Random forest  algorithm was chosen for ability to handle non linear relationships and complex

interactions between features which makes it suitable for car price predictions

### Model Training:

The  Random forest model was trained on the preprocessed  data using `RandomForestRegressor`

class from **Scikit- Learn**

### Model Hyper Parameters:

`n_estimators`:  300(number of trees in the forest)

`max_depth:` none(max depth of each tree)

`min_samples_split:` 3(minimum number of samples to split mode)

`random_state`: 42(For reproductivity)

---

**Model Evaluation**:

**Metrics**:

The following evaluation metrics are used to evaluate the performance of the model

**Mean Absolute Percentage Error(MAPE):** 

**Mean Squared Error(MSE)**: 30730036

**R squared Error:** 0.99(indicating 99% of variance in the car prices explained by the model)

Feature Importance:

The top features influencing car predictions
Model Year
Width
Length
Maxpower

---

**Model Deployment**:

**Deployment method**:

The model is deployed as a Streamlit web application  allowing users to input  car features and get

price predictions.

Here I attach my streamlit application link:  **http://localhost:8501/**

### Future Improvements

Experiment with hyper parameter tuning (eg:GridsearchCV) to optimize the model performance

Add additional features like  Power_to_weight, Accel_to_TopSpeed, Displacement_per_Cylinder

### Accuracy:

**r2_score:**

RandomForestRegressor  using top 10 features: **1.00**

GradientBoostingRegressor  with  GridSearchCV: **93.38**

LassoRegressor  to check overfitting: **93.38**

cross_val_score: **0.77**
