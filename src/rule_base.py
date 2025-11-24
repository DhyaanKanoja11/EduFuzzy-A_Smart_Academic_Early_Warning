from skfuzzy import control as ctrl

class RuleBase:
    def get_rules(self, attendance, internal_marks, risk_level):
        rule1 = ctrl.Rule(attendance['low'] | internal_marks['poor'], risk_level['critical'])
        rule2 = ctrl.Rule(attendance['medium'] & internal_marks['average'], risk_level['monitor'])
        rule3 = ctrl.Rule(attendance['high'] | internal_marks['good'], risk_level['safe'])
        rule4 = ctrl.Rule(attendance['medium'] & internal_marks['poor'], risk_level['critical'])
        
        return [rule1, rule2, rule3, rule4]
