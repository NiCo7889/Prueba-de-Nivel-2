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
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return print("El punto {} pertenece al primer cuadrante.".format(self))
        if self.x < 0 and self.y < 0:
            return print("El punto {} pertenece al tercer cuadrante.".format(self))
        if self.x > 0 and self.y < 0:
            return print("El punto {} pertenece al cuarto cuadrante.".format(self))
        if self.x < 0 and self.y > 0:
            return print("El punto {} pertenece al cuarto cuadrante.".format(self))
        else:
            return print("El punto {} es el origen.".format(self))
        
    def vector(self, punto):
        self.punto = punto
        return print("El resultado entre estos dos puntos es: ({}, {})".format(punto.x - self.x, punto.y - self.y))


    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)^2 + (punto.y - self.y)^2)
        return print("La distancia entre los puntos {} y {} es: {}".format(self, punto, distancia))


"""
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
• Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
• Añade al rectángulo un método llamado base que muestre la base.
• Añade al rectángulo un método llamado altura que muestre la altura.
• Añade al rectángulo un método llamado area que muestre el area.
Sugerencia
Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. Si andas perdido, prueba de dibujarlo en un papel, ¡seguro
que lo verás mucho más claro! Además recuerda que puedes utilizar la función abs() para saber el valor absolute de un número.
"""


class rectangulo:
    def __init__(self, inicial = Punto(), final = Punto()):
        self.inicial = inicial
        self.final = final

    def base(self):
        self.base = abs(self.final.x - self.inicial.x)
        return print("Base del rectángulo {}".format(self.base))

    def altura(self):
        self.altura = abs(self.final.y - self.final.y)
        return print("Altura del rectángulo {}".format(self.altura))
    
    def area(self):
        self.base = abs(self.final.x - self.inicial.x)
        self.altura = abs(self.final.y - self.final.y)
        self.area = self.base * self.altura
        return print("El área del rectángulo son {} u^2.".format(self.area))
    
"""
• Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
• Consulta a que cuadrante pertenecen el punto A, C y D.
• Consulta los vectores AB y BA.
• (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
• (Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
• Crea un rectángulo utilizando los puntos A y B.
• Consulta la base, altura y área del rectángulo.
"""

# EXPERIMENTACIÓN

print("Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.\n")
punto1 = Punto(2, 3)
punto2 = Punto(5, 5)
punto3 = Punto(-3, -1)
origen = Punto(0, 0)

print("Consulta a que cuadrante pertenecen el punto A, C y D.\n")
punto1.cuadrante()
punto3.cuadrante()
origen.cuadrante()

print("Consulta la distancia entre los puntos 'A y B' y 'B y A'.\n")
punto1.vector(punto2)
punto2.vector(punto1)

print("Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).\n")
punto1.distancia(origen)
punto2.distancia(origen)
punto3.distancia(origen)
print("Crea un rectángulo utilizando los puntos A y B.\n")
Rectangulo = rectangulo(punto1, punto2)

print("Consulta la base, altura y área del rectángulo.\n")
Rectangulo.base()
Rectangulo.altura()
Rectangulo.area()