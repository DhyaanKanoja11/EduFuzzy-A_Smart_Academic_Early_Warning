import numpy as np
from skfuzzy import control as ctrl

class FuzzyVariables:
    def get_variables(self):
        # Inputs
        attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
        internal_marks = ctrl.Antecedent(np.arange(0, 51, 1), 'internal_marks')
        
        # Output
        risk_level = ctrl.Consequent(np.arange(0, 101, 1), 'risk_level')

        # Membership Functions
        attendance.automf(3, names=['low', 'medium', 'high'])
        internal_marks.automf(3, names=['poor', 'average', 'good'])
        risk_level.automf(3, names=['safe', 'monitor', 'critical'])

        return attendance, internal_marks, risk_level
