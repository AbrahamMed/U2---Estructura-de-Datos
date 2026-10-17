from typing import List

class Pila:
    def __init__(self) -> None:
        self.elementos: List[str] = []

    def apilar(self, dato: str) -> None:
        self.elementos.append(dato)

    def desapilar(self) -> str:
        if self.esta_vacia():
            raise IndexError("Error: La pila está vacía.")
        return self.elementos.pop()

    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0

    def tamaño(self) -> int:
        return len(self.elementos)


class NavegadorWeb:
    def __init__(self, pagina_inicio: str = "about:blank") -> None:
        self.historial_atras = Pila()
        self.historial_adelante = Pila()
        self.pagina_actual = pagina_inicio
        print(f"Navegador abierto en: {self.pagina_actual}")

    def visitar(self, url: str) -> None:
        self.historial_atras.apilar(self.pagina_actual)
        self.pagina_actual = url
        
        # Al visitar una nueva URL, el historial de avance se invalida
        self.historial_adelante = Pila()
        print(f"Visitando: {self.pagina_actual}")

    def atras(self) -> None:
        if self.historial_atras.esta_vacia():
            print("Acción denegada: No hay historial hacia atrás")
            return

        self.historial_adelante.apilar(self.pagina_actual)
        self.pagina_actual = self.historial_atras.desapilar()
        print(f"<- Retrocediendo a: {self.pagina_actual}")

    def adelante(self) -> None:
        if self.historial_adelante.esta_vacia():
            print("Acción denegada: No hay historial hacia adelante")
            return

        self.historial_atras.apilar(self.pagina_actual)
        self.pagina_actual = self.historial_adelante.desapilar()
        print(f"-> Avanzando a: {self.pagina_actual}")

    def mostrar_estado(self) -> None:
        print(f"\n[Estado] Página actual: {self.pagina_actual} | "
              f"Historial atrás: {self.historial_atras.tamaño()} | "
              f"Historial adelante: {self.historial_adelante.tamaño()}\n")


#Pruebas de ejecución

if __name__ == "__main__":
    navegador = NavegadorWeb("google.com")
    
    navegador.visitar("gemini.google.com")
    navegador.visitar("sie.merida.tecnm.mx")
    navegador.visitar("youtube.com")
    navegador.mostrar_estado()
    
    navegador.atras()
    navegador.atras()
    navegador.mostrar_estado()
    
    navegador.adelante()
    
    print("\nVisitando nuevo enlace desde el medio del historial...")
    navegador.visitar("xbox.com")
    
    navegador.adelante()
    navegador.mostrar_estado()