import pandas as pd
import os 
import sys 
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngetionConfig:
    train_data_path = str=os.path.join('artifacts',"train.csv")
    test_data_path = str=os.path.join('artifacts',"test.csv")
    raw_data_path = str=os.path.join('artifacts',"data.csv")

class DataIngetion:
    def __init__(self):
        self.ingetionconfig = DataIngetionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enteredd data ingestion component")
        try :
            df = pd.read_csv("notebook\\data\\stud.csv")
            logging.info("read data as datafram")

            os.makedirs(os.path.dirname(self.ingetionconfig.train_data_path), exist_ok=True)

            df.to_csv(self.ingetionconfig.raw_data_path,index=False,header=True)

            logging.info("Train Test split instiated")

            train_set,test_set =  train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingetionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingetionconfig.test_data_path,index=False,header=True)

            logging.info("Data infestion completed")

            return (
                self.ingetionconfig.train_data_path,
                self.ingetionconfig.test_data_path
            )
        
        except Exception as e :
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngetion()
    train_data,test_data = obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)