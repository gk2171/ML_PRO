import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation  # Removed DataTransformationConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

        # ✅ Ensure the `artifacts` directory exists
        os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

    def initiate_data_ingestion(self):
        """Reads dataset, splits it, and saves train/test sets."""
        logging.info("Entered the data ingestion method or component")
        try:
            dataset_path = os.path.join('notebook', 'data', 'stud.csv')
            if not os.path.exists(dataset_path):
                raise FileNotFoundError(f"Dataset file not found at {dataset_path}")

            df = pd.read_csv(dataset_path)
            logging.info(f"Successfully read dataset: {dataset_path} with shape {df.shape}")

            # ✅ Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            # ✅ Train-test split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # ✅ Save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion process completed successfully")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        obj = DataIngestion()
        train_data, test_data = obj.initiate_data_ingestion()

        # Read train and test data into DataFrames
        train_df = pd.read_csv(train_data)  # Read train data into DataFrame
        test_df = pd.read_csv(test_data)    # Read test data into DataFrame

        # Debugging: Check if 'target' column exists in the dataset
        print("Columns in train data:", train_df.columns)  # Check column names in train data

        if 'target' not in train_df.columns:
            raise CustomException(f"Target column is missing in the dataset. Columns found: {train_df.columns}", sys)

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_df, test_df)

        # Model Training
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise CustomException(e, sys)
