class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return 0 

def sumar_colas(cola_a, cola_b):
    print(f"{'Cola A':<8} {'Cola B':<8} {'Cola Resultado'}")
    
    cola_resultado = Cola()
    
    while not cola_a.esta_vacia() or not cola_b.esta_vacia():
        val_a = cola_a.desencolar()
        val_b = cola_b.desencolar()
        
        suma = val_a + val_b
        cola_resultado.encolar(suma)
        
        print(f"  {val_a:<6}   {val_b:<6}   {suma}")
        
    return cola_resultado

#Para ejecutar
if __name__ == "__main__":
    cola1 = Cola()
    cola2 = Cola()

    #Cola A
    for num in [2, 1000, 121, 100, 34]:
        cola1.encolar(num)

    #Cola B
    for num in [1, 5, 8, 11000, 1000]:
        cola2.encolar(num)

    resultado = sumar_colas(cola1, cola2)