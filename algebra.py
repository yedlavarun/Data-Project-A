import sympy as sp

Δα, Δδ, a = sp.symbols('Δα Δδ a')
Δx, Δy = sp.symbols('Δx Δy')
θ = sp.symbols('θ')
δ = sp.symbols('δ')

Eq1 = sp.Eq((-(Δx*a*sp.cos(θ) + Δy*a*sp.sin(θ))/sp.cos(δ)), Δα)
Eq2 = sp.Eq(-(Δx*a*sp.sin(θ) - Δy*a*sp.cos(θ)), Δδ)

# sin = -(Δα*math.cos(δ_)/a + (Δx)*cos)/Δy

# cos = -(Δα*math.cos(δ_)/a + (Δy)*sin)/Δx

# sin = (Δy*cos - Δδ/a)/Δx

# cos = (Δx*sin + Δδ/a)/Δy

Eq3 = sp.Eq((-(Δα*sp.cos(δ)/a) + (Δx)*sp.cos(θ))/Δy, sp.sin(θ))

Eq4 = sp.Eq(((Δy*sp.cos(θ) - Δδ/a)/Δx), sp.sin(θ))

solution = sp.solve((Eq1, Eq2, Eq3, Eq4),(θ, a))
print(solution)
