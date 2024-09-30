class triangulo: 
    def __init__(self,color,base, altura, area ):
        self.base =4 
        self.altura= 6
        self.color= 'verde'
        self.area= (base*altura)/2
        

    def area(self):
        return 


    def dibujar (self):
        return f"Hola soy un triangulo de color: {self.color} y de area: {self.area}"
    
print (triangulo.area())
print (triangulo.dibujar())

class trinagulo(shape):
    def __init__(self,color,base,altura):
        self.base = base
        self.altura = altura 
        super().__init__(color)

        def area(self):
            return (base*altura)/2
        
    def dibujar (self):
        return f"Hola soy un triangulo de color: {self.color} y de area: {self.area}"
    
    triangulo = triangulo('verde',4,6)
    print (triangulo.area())
    print (triangulo.dibujar())
    