class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada=None
        
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada=valor

    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
    def propiedadPrivada(self, valor=None):
        if valor==None:
            #actua como getter
            return self.__propiedad_privada
        else:
            #actua como setter
            self.__propiedad_privada=valor

    def __str__(self):
        return "CalseConGetterySetter con propiedad_Privada -> {}".format(self.__propiedad_privada)

if __name__=="__main__":
    c=ClaseConGetterySetter()
    print("imprime lo que tenga por defecto")
    print(c)
    print("\nponemos un valor con el Setter")
    c.setPropiedadPrivada("un chalet con vistas")
    print(c)
    print(c.propiedadPrivada())
    print("\nponemos otro valor con el Setter")
    c.setPropiedadPrivada("un chalet con vistas y piscina climatizada")
    print(c)
    print(c.propiedadPrivada())