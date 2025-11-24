import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

class GradePredictor:
    def __init__(self):
        self.model = LinearRegression()

    def train_and_predict(self, current_marks):
        # Dummy training data: [Internal Marks] -> [Final Exam Score]
        # We assume internal marks (out of 50) correlate to final marks (out of 100)
        X_train = np.array([[20], [25], [30], [35], [40], [45], [50]])
        y_train = np.array([[40], [50], [60], [70], [80], [90], [100]])
        
        self.model.fit(X_train, y_train)
        
        # Predict based on actual student marks
        # Reshape data because sklearn expects 2D array
        X_input = np.array(current_marks).reshape(-1, 1)
        predictions = self.model.predict(X_input)
        return predictions.flatten()

class StudentClusterer:
    def __init__(self, n_clusters=3):
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    def group_students(self, data_matrix):
        # Clusters students based on Attendance and Internal Marks
        labels = self.kmeans.fit_predict(data_matrix)
        return labels
