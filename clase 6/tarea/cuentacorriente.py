from tarea.cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=0):
        if limite_descubierto < 0:
            raise ValueError("El límite de descubierto no puede ser negativo.")
        self._limite_descubierto = limite_descubierto
        super().__init__(titular, cbu, saldo_inicial)

    @property
    def limite_descubierto(self):
        return self._limite_descubierto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        disponible = self._saldo + self._limite_descubierto
        if monto > disponible:
            print(
                f"[CuentaCorriente] Límite superado. Disponible: ${disponible:,.2f} "
                f"(saldo: ${self._saldo:,.2f} + descubierto: ${self._limite_descubierto:,.2f})"
            )
            return
        self._saldo -= monto
        print(f"[CuentaCorriente] Extracción de ${monto:,.2f} realizada. Saldo restante: ${self._saldo:,.2f}")
