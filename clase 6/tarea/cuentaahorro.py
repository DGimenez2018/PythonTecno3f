from tarea.cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    TASA_INTERES = 0.001 

    def __init__(self, titular, cbu, saldo_inicial=0):
        super().__init__(titular, cbu, saldo_inicial)

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        if monto > self._saldo:
            print(f"[CuentaAhorro] Saldo insuficiente. Saldo disponible: ${self._saldo:,.2f}")
            return
        self._saldo -= monto
        print(f"[CuentaAhorro] Extracción de ${monto:,.2f} realizada. Saldo restante: ${self._saldo:,.2f}")

    def aplicar_interes(self):
        interes = self._saldo * self.TASA_INTERES
        self._saldo += interes
        print(f"[CuentaAhorro] Interés aplicado (0.1%): +${interes:,.2f} | Nuevo saldo: ${self._saldo:,.2f}")
