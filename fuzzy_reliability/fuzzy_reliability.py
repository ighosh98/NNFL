#Python Code for Reliability Improvement Index Calculation
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

noise = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'noise')
leak = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'leak')
service = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'service')

rii = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'rii')

noise.automf(3)
leak.automf(3)
service.automf(3)

noise['neg'] = fuzz.trimf(noise.universe, [0, 0, 0.2])
noise['vlow'] = fuzz.trimf(noise.universe, [0, 0.2, 0.4])
noise['low'] = fuzz.trimf(noise.universe, [0.2, 0.4, 0.6])
noise['mod'] = fuzz.trimf(noise.universe, [0.4, 0.6, 0.8])
noise['high'] = fuzz.trimf(noise.universe, [0.6, 0.8, 1.0])
noise['vhigh'] = fuzz.trimf(noise.universe, [0.8, 0.8, 1.0])

leak['neg'] = fuzz.trimf(leak.universe, [0, 0, 0.2])
leak['vlow'] = fuzz.trimf(leak.universe, [0, 0.2, 0.4])
leak['low'] = fuzz.trimf(leak.universe, [0.2, 0.4, 0.6])
leak['mod'] = fuzz.trimf(leak.universe, [0.4, 0.6, 0.8])
leak['high'] = fuzz.trimf(leak.universe, [0.6, 0.8, 1.0])
leak['vhigh'] = fuzz.trimf(leak.universe, [0.8, 0.8, 1.0])

service['neg'] = fuzz.trimf(service.universe, [0, 0, 0.2])
service['vlow'] = fuzz.trimf(service.universe, [0, 0.2, 0.4])
service['low'] = fuzz.trimf(service.universe, [0.2, 0.4, 0.6])
service['mod'] = fuzz.trimf(service.universe, [0.4, 0.6, 0.8])
service['high'] = fuzz.trimf(service.universe, [0.6, 0.8, 1.0])
service['vhigh'] = fuzz.trimf(service.universe, [0.8, 0.8, 1.0])

rii['neg'] = fuzz.trimf(rii.universe, [0, 0, 0.2])
rii['vlow'] = fuzz.trimf(rii.universe, [0, 0.2, 0.4])
rii['low'] = fuzz.trimf(rii.universe, [0.2, 0.4, 0.6])
rii['mod'] = fuzz.trimf(rii.universe, [0.4, 0.6, 0.8])
rii['high'] = fuzz.trimf(rii.universe, [0.6, 0.8, 1.0])
rii['vhigh'] = fuzz.trimf(rii.universe, [0.8, 0.8, 1.0])

rule1 = ctrl.Rule(noise['mod'] & leak['low'] & service['vlow'], rii['low'])
rule2 = ctrl.Rule(noise['mod'] & leak['low'] & service['low'], rii['low'])
rule3 = ctrl.Rule(noise['mod'] & leak['mod'] & service['vlow'], rii['low'])
rule4 = ctrl.Rule(noise['mod'] & leak['mod'] & service['low'], rii['mod'])
rule5 = ctrl.Rule(noise['high'] & leak['low'] & service['vlow'], rii['low'])
rule6 = ctrl.Rule(noise['high'] & leak['low'] & service['vlow'], rii['mod'])
rule7 = ctrl.Rule(noise['high'] & leak['mod'] & service['vlow'], rii['mod'])
rule8 = ctrl.Rule(noise['high'] & leak['mod'] & service['vlow'], rii['mod'])

rule1.view()
rule2.view()
rule3.view()
rule4.view()
rule5.view()
rule6.view()
rule7.view()
rule8.view()

rii_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
rii_val = ctrl.ControlSystemSimulation(rii_ctrl)

rii_val.input['noise'] = 0.65
rii_val.input['leak'] = 0.50
rii_val.input['service'] = 0.35

rii_val.compute()

print(rii_val.output['rii'])
rii.view(sim=rii_val)



