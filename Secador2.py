from dataclasses import dataclass
@dataclass
class ParametrosSecagem:
   """
   X = Umidade livre do Material (kg de água / kg de sólido seco)
   Xe = Umidade de equilíbrio
   K = Constante de Primeira Ordem (1/h)
   T  = Temperatura (ºC)

   """
   Xe: float=0.05
   T : float= 50.0

def func_secagem(T):
  K = 0.2*(1 + 0.02*(T - 60))
  return K

def modelo_secagem(t,X,params):
  T=params.T
  Xe=params.Xe
  dXdt = -func_secagem(T) * (X - Xe)
  return dXdt

import numpy as np
from scipy.integrate import solve_ivp
def simula_secagem(tempo, params):
  t_span = [0, tempo]
  Cond_inicial = [0.5]
  t_eval = np.linspace(0, tempo, 100)
  modelo_mod = lambda t, T: modelo_secagem(t, T, params) # Slide 123, aqui criou uma nova função modelo que usou a função lambda que fala pro solve ivp que tem 2 variais so para utilizar e usa params
  sol = solve_ivp(modelo_mod, t_span, Cond_inicial, t_eval=t_eval, method='RK45')
  return sol.t, sol.y[0]

