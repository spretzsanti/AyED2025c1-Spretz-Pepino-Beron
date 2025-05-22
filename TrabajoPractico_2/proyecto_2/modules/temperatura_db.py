from AVL import AVL
import datetime



class temperatura_db:
    def __init__(self):
        self.arbol_temperatura = AVL() #Creamos la instancia en si


    def formato_fecha(self,fecha:str):
        fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        if not isinstance(fecha_obj,datetime.date): 
            raise(f"Error: El formato de la fecha '{fecha_str}' no es válido. Use 'dd/mm/aaaa'.")

        return fecha_obj




    def guardar_temperatura(self ,temperatura,fecha):
        
        fecha_obj = self.formato_fecha(fecha)
        
        #Nos aseguramos de que sea un flotante, podriamos agregar algun seguro aca tmb
        temperatura_float = float(temperatura)

        self.arbol_temperatura.insertar(fecha_obj,temperatura_float)
        return (print(f"Dato guardado/actualizado: {fecha_obj.strftime('%d/%m/%Y')} - {temperatura_float}°C"))


    def devolver_temperatura(self,fecha:str):

        fecha_obj = self.formato_fecha(fecha)
        temperatura_encontrada = self.arbol_temperatura.buscar(fecha_obj)

        if temperatura_encontrada is not None:
            return temperatura_encontrada
        else:
            # Opcional: imprimir un mensaje si no se encuentra la fecha.
            print(f"Información: No se encontró temperatura para la fecha {fecha}.")
            

    




        


