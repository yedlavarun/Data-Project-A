import numpy as np
import math
import Degrees
import itertools
import matplotlib.pyplot as plt

#The first or anything that has the number #1 for example Picture1 is for the image F110W

#Here We need to the pixel angular size of the image

θ = None
Δx = None
Δy = None
a = None
δ_ = None
Δα = None
sin = None
cos = None
Δδ = None



Picture1 = {'RAs': ['10:38:40.9310', '10:38:45.3169', '10:38:47.6715', '10:38:42.7365'],
            'Decs': ['48:49:35.241', '48:49:15.346', '48:48:56.741', '48:48:41.323'],
            'Xs': [3785.1514, 2343.1855, 1569.2226, 3193.7719],
            'Ys': [5416.1669, 4751.6511, 4130.6542, 3616.921],
            "a": [],
            "θ": []}

Picture2 = {'RAs': ['10:38:40.9377', '10:38:45.3146', '10:38:47.6683', '10:38:42.7333'],
            'Decs': ['48:49:35.244', '48:49:15.350', '48:48:56.699', '48:48:41.306'],
            'Xs': [406.61567, 1959.0388, 2852.8247, 1381.8851],
            'Ys': [822.5355, 1149.7437, 1584.0845, 2445.1244],
            "a": [],
            "θ": []}



# Δα*math.cos(δ_) = a*((-(Δx)*cos)-((Δy)*sin))

# sin = -(Δα*math.cos(δ_)/a + (Δx)*cos)/Δy

# cos = -(Δα*math.cos(δ_)/a + (Δy)*sin)/Δx

# Δδ = a*((-(Δx)*sin)+((Δy)*cos))

# sin = (Δy*cos - Δδ/a)/Δx

# cos = (Δx*sin + Δδ/a)/Δy



# (Δy*cos - Δδ/a)*Δy/Δx = -(Δα*math.cos(δ_)/a + (Δx)*cos)

# (Δy**2)*cos - Δy*Δδ/a = -(Δx*Δα*math.cos(δ_)/a + (Δx**2)*cos)

# a*cos = (Δy*Δδ - Δx*Δα*math.cos(δ_))/(Δy**2 + Δx**2)

# Acos = (Δy*Δδ - Δx*Δα*math.cos(δ_))/(Δy**2 + Δx**2)


# (Δx*sin + Δδ/a)*Δx/Δy = -(Δα*math.cos(δ_)/a + (Δy)*sin)

# (Δx**2)*sin + Δx*Δδ/a = -(Δy*Δα*math.cos(δ_)/a + (Δy**2)*sin)

# a*sin = (-Δx*Δδ + Δy*Δα*math.cos(δ_))/(Δy**2 + Δx**2)

# Asin = (-Δx*Δδ - Δy*Δα*math.cos(δ_))/(Δy**2 + Δx**2)


def ΔValues(X_1, Y_1, RA_1, Dec_1, X_2, Y_2, RA_2, Dec_2):
    Δx = X_2 - X_1
    Δy = Y_2 - Y_1
    Δα = math.radians(Degrees.RAtoDegrees(RA_2) - Degrees.RAtoDegrees(RA_1))
    δ_ =  math.radians(Degrees.DecToDegrees(Dec_1))
    Δδ = math.radians(Degrees.DecToDegrees(Dec_2) - Degrees.DecToDegrees(Dec_1))
    return Δx, Δy, Δα, δ_, Δδ

def solvefora(X_1, Y_1, RA_1, Dec_1, X_2, Y_2, RA_2, Dec_2):
    Δx, Δy, Δα, δ_, Δδ = ΔValues(X_1, Y_1, RA_1, Dec_1, X_2, Y_2, RA_2, Dec_2)
    Acos = (((Δy*Δδ) - (Δx*Δα*math.cos(δ_)))/(Δy**2 + Δx**2))
    Asin = (((-Δx*Δδ) - (Δy*Δα*math.cos(δ_)))/(Δy**2 + Δx**2))
    a = math.sqrt(Acos**2 + Asin**2)
    θ = (math.atan2(Asin,Acos))
    return(a, θ)


# solvefora(2343.1855, 4751.6511, '10:38:45.3169', '48:49:15.346', 3785.1659, 5416.1818, '10:38:40.9310', '48:49:35.241')

# solvefora(2343.1855, 4751.6511, '10:38:45.3169', '48:49:15.346', 1569.2226, 4130.6542, '10:38:47.6715', '48:48:56.741')


for i in range(4):
    for j in range(4):
        if i != j:
            a, θ =   solvefora(Picture1['Xs'][i], Picture1['Ys'][i], Picture1['RAs'][i],
                      Picture1['Decs'][i], Picture1['Xs'][j], Picture1['Ys'][j],
                      Picture1['RAs'][j], Picture1['Decs'][j])
            Picture1['a'].append(a)
            Picture1['θ'].append(θ)



a1 = np.mean(Picture1['a'])
ea1 = np.std(Picture1['a'])
θ1 = np.mean(Picture1["θ"])
eθ1 = np.std(Picture1['θ'])


for i in range(4):
    for j in range(4):
        if i != j:
            a, θ =   solvefora(Picture2['Xs'][i], Picture2['Ys'][i], Picture2['RAs'][i],
                      Picture2['Decs'][i], Picture2['Xs'][j], Picture2['Ys'][j],
                      Picture2['RAs'][j], Picture2['Decs'][j])
            Picture2['a'].append(a)
            Picture2['θ'].append(θ)

a2 = np.mean(Picture2['a'])
ea2 = np.std(Picture2['a'])
θ2 = np.mean(Picture2["θ"])
eθ2 = np.std(Picture2['θ'])


    

# plt.plot(Picture1['a'], marker="o", linestyle="", label="all a's")
# plt.axhline(y=a1, color='r', linestyle="--", label="Mean")
# plt.xlabel("Number of Combinations for fit F101W")
# plt.axhline(a1 + ea1, color='green', linestyle=':', label=f'Errors')
# plt.axhline(a1 - ea1, color='green', linestyle=':')
# plt.ylabel("Scaling Values for fit F101W(a)")
# plt.text(
#     (2),
#     a1,
#     f"Mean = {a1:.10f}",
#     va= 'bottom',
#     ha='right'
# )
# plt.legend()
# plt.show()

# plt.plot(Picture1['θ'], marker="x", linestyle="", label="all 'θs", color="b")
# plt.axhline(y=θ1 , color='r', linestyle="--", label="Mean")
# plt.axhline(θ1 + eθ1, color='green', linestyle=':', label=f'Errors')
# plt.axhline(θ1 - eθ1, color='green', linestyle=':')
# plt.xlabel("Number of Combinations for fit F101W")
# plt.ylabel("Rotation Values for fit F101W(a)")
# plt.text(
#     (2),
#     θ1,
#     f"Mean = {θ1:.10f}",
#     va= 'bottom',
#     ha='right'
# )
# plt.legend(loc='upper right')
# plt.show()


# plt.plot(Picture2['a'], marker="o", linestyle="", label="all a's")
# plt.axhline(y=a2, color='r', linestyle="--", label="Mean")
# plt.xlabel("Number of Combinations for fit F101W")
# plt.axhline(a2 + ea2, color='green', linestyle=':', label=f'Errors')
# plt.axhline(a2 - ea2, color='green', linestyle=':')
# plt.ylabel("Scaling Values for fit F101W(a)")
# plt.text(
#     (2),
#     a2,
#     f"Mean = {a2:.10f}",
#     va= 'bottom',
#     ha='right'
# )
# plt.legend()
# plt.show()

# plt.plot(Picture2['θ'], marker="x", linestyle="", label="all 'θs", color="b")
# plt.axhline(y=θ2 , color='r', linestyle="--", label="Mean")
# plt.axhline(θ2 + eθ2, color='green', linestyle=':', label=f'Errors')
# plt.axhline(θ2 - eθ2, color='green', linestyle=':')
# plt.xlabel("Number of Combinations for fit F606W")
# plt.ylabel("Rotation Values for fit F606W(a)")
# plt.text(
#     (2),
#     θ2,
#     f"Mean = {θ2:.10f}",
#     va= 'bottom',
#     ha='right'
# )
# plt.legend(loc='upper right')
# plt.show()

# print(a2,2(θ2))

print(ea1, eθ1, ea2, eθ2)

