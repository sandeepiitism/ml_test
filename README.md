## End-to-End Machine Learning Application and Azure Deployment
### Overview
This repository contains a proof-of-concept (PoC) for a machine learning (ML) application that follows best practices for modular coding and MLOps (Machine Learning Operations). The application is designed to seamlessly transition from development to deployment on the Azure cloud platform.

### Directory Structure
The project is organized into the following directories:

Notebook/data: Contains datasets used for training and testing the machine learning model.

src: Inside components folders --> Consists of modularized source code, with separate modules for data ingestion, data transformation, and model training.

Inside Pipeline: Stores the predict-pipeline and train-pipeline.

Utils: Includes utility scripts for tasks such as data download, model training, and evaluation.

notebooks: Contains Jupyter notebooks for exploratory data analysis and model prototyping.

deploy: Houses the necessary files for deploying the model on Azure.

config: Configuration files for model parameters and Azure deployment settings.

Requirements
Ensure you have the following dependencies installed:

bash
Copy code
pip install -r requirements.txt
Usage
Data Preparation: Run data preprocessing scripts to clean and prepare the datasets.

bash
Copy code
python src/data_ingestionpy
Model Training: Train the machine learning model using the following script.

bash
Copy code
python src/train_model.py
Model Evaluation: Evaluate the trained model's performance.

bash
Copy code
python src/app.py
Webpage: checking the predicted output at flask application.



References
For more details on modular coding and MLOps with Azure, refer to the following resources:

Microsoft Machine Learning Documentation

Modular Programming in Python

License
This project is licensed under the MIT License - see the LICENSE file for details.
