import pandas as pd
import numpy as np
import pickle
import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class AudioModel:
    """Lead: Sunday Boniface - Phase 1: Audio Model Development"""
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.model = SVC(kernel='rbf', C=1.0, random_state=42) # Specified in brief [cite: 134]
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.df = None

    def preprocess(self):
        """Preprocess audio_features.csv as per Phase 1 requirements [cite: 79-101]"""
        # Load the dataset
        self.df = pd.read_csv(self.data_path)
        
        # 1. Categorical Encoding for Target [cite: 81-86]
        # Mapping: Low=0, Medium=1, High=2
        target_map = {'Low': 0, 'Medium': 1, 'High': 2}
        self.df['performance_rating'] = self.df['performance_rating'].map(target_map)
        
        # 2. Feature Engineering 
        # clarity_to_speed_ratio = speech_clarity_score / speaking_speed * 100
        self.df['clarity_to_speed_ratio'] = (self.df['speech_clarity_score'] / 
                                            self.df['speaking_speed']) * 100
        
        # 3. Drop employee_id [cite: 94]
        features = self.df.drop(columns=['employee_id', 'performance_rating'])
        target = self.df['performance_rating']
        
        return features, target

    def train(self, X_train, y_train):
        """Train the SVC model after scaling [cite: 133-135]"""
        start_time = time.time()
        
        # Scaling must be fit only on X_train to avoid data leakage 
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        print("Training Audio Features Performance Predictor (SVC)...")
        self.model.fit(X_train_scaled, y_train)
        
        end_time = time.time()
        print(f"Training completed in {end_time - start_time:.4f} seconds.")

    def predict(self, X):
        """Generate predictions using the trained model [cite: 136]"""
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def evaluate(self, X, y):
        """Calculate and report performance metrics [cite: 143-151]"""
        y_pred = self.predict(X)
        
        print("\n--- Audio Model Evaluation ---")
        print(f"Accuracy Score: {accuracy_score(y, y_pred):.4f}")
        print("\nClassification Report:")
        print(classification_report(y, y_pred, target_names=['Low', 'Medium', 'High']))
        
        # Generate Confusion Matrix for visualization later [cite: 147]
        cm = confusion_matrix(y, y_pred)
        return cm

    def save_model(self, file_path='audio_model.pkl'):
        """Save the trained model and scaler as a pickle file [cite: 161]"""
        with open(file_path, 'wb') as f:
            pickle.dump({'model': self.model, 'scaler': self.scaler}, f)
        print(f"Model saved to {file_path}")

# Example Usage for Phase 1
if __name__ == "__main__":
    audio_expert = AudioModel('audio_features.csv')
    X, y = audio_expert.preprocess()

    # Synchronized Split: 80-20 ratio, random_state 42 [cite: 110-113]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    audio_expert.train(X_train, y_train)
    audio_expert.evaluate(X_test, y_test)
    audio_expert.save_model()