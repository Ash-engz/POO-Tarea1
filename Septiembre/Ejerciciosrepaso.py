class Caro:
    modelo = 2012
    Marca = 'Nisan'
    color = ''


texi = Caro()
print(texi.modelo)

#________________________________________________________________________
'''
class Camion:
    pass

truck = Camion
truck2 = Camion

truck.año = 2024
truck.dia= 'miercoles'

truck2.dia = 'jueves'
truck2.mes = 'septiembre'

#print(truck2.mes)
#print(truck.año)

#________________________________________________________________________

class Matematicas:
    def resta(self):
        self.num1 = 80
        self.num2 = 3

operacion = Matematicas()
operacion.resta()
#print(operacion.num1 - operacion.num2)

#_________________________________________________________________________

class Operaciones:
    def __init__(self, num1, num2):
        self.suma = num1 + num2 
        self.resta = num1 - num2 
        self.multiplicacion = num1 * num2
        self.division = num1 / num2 

objeto = Operaciones(5,9)
print(objeto.division)
        

        #QUE PASA SI NO LO CUMPIMOS'8

       # clase abstracta es lo que no conocemos exactamente como dibujar una forma 
 ## interface implementa abstractos ""es"""
 ##QUE PASA CUANDO NO SE USA CONTRATOS? 
#
#-------------------------7
#ASI IMPLEMENTAMOS INTERFACES ABSTRACTAS 
#ABS #MEANS ABSTRACT, AYUDA A ESTANDARIZAR HERENCIA Y METORO ABSTRACTO PARA VISUALIZAR METODOS ABSTRACTOS +
#PARA AGREGAR CLASE ABSTRACTA 

##
#COMO CODIGO NUEVO VAMOS A DEFINIR RUEDAS

#IMPLEMENTAMOS EN LA CLASE CAMOIN LAS RUEDAS 
#
##LO QUE HICIMOS ES LO SIGUIENTE: AUTOMOTOR TIENE UN METODO ABSTRACTO QUE ES RUEDAS ,DICE QUE TODOS LAS LASES DEBEN TENER LA MISMA PROPIEDAD 

#EN EL LADO DERECHO DEFINIMOS RUEDAS EN LA CLASE CAMION 
#
#CREAMOS UN CAMION, LE AGREGAMOS GASOLINA. HAY QUE HACERLO EN TODAS LAS CCLASES 

#@PROPERTI DFINE QUE UNA FUNCION E UNA PROPIEDAD. PROPERTY 

#SE PONE EN CURSIVA SI HACEN LO MISMO PERO DE DIFERENTE FORMA ESO ES ABSTRACTO
##BICICLETA HEREDA DE VEHICULO, CUANOD SE INICIALICE UNA LLAMA A CLASE PADRE Y LLAMA A SUS ARGUMENTOS 
#NINGUNA CLASE ABSTRACTA NOSE PUEDE INSTANCIAR 

# EL OROBLEMAS AUTOMOTOR HEREDA DE VEHICULO, VEHICULO TIENE METODOS ABSTRACTOS TIENE AVANZAR Y RUEDAS PERO NO LOS IMPLETA, SOLO IMPLEMENTA AVANZAR PORL LO QUE RUEDAS ES ABSTRACTO 


 ##SOLO IMPLEMENTAMOS CLASES ABSTRACTAS, 
 '''