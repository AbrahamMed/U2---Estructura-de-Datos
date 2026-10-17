from typing import List

class Pila:
    def __init__(self) -> None:
        self.elementos: List[float] = []

    def apilar(self, dato: float) -> None:
        self.elementos.append(dato)

    def desapilar(self) -> float:
        if self.esta_vacia():
            raise IndexError("Error: Faltan operandos en la expresión")
        return self.elementos.pop()

    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0

    def tamaño(self) -> int:
        return len(self.elementos)


class EvaluadorExpresiones:
    OPERADORES = {'+', '-', '*', '/', '^'}

    @staticmethod
    def _aplicar_operacion(operador: str, a: float, b: float) -> float:
        if operador == '+': return a + b
        if operador == '-': return a - b
        if operador == '*': return a * b
        if operador == '^': return a ** b
        if operador == '/':
            if b == 0:
                raise ZeroDivisionError("Error: División por cero no permitida.")
            return a / b
        raise ValueError(f"Operador no soportado: {operador}")

    @classmethod
    def evaluar_posfija(cls, expresion: str) -> float:
        pila = Pila()

        for token in expresion.split():
            if token not in cls.OPERADORES:
                pila.apilar(float(token))
            else:
                # En posfija, el primer desapilado es el operando derecho
                operando_derecho = pila.desapilar()
                operando_izquierdo = pila.desapilar()
                
                resultado = cls._aplicar_operacion(token, operando_izquierdo, operando_derecho)
                pila.apilar(resultado)

        if pila.tamaño() != 1:
            raise ValueError("Error de sintaxis: Sobran operandos")
        return pila.desapilar()

    @classmethod
    def evaluar_prefija(cls, expresion: str) -> float:
        pila = Pila()

        # En prefija, la expresión se lee de derecha a izquierda
        for token in reversed(expresion.split()):
            if token not in cls.OPERADORES:
                pila.apilar(float(token))
            else:
                # Al leer al revés, el primer desapilado es el operando izquierdo
                operando_izquierdo = pila.desapilar()
                operando_derecho = pila.desapilar()
                
                resultado = cls._aplicar_operacion(token, operando_izquierdo, operando_derecho)
                pila.apilar(resultado)

        if pila.tamaño() != 1:
            raise ValueError("Error de sintaxis: Sobran operandos")
        return pila.desapilar()


    #Pruebas de expresiones
    
if __name__ == "__main__":
    evaluador = EvaluadorExpresiones()

    # Equivalente infijo para ambas: 5 + ((1 + 2) * 4) - 3 = 14
    expr_posfija = "5 1 2 + 4 * + 3 -"
    expr_prefija = "- + 5 * + 1 2 4 3"

    try:
        print("Expresión Posfija:", expr_posfija)
        print("Resultado Posfija:", evaluador.evaluar_posfija(expr_posfija), "\n")

        print("Expresión Prefija:", expr_prefija)
        print("Resultado Prefija:", evaluador.evaluar_prefija(expr_prefija))
    except Exception as e:
        print(f"Error en la evaluación: {e}")