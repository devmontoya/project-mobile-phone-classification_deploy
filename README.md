# Mobile phone classification deploy Project

This project uses streamlit and gcloud to deploy a web application that seeks to predict the price range of mobiles from a dataset.
For this purpose, an exploratory analysis, a search for a suitable model and finally a prediction and preprocessing pipeline were performed.

## Initial problem and dataset

> Create a web application using Streamlit, deployed on Google Cloud, which utilizes a previously built pipeline to make predictions. Perform Exploratory Data Analysis (EDA) and identify a suitable machine learning model for this purpose.

### Dataset:
https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification/data

## Web application link:

https://servicio-stmlit-mobileprange-dm-wuytbudssq-uc.a.run.app/

## How to use it, key notations

- Create a virtual environment using venv or conda.
- Install the packages from requirements.txt `pip install -r requirements.txt`.
- **data_mobile_price_range.csv** is the input data.
- The files found in **Datasets** are training and testing datasets without any preprocessing; they were simply gotten from input data by sklearn splitting.
- The files found in **Datasets_processed** were preprocessed in EDA.ipynb.
- If you want to do a test on the final streamlit web application, use `Datasets/xtest.csv`.


## Commands used to deploy on gcloud

- `gcloud artifacts repositories create <repo-name> --repository-format docker --project <project-name> --location us-central1`
- `gcloud builds submit --config=cloudbuild.yaml --project <project-name>`
- `gcloud run services replace service.yaml --region us-central1 --project <project-name>`
- `gcloud run services set-iam-policy <service> gcr-service-policy.yaml --region us-central1 --project <project-name>`
