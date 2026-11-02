from tarea.cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):
    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=0):
        if costo_emision < 0:
            raise ValueError("El costo de emisión no puede ser negativo.")
        self._costo_emision = costo_emision
        super().__init__(titular, cbu, saldo_inicial)

    @property
    def costo_emision(self):
        return self._costo_emision

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("El monto a extraer debe ser mayor a cero.")
        total = monto + self._costo_emision
        if total > self._saldo:
            print(
                f"[CuentaCheque] Saldo insuficiente. Se necesitan ${total:,.2f} "
                f"(monto: ${monto:,.2f} + comisión: ${self._costo_emision:,.2f}). "
                f"Saldo disponible: ${self._saldo:,.2f}"
            )
            return
        self._saldo -= total
        print(
            f"[CuentaCheque] Extracción de ${monto:,.2f} realizada "
            f"(+ comisión ${self._costo_emision:,.2f}). Saldo restante: ${self._saldo:,.2f}"
        )
