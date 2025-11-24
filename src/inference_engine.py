from skfuzzy import control as ctrl

class InferenceEngine:
    def __init__(self, variables_obj, rules_obj):
        self.attendance, self.marks, self.risk = variables_obj.get_variables()
        self.rules = rules_obj.get_rules(self.attendance, self.marks, self.risk)
        
        self.system = ctrl.ControlSystem(self.rules)
        self.simulation = ctrl.ControlSystemSimulation(self.system)

    def calculate_risk(self, att_val, mark_val):
        self.simulation.input['attendance'] = att_val
        self.simulation.input['internal_marks'] = mark_val
        self.simulation.compute()
        return self.simulation.output['risk_level']
