import math
class punto:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def __str__(self):
        return f"({self.x}, {self.y})"

class linea:
    def __init__(self, inicio, fin):
        self.inicio= inicio
        self.fin= fin 
        self.longitud= self.compute_length()
        self.pendiente= self.compute_slope() 
    def compute_length(self): # formula de distancia euclediana 
        return math.sqrt((self.fin.x - self.inicio.x)**2 + (self.fin.y - self.inicio.y)**2)
        
    def compute_slope(self):
        if self.fin.x == self.inicio.x: 
             return float('inf')
        pendiente_rad = math.atan2(self.fin.y - self.inicio.y, self.fin.x - self.inicio.x)
        return math.degrees(pendiente_rad)
    def compute_horizontal_cross(self):
        return (self.inicio.y * self.fin.y) <= 0
    def compute_vertical_cross(self):
        return (self.inicio.x * self.fin.x) <= 0
    def __str__(self):
        return f"Linea desde {self.inicio} hasta {self.fin} , Longitud: {self.longitud:.2f}, Pendiente: {self.pendiente:.2f}"
    
punto_1= punto(5, -2)
punto_2= punto(0, -4)

Linea= linea(punto_1, punto_2)

print(Linea)
print("Intercepta el eje x: ", Linea.compute_horizontal_cross())
print("Intercepta el eje y: ", Linea.compute_vertical_cross())
