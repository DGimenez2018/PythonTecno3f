from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    def __init__(self, titular, cbu, saldo_inicial=0):
        self._titular = titular
        self._cbu = cbu
        self._saldo = 0
        self.saldo = saldo_inicial


    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo.")
        self._saldo = valor

    @property
    def cbu(self):
        return self._cbu

    @property
    def titular(self):
        return self._titular

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a cero.")
        self._saldo += monto
        print(self)

    def __str__(self):
        return (
            f"Titular : {self._titular}\n"
            f"CBU     : {self._cbu}\n"
            f"Saldo   : ${self._saldo:,.2f}"
        )

    @abstractmethod
    def extraer(self, monto):
        """Cada subclase define sus propias reglas de extraccion."""
        pass
