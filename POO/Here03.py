class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.saldo:.2f}")


class CuentaAhorro(Cuenta):
    def __init__(self, titular, saldo, tasa_interes):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * (self.tasa_interes / 100)
        self.saldo += interes
        print(f"Interés aplicado: ${interes:.2f}")


class CuentaCorriente(Cuenta):
    def __init__(self, titular, saldo, limite_sobregiro):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= self.saldo + self.limite_sobregiro:
            self.saldo -= monto
            print(f"Retiro exitoso de ${monto:.2f}")
        else:
            print("Fondos insuficientes. No se puede realizar el retiro.")


cuenta_ahorro = CuentaAhorro("Samuel Rodriguez", 2000, 5)
cuenta_corriente = CuentaCorriente("Emanuel Morales", 1000, 500)

print("CUENTA DE AHORRO:")
cuenta_ahorro.mostrar_informacion()
cuenta_ahorro.aplicar_interes()
cuenta_ahorro.mostrar_informacion()

print("CUENTA CORRIENTE:")
cuenta_corriente.mostrar_informacion()
cuenta_corriente.retirar(1200)
cuenta_corriente.mostrar_informacion()
