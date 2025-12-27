🧠 Introvert vs Extrovert Personality Prediction
📌 Project Overview

This project focuses on predicting a person’s personality type (Introvert or Extrovert) using behavioral and social features.
The goal is to build a robust supervised classification system by applying proper data analysis, preprocessing, and multiple machine learning models.

Rather than treating ML as a black box, this project emphasizes data understanding, feature behavior, and model comparison.

📊 Dataset Description

Rows: 2900 → cleaned to 2498 after removing duplicates

Columns: 8

Target Variable: Personality

0 → Introvert

1 → Extrovert

Features Used
Feature	Description
Time_spent_Alone	Time spent alone
Social_event_attendance	Frequency of attending social events
Going_outside	How often the person goes outside
Friends_circle_size	Number of friends
Post_frequency	Social media post frequency
Stage_fear	Stage fear (Yes/No)
Drained_after_socializing	Feels drained after socializing (Yes/No)
🔍 Exploratory Data Analysis (EDA)

Dataset overview using a custom smart overview function

Duplicate detection and removal

Distribution analysis (histograms & KDE plots)

Categorical value counts

Correlation heatmap

Boxplots & violin plots for personality comparison

Outlier detection using IQR method (no significant outliers found)

🧹 Data Preprocessing

Removed duplicate records

Binary encoding for categorical variables (Yes → 1, No → 0)

One-Hot Encoding for categorical features

Feature–target separation

Train–test split (80/20)

🤖 Models Trained

Multiple classification models were trained and compared:

Logistic Regression

K-Nearest Neighbors (KNN)

Decision Tree

Random Forest

Naive Bayes

Support Vector Machine (SVM)

Gradient Boosting

XGBoost

📈 Model Performance

Most models achieved ~90–91% accuracy, showing strong and consistent performance.

Model	Accuracy
Logistic Regression	~90.6%
KNN	~90.6%
Decision Tree	~90.6%
Random Forest	~90.8%
Naive Bayes	~90.8%
SVM	~90.8%
Gradient Boosting	~90.6%
XGBoost	~87.8%

Random Forest was selected as the final model due to stability and strong generalization.

❌ Error Analysis

Total incorrect predictions: 61

Misclassified samples were extracted and analyzed to understand model confusion patterns.

💾 Model Saving

The final trained model was saved using joblib for future inference or deployment.

joblib.dump(final_model, 'personality_model.pkl')

🛠️ Tech Stack & Libraries

Python

pandas, numpy

seaborn, matplotlib, plotly

scikit-learn

XGBoost

CatBoost

joblib

🎯 Key Learnings

Importance of EDA before modeling

Handling categorical variables correctly

Comparing multiple models instead of relying on one

Understanding that higher complexity doesn’t always mean better performance

Model evaluation beyond just accuracy

🚀 Future Improvements

Hyperparameter tuning using GridSearchCV / RandomizedSearchCV

Feature importance & explainability (SHAP)

Model deployment using Flask / FastAPI

UI integration for real-time prediction

📌 Author

Bushra
Machine Learning & AI Enthusiast
