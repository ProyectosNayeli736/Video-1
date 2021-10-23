Expansión en Series de Fourier

from IPython.display import Image
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import scipy as sp
import sympy as sym

%matplotlib inline

1. Función convencional
Declaramos las variables simbólicas n y t
n = sym.Symbol('n')
t = sym.Symbol('t')
Definimos la función peridódica
Tmin = 0
Tmax = 2*np.pi
​
T=Tmax-Tmin
w = 2*np.pi/T
​
# ft es una función simbólica
ft=t
Calculamos los coeficientes de Fourier
# Calculamos la integral para a0
f_integral = ft
a0 = (2/T)*sym.integrate(f_integral,(t,Tmin,Tmax))
print("a0 = ")
sym.pprint(a0)
​
# Calculamos la integral para an
f_integral = ft*sym.cos(n*w*t)
an = (2/T)*sym.integrate(f_integral,(t,Tmin,Tmax))
an = sym.simplify(an)
print("an = ")
sym.pprint(an)
​
# Calculamos la integral para bn
f_integral = ft*sym.sin(n*w*t)
bn = (2/T)*sym.integrate(f_integral,(t,Tmin,Tmax))
print("bn = ")
bn = sym.simplify(bn)
sym.pprint(bn)
​
a0 = 
6.28318530717959
an = 
⎧2.0⋅n⋅sin(6.28318530717959⋅n) + 0.318309886183791⋅cos(6.28318530717959⋅n) - 0
⎪─────────────────────────────────────────────────────────────────────────────
⎪                                               2                             
⎨                                              n                              
⎪                                                                             
⎪                                      6.28318530717959                       
⎩                                                                             

.318309886183791                            
────────────────  for n > -∞ ∧ n < ∞ ∧ n ≠ 0
                                            
                                            
                                            
                          otherwise         
                                            
bn = 
⎧-2.0⋅n⋅cos(6.28318530717959⋅n) + 0.318309886183791⋅sin(6.28318530717959⋅n)   
⎪──────────────────────────────────────────────────────────────────────────  f
⎪                                     2                                       
⎨                                    n                                        
⎪                                                                             
⎪                                    0                                        
⎩                                                                             

                         
or n > -∞ ∧ n < ∞ ∧ n ≠ 0
                         
                         
                         
       otherwise         
                         
Usando los coeficientes representamos la expansión en Series de Fourier
# Definimos el número de armónicos para la expansión
serie = 0
Armonicos = 3
​
for i in range(1,Armonicos+1):
    
    # Evaluamos los coeficientes para cada armónico
    an_c = an.subs(n,i)
    bn_c = bn.subs(n,i)
    
    if abs(an_c) < 0.0001: an_c = 0
    if abs(bn_c) < 0.0001: bn_c = 0
        
    serie= serie + an_c*sym.cos(i*w*t) # Términos coseno de la serie
    serie = serie + bn_c*sym.sin(i*w*t) # Términos seno de la serie
​
serie = a0/2+serie  # Expansión final de la serie
​
print('f(t)= ')
sym.pprint(serie)
f(t)= 
-2.0⋅sin(1.0⋅t) - 1.0⋅sin(2.0⋅t) - 0.666666666666667⋅sin(3.0⋅t) + 3.1415926535
8979
Graficamos la función periódica original y su expansión en Series de Fourier
# Convertimos la expresión Sympy a una función evaluable
fserie = sym.lambdify(t,serie)
f = sym.lambdify(t,ft)
​
# Creamos un vector de tiempo para la gráfica
v_tiempo = np.linspace(Tmin,Tmax,200)
​
# Evaluamos las funciones
fserieG = fserie(v_tiempo)
fG = f(v_tiempo)
 
plt.plot(v_tiempo,fG,label = 'f(t)')
plt.plot(v_tiempo,fserieG,label = 'Expansión')
​
plt.xlabel('tiempo')
plt.legend()
plt.title('Expansión en Series de Fourier')
plt.show()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-25-3c1e69b79206> in <module>
      1 # Convertimos la expresión Sympy a una función evaluable
----> 2 fserie = sym.lambdify(t,serie)
      3 f = sym.lambdify(t,ft)
      4 
      5 # Creamos un vector de tiempo para la gráfica

NameError: name 't' is not defined

2. Función por tramos
Declaramos las variables simbólicas n y t
n = sym.Symbol('n')
t=sym.Symbol('t')
Definimos la función peridódica por tramos
Tmin = -2
Tmax = 2
​
T=Tmax-Tmin
w = 2*np.pi/T
​
f1=-1
f2=1
​
# ft es una función simbólica por tramos
ft = sym.Piecewise((f1, ((t <= -1) & (t >= -2))), (f2, ((t > -1) & (t <= 2))))
ft
{−11for𝑡≥−2∧𝑡≤−1for𝑡≤2∧𝑡>−1
Calculamos los coeficientes de Fourie
# Calculamos la integral para a0
f_integral = ft
a0 = (2/T)*sym.integrate(f_integral,(t,Tmin,Tmax))
print("a0 = ")
sym.pprint(a0)
​
# Calculamos la integral para an
f_integral = ft*sym.cos(n*w*t)
an = (2/T)*sym.integrate(f_integral,(t,Tmin,Tmax))
an = sym.simplify(an)
print("an = ")
sym.pprint(an)
​
# Calculamos la integral para bn
f_integral = ft*sym.sin(n*w*t)
bn = (2/T)*sym.integrate(f_integral,(t,Tmin,Tmax))
print("bn = ")
bn = sym.simplify(bn)
sym.pprint(bn)
a0 = 
1.00000000000000
an = 
⎧0.636619772367581⋅sin(1.5707963267949⋅n)                            
⎪────────────────────────────────────────  for n > -∞ ∧ n < ∞ ∧ n ≠ 0
⎨                   n                                                
⎪                                                                    
⎩                  1.0                             otherwise         
bn = 
⎧0.636619772367581⋅(cos(1.5707963267949⋅n) - cos(3.14159265358979⋅n))         
⎪────────────────────────────────────────────────────────────────────  for n >
⎨                                 n                                           
⎪                                                                             
⎩                                 0                                           

                   
 -∞ ∧ n < ∞ ∧ n ≠ 0
                   
                   
 otherwise         
Usando los coeficientes representamos la expansión en Series de Fourier
# Definimos el número de armónicos para la expansión
serie = 0
Armonicos = 30
​
for i in range(1,Armonicos+1):
    
    # Evaluamos los coeficientes para cada armónico
    an_c = an.subs(n,i)
    bn_c = bn.subs(n,i)
    
    if abs(an_c) < 0.0001: an_c = 0
    if abs(bn_c) < 0.0001: bn_c = 0
        
    serie= serie + an_c*sym.cos(i*w*t) # Términos coseno de la serie
    serie = serie + bn_c*sym.sin(i*w*t) # Términos seno de la serie
​
serie = a0/2+serie  # Expansión final de la serie
​
print('f(t)= ')
sym.pprint(serie)
f(t)= 
0.636619772367581⋅sin(1.5707963267949⋅t) - 0.636619772367581⋅sin(3.14159265358
979⋅t) + 0.212206590789194⋅sin(4.71238898038469⋅t) + 0.127323954473516⋅sin(7.8
5398163397448⋅t) - 0.212206590789194⋅sin(9.42477796076938⋅t) + 0.0909456817667
973⋅sin(10.9955742875643⋅t) + 0.0707355302630646⋅sin(14.1371669411541⋅t) - 0.1
27323954473516⋅sin(15.707963267949⋅t) + 0.0578745247606891⋅sin(17.278759594743
9⋅t) + 0.0489707517205831⋅sin(20.4203522483337⋅t) - 0.0909456817667973⋅sin(21.
9911485751286⋅t) + 0.0424413181578387⋅sin(23.5619449019234⋅t) + 0.037448221903
9753⋅sin(26.7035375555132⋅t) - 0.0707355302630646⋅sin(28.2743338823081⋅t) + 0.
03350630380882⋅sin(29.845130209103⋅t) + 0.0303152272555991⋅sin(32.986722862692
8⋅t) - 0.0578745247606892⋅sin(34.5575191894877⋅t) + 0.0276791205377208⋅sin(36.
1283155162826⋅t) + 0.0254647908947033⋅sin(39.2699081698724⋅t) - 0.048970751720
5832⋅sin(40.8407044966673⋅t) + 0.0235785100876881⋅sin(42.4115008234622⋅t) + 0.
0219524059437097⋅sin(45.553093477052⋅t) - 0.0424413181578388⋅sin(47.1238898038
469⋅t) + 0.636619772367581⋅cos(1.5707963267949⋅t) - 0.212206590789194⋅cos(4.71
238898038469⋅t) + 0.127323954473516⋅cos(7.85398163397448⋅t) - 0.09094568176679
73⋅cos(10.9955742875643⋅t) + 0.0707355302630646⋅cos(14.1371669411541⋅t) - 0.05
78745247606892⋅cos(17.2787595947439⋅t) + 0.0489707517205832⋅cos(20.42035224833
37⋅t) - 0.0424413181578388⋅cos(23.5619449019234⋅t) + 0.0374482219039754⋅cos(26
.7035375555132⋅t) - 0.0335063038088201⋅cos(29.845130209103⋅t) + 0.030315227255
5991⋅cos(32.9867228626928⋅t) - 0.0276791205377209⋅cos(36.1283155162826⋅t) + 0.
0254647908947033⋅cos(39.2699081698724⋅t) - 0.0235785100876882⋅cos(42.411500823
4622⋅t) + 0.0219524059437097⋅cos(45.553093477052⋅t) + 0.5
Graficamos la función periódica original y su expansión en Series de Fourier
# Convertimos la expresión Sympy a una función evaluable
fserie = sym.lambdify(t,serie)
f = sym.lambdify(t,ft)
​
# Creamos un vector de tiempo para la gráfica
v_tiempo = np.linspace(Tmin,Tmax,200)
​
# Evaluamos las funciones
fserieG = fserie(v_tiempo)
fG = f(v_tiempo)
 
plt.plot(v_tiempo,fG,label = 'f(t)')
plt.plot(v_tiempo,fserieG,label = 'Expansión')
​
plt.xlabel('tiempo')
plt.legend()
plt.title('Expansión en Series de Fourier')
plt.show()
