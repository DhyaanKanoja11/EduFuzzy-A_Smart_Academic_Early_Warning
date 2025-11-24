from src.data_manager import StudentDataManager
from src.fuzzy_variables import FuzzyVariables
from src.rule_base import RuleBase
from src.inference_engine import InferenceEngine
from src.visualizer import Visualizer
from src.ai_features import GradePredictor, StudentClusterer 

def main():
    # Initialize Modules
    data_mgr = StudentDataManager('data/students.csv')
    fuzzy_vars = FuzzyVariables()
    rules = RuleBase()
    engine = InferenceEngine(fuzzy_vars, rules)
    viz = Visualizer()
    
    # Initialize New AI Modules
    predictor = GradePredictor()
    clusterer = StudentClusterer()

    # Load Data
    print("Loading Data...")
    df = data_mgr.load_data()
    print("Data Loaded Successfully.")

    # 1. Fuzzy Logic: Calculate Risk
    print("Calculating Fuzzy Risk Scores...")
    risk_scores = []
    for index, row in df.iterrows():
        score = engine.calculate_risk(row['Attendance'], row['InternalMarks'])
        risk_scores.append(round(score, 2))
    df['Fuzzy_Risk_Score'] = risk_scores
    
    # 2. Supervised AI: Predict Final Exam Score
    print("Running Linear Regression Prediction...")
    predicted_finals = predictor.train_and_predict(df['InternalMarks'].values)
    df['Predicted_Final_Score'] = [round(x, 2) for x in predicted_finals]

    # 3. Unsupervised AI: Group Students (Clustering)
    print("Running K-Means Clustering...")
    # We use Attendance and InternalMarks to group similar students
    data_matrix = df[['Attendance', 'InternalMarks']].values
    df['Cluster_Group'] = clusterer.group_students(data_matrix)

    # Determine Risk Category for Report
    df['Status'] = df['Fuzzy_Risk_Score'].apply(lambda x: 'Critical' if x > 60 else ('Monitor' if x > 30 else 'Safe'))

    # Output Results
    print("\nFinal Analysis (Fuzzy + Regression + Clustering):")
    # Display relevant columns
    print(df[['Name', 'Attendance', 'Fuzzy_Risk_Score', 'Predicted_Final_Score', 'Cluster_Group', 'Status']])
    
    data_mgr.save_results(df, 'data/student_risk_report.csv')

    # Visualize
    viz.plot_risk_distribution(df)

if __name__ == "__main__":
    main()
