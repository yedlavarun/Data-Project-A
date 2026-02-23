import matplotlib.pyplot as plt
import matplotlib.patches as patches

Pixels1 = {"X": 3502, "Y": 2802}
Pixels2 = {"X": 3301, 'Y': 2501}

a_size = 1.4541 * 10**(-7)





Area1 = (Pixels1['X']*a_size) * (Pixels1['Y']*a_size)
Area2 = (Pixels2['X']*a_size) * (Pixels2['Y']*a_size)

print(Area1, Area2)