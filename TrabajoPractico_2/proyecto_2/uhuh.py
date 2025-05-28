def _eliminar(self,nodo_actual,fecha):
        if not nodo_actual:
            return nodo_actual

        if fecha <  nodo_actual.fecha:
            nodo_actual.izquierda = self._eliminar(nodo_actual.izquierda,fecha)
        elif fecha > nodo_actual.fecha:
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha,fecha)
        else: #Aca ya lo encontramos
            #Debemos tener en cuenta varios casos, esto se me ocurrio a mi cpz que hay alguna manera mas efectiva de hacerlo






            #Caso 1 nodo con un solo hijo o sin hijos
            if nodo_actual.izquierda is None:
                nodo_temporal = nodo_actual.derecha
                return nodo_temporal #El hijo de la derecha reemplaza al actual, si es none es none
            elif nodo_actual.derecha is None:
                nodo_temporal = nodo_actual.izquierda
                return nodo_temporal

            #Caso 2 nodo con dos hijos, aca vamos a aplicar el concepto de sucesor in-order revisar wiki, buscamos el mejor sucesor para los dos hijos huerfanos jajajajajjaja

            #Buscamos el menor valor del arbol, es decir el "sucesor"
            nodo_temporal = self.obtener_valor_minimo(nodo_actual.derecha)


            #Copiamos el sucesor en el eliminado
            nodo_actual.fecha = nodo_temporal.fecha
            nodo_actual.temperatura = nodo_temporal.temperatura
            nodo_actual.derecha = self._eliminar(nodo_actual.derecha, nodo_temporal.fecha)
            #Actualizamos altura
            self.actualizar_altura(nodo_actual)


            #Balance para luego rotar
            balance = self.factor_eq(nodo_actual)

            #Rotaciones, las mismas que al insertar
            if balance > 1 and fecha < nodo_actual.izquierda.fecha:
                return self.rot_derecha(nodo_actual)

                #Dos a la derecha
            if balance < -1 and fecha > nodo_actual.derecha.fecha:
                return self.rot_izquierda(nodo_actual)

                #Izquierda y derecha
            if balance > 1 and fecha > nodo_actual.izquierda.fecha:
                    nodo_actual.izquierda = self.rot_izquierda(nodo_actual.izquierda)
                    return self.rot_derecha(nodo_actual)
                #Derecha y izquierda
            if balance < -1 and fecha < nodo_actual.derecha.fecha:
                    nodo_actual.derecha = self.rot_derecha(nodo_actual.derecha)
                    return self.rot_izquierda(nodo_actual)

            return nodo_actual #Si estaba bien







