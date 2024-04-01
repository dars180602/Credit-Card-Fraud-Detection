# Credit-Card-Fraud-Detection
Our project, centered on the development of an advanced Credit Card Fraud Detection Model is a Capstone Project developed by Cecille Jatulan, Maria Melencio, Michael Montanez, David Higuera, and Diana Reyes, students of the Big Data Analytics program at Lambton College.

## Data Source
The dataset used in this project is sourced from Kaggle. Credit Card Fraud Detection Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download

Please note that for the sake of convenience, the data was initially downloaded from the provided source and subsequently uploaded to Google Drive for storage and access.

## Data Overview
The dataset contains only numerical input variables resulting from a Principal Component Analysis (PCA) transformation. Due to confidentiality constraints, the original features and additional background information about the data are not provided.

Features V1 through V28 are the principal components obtained via PCA.
Features Time and Amount have not undergone PCA transformation.
Feature Time represents the elapsed time in seconds between each transaction and the first transaction in the dataset.
Feature Amount denotes the transaction amount, which can be utilized for example-dependent cost-sensitive learning.
The target variable, Feature Class, denotes the transaction's classification as fraudulent (1) or non-fraudulent (0).

Thank you for your interest in our project! If you have any questions or suggestions, please feel free to reach out. We appreciate your feedback.

Timeline and Deliverables: https://docs.google.com/spreadsheets/d/1JDPSTqTU8q4MK3zN5AF9vBCsO8XDJI5lD9oyeVHPxPM/edit#gid=1115838130

Google Colab Link: https://colab.research.google.com/drive/1D-RRUslLfotFEVqwImfes5CWee3Yot3I?usp=sharing#scrollTo=7RHcIuyRaA8B


**Sample Input Array for the UI**

**Fraudulent:** 6986, -2.592844218, 2.679786967, -3.496197293, -4.801637406, -10.91281932, -6.771096725, -7.358083221, -12.59841854, -5.131548628, 0.308333946, -0.171607879, 0.573574068, -0.053501865, -0.827135715, 0.84957338, 59

**Non - Fraudulent:** 7, -0.11319, -0.27153, 0.370145, -0.41043, -0.11045, 0.074355, -0.21008, -0.49977, 0.118765, 0.570328, 0.052736, -0.07343, 1.011592, 0.011747, 0.142404, 93.2
