class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular=titular
        self.__saldo=cantidad

    def get_cantidad(self):
        return self.__saldo
    
    def ingresar (self, monto):
        if monto > 0:
            self.__saldo += monto
    
    def retirar (self, monto):
        if monto > 0 and self.__saldo >= monto:
            self.__saldo -= monto

    def mostrar_info (self):
        return f"Titular: {self.titular} * cantidad: $ {self.__saldo}"
    
if __name__ == "__main__":
    cuenta= Cuenta("Juan Pérez", 1000000)
    print(cuenta.mostrar_info())

    cuenta.ingresar(500000)
    print("Saldo actualizado después de su deposito")
    print(cuenta.mostrar_info())

    cuenta.retirar(2000)
    print("Saldo actualizado después de su retiro")
    print (cuenta.mostrar_info())