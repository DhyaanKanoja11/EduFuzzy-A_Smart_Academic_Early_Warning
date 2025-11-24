import pandas as pd

class StudentDataManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.filepath)
        return self.data

    def save_results(self, results_df, output_path):
        results_df.to_csv(output_path, index=False)
        print(f"Results saved to {output_path}")
