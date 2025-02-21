from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self):
        # Initialization logic for the model trainer
        self.model = RandomForestClassifier()  # Example model, you can choose another model

    def initiate_model_trainer(self, train_data, test_data):
        # Split the data into features and labels (assuming your data is ready)
        X_train, y_train = train_data.drop('target', axis=1), train_data['target']
        X_test, y_test = test_data.drop('target', axis=1), test_data['target']

        # Train the model
        self.model.fit(X_train, y_train)

        # Predict on test data
        y_pred = self.model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model accuracy: {accuracy * 100:.2f}%")
        
        return 
    
class ModelTrainerConfig:
    def __init__(self):
        self.model_save_path = 'artifacts/model.pkl'  # Example: Save path for the trained model
        self.random_state = 42  # Example: Random state for reproducibility

