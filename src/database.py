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
        
    def vector(self, punto):
        self.punto = punto
        return print("El resultado entre estos dos puntos es: {}".format(self - punto))


    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)^2 + (punto.y - self.y)^2)
        return print("La distancia entre los puntos {} y {} es: {}".format(self, punto, distancia))


"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
• Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
• Añade al rectángulo un método llamado base que muestre la base.
• Añade al rectángulo un método llamado altura que muestre la altura.
• Añade al rectángulo un método llamado area que muestre el area.
"""


class rectangulo:
    def __init__(self, inicial, final):
        self.inicial = inicial
        self.final = final

    def base(self):

    def altura(self):

    def area(self):

    