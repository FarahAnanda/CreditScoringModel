# CreditScoringModel

## Project Overview
This project builds a credit score prediction model and deploys it as a web application using Streamlit. The model predicts credit scores based on various financial features.

## Dataset
The dataset used in this project was obtained from Kaggle. I used the [cleaned dataset](https://www.kaggle.com/datasets/clkmuhammed/creditscoreclassification/data?select=train.csv/@blank) since the dataset is too messy and the focus of this project is modeling credit score. The original dataset can be found [here](https://www.kaggle.com/datasets/parisrohan/credit-score-classification/@blank).

### Dataset Description
The dataset includes credit-related information for various individuals. Below is a description of the columns in the dataset:

| **Feature**                  | **Description**                                                        |
|------------------------------|------------------------------------------------------------------------|
| ID                           | A unique identification of an entry                                    |
| Customer_ID                  | A unique identification of a person                                     |
| Month                        | The month of the year                                                   |
| Name                         | Name of a person                                                        |
| Age                          | Person's age                                                             |
| SSN                          | The social security number of a person                                   |
| Occupation                    | Occupation of the person                                                 |
| Annual_Income                 | Annual income of the person                                               |
| Monthly_Inhand_Salary         | Monthly base salary of a person                                           |
| Num_Bank_Accounts             | Total bank accounts a person holds                                       |
| Num_Credit_Card               | Total other credit cards held by a person                                |
| Interest_Rate                 | Interest rate on credit card                                             |
| Num_of_Loan                   | Total loans taken from the bank                                          |
| Type_of_Loan                  | Types of loan taken by a person                                          |
| Delay_from_due_date           | Average number of days delayed from the payment date                    |
| Num_of_Delayed_Payment        | Average number of payments delayed by a person                          |
| Changed_Credit_Limit          | Percentage change in credit card limit                                   |
| Num_Credit_Inquiries          | Total credit card inquiries                                              |
| Credit_Mix                    | Classification of the mix of credits                                     |
| Outstanding_Debt              | The remaining debt to be paid (in USD)                                   |
| Credit_Utilization_Ratio      | Utilization ratio of credit card                                         |
| Credit_History_Age            | Length of credit history of the person                                   |
| Payment_of_Min_Amount         | Whether only the minimum amount was paid by the person                   |
| Total_EMI_per_month           | The monthly EMI payments (in USD)                                        |
| Amount_invested_monthly       | The monthly amount invested by the customer (in USD)                     |
| Payment_Behaviour             | Payment behavior of the customer                                         |
| Monthly_Balance               | Monthly balance amount of the customer (in USD)                          |
| Credit_Score                  | The bracket of credit score (Poor, Standard, Good)                       |

## [`model_building.ipynb`](model_building.ipynb)

### Data Preparation
1. **Data Import**: The dataset is loaded using `pandas` and contains 100,000 rows with various financial features.
2. **Data Cleaning**: Irrelevant columns such as `ID`, `Customer_ID`, `Name`, and others not considered in credit score calculation are dropped.
3. **Feature Selection**: Features with low correlation to the credit score are removed. The remaining features are used to calculate weighted scores for different credit scoring aspects.

### Data Exploration
- Histograms and bar plots are used to explore the distribution of continuous and categorical variables.
- Correlation analysis is performed to understand the relationship between features and the credit score.

### Feature Engineering
1. **Score Calculation**: The credit score is recalculated based on weighted factors:
   - Payment History (40%)
   - Amounts Owed (35%)
   - Length of Credit History (15%)
   - Credit Mix (10%)
2. **Normalization**: The raw credit score is normalized to a range of 300 to 850.

### Model Building
1. **Data Splitting**: The dataset is split into training and testing sets.
2. **Model Training**: Four regression models are trained:
   - Linear Regression
   - Random Forest Regressor
   - XGBoost Regressor
   - Gradient Boosting Regressor
3. **Model Evaluation**: Each model's performance is evaluated using Mean Squared Error (MSE) and R-squared metrics.

### Results
Linear Regression performs the best with an MSE of 0.0000 and an R-squared value of 1.0000. It was saved using `pickle` for future use.

## [`credit_scoring.py`](credit_scoring.py)
Script for a web application for predicting credit scores based on user inputs. It uses a pre-trained model ([`credit_score_model.pkl`](credit_score_model.pkl)) to estimate credit scores from features like the number of bank accounts, credit cards, loans, and other financial metrics. Users input their financial details through a web interface, and the script displays the predicted credit score. This tool is designed to be run in the Jupyter Lab terminal using this command:

```bash
streamlit run credit_scoring.py
```
The web app can be found in [here](https://mycreditscoringmodel.streamlit.app/@blank)

## Notes

This model isn't perfect due to the lack of data on new credit histories. It also has limitations because the `credit_utilization_ratio` feature in the training dataset ranges only from 20% to 50%. Thus, predictions may not be accurate if the credit utilization ratio is below 10% or above 50%.
