from AVL import AVL
import datetime



class temperatura_db:
    def __init__(self):
        self.arbol_temperatura = AVL() #Creamos la instancia en si

    def guardar_temperatura(self ,temperatura,fecha):
        #Logica para convertir fecha en objeto date
        fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        if not isinstance(fecha_obj,datetime.date): 
            raise(f"Error: El formato de la fecha '{fecha_str}' no es válido. Use 'dd/mm/aaaa'.")
        
        #Nos aseguramos de que sea un flotante, podriamos agregar algun seguro aca tmb
        temperatura_float = float(temperatura)

        self.arbol_temperatura.insertar(fecha_obj,temperatura_float)
        return (print(f"Dato guardado/actualizado: {fecha_obj.strftime('%d/%m/%Y')} - {temperatura_float}°C"))

    




        


