"""
Crea una clase llamada Punto con sus dos coordenadas X e Y.
• Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
• Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
• Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e 
Y== 0 está sobre el origen.
• Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
• (Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla.
"""

import math 


class Punto:
    def __init__(self, x = 0, y =0):
        self.x = x
        self.y = y

    def __str__(self):
        return print("({},{})".format(self.x, self.y))
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return print("El punto ({},{}) pertenece al primer cuadrante.".format(self.x, self.y))
        if self.x < 0 and self.y < 0:
            return print("El punto ({},{}) pertenece al tercer cuadrante.".format(self.x, self.y))
        if self.x > 0 and self.y < 0:
            return print("El punto ({},{}) pertenece al cuarto cuadrante.".format(self.x, self.y))
        if self.x < 0 and self.y > 0:
            return print("El punto ({},{}) pertenece al cuarto cuadrante.".format(self.x, self.y))
        else:
            return print("El punto ({},{}) es el origen.")
        
    def vector(self):


    def distancia(self, )