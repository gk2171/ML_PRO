import sys
import traceback
from src.logger import logging

# Function to extract detailed error information
def error_message_detail(error, error_detail: sys):
    try:
        # Capture the traceback of the original exception
        _, _, exc_tb = error_detail.exc_info()
        
        # If traceback is available, extract file name and line number
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            error_message = f"Error occurred in python script name [{file_name}] at line number [{exc_tb.tb_lineno}] with error message [{str(error)}]"
        else:
            error_message = f"Error occurred: {str(error)}"
    
    except Exception as inner_error:
        # If traceback extraction fails, return a simple message
        error_message = f"Error occurred while processing the error: {str(inner_error)}"
    
    return error_message

# CustomException class that formats and stores error details
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Test block to raise a custom exception
if __name__ == "__main__":
    try:
        # Your dataset column check logic
        train_df_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 
                            'test_preparation_course', 'math_score', 'reading_score', 'writing_score']
        
        # Check if 'target' column exists
        if 'target' not in train_df_columns:
            raise CustomException(f"Target column is missing in the dataset. Columns found: {train_df_columns}", sys)
        
    except CustomException as e:
        logging.error(str(e))  # Log the error message
        print(str(e))  # Print the error message to the console
