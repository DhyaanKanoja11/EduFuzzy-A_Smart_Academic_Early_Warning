import matplotlib.pyplot as plt

class Visualizer:
    def plot_risk_distribution(self, df):
        plt.figure(figsize=(8, 5))
        
        # CHANGED 'RiskScore' TO 'Fuzzy_Risk_Score'
        plt.bar(df['Name'], df['Fuzzy_Risk_Score'], color='salmon')
        
        plt.xlabel('Students')
        plt.ylabel('Risk Score (0-100)')
        plt.title('Student Academic Risk Analysis')
        plt.axhline(y=70, color='r', linestyle='--', label='Critical Threshold')
        plt.legend()
        plt.savefig('risk_analysis_chart.png')
        plt.show()
