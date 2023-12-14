import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,
        gender: str,
        regions: str,
        education_level,
        lncome: str,
        health_issue: str,
        earlier_sales: int,
        quantity_sold: int):

        self.gender = gender

        self.regions = regions

        self.education_level = education_level

        self.lncome = lncome

        self.health_issue = health_issue

        self.earlier_sales = earlier_sales

        self.quantity_sold = quantity_sold

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "regions": [self.regions],
                "education_level": [self.education_level],
                "lncome": [self.lncome],
                "health_issue": [self.health_issue],
                "earlier_sales(k)": [self.earlier_sales],
                "quantity_sold": [self.quantity_sold],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)