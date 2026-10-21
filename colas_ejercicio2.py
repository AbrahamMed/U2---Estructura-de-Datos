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
        return None

class ManejadorServicios:
    def __init__(self):
        self.colas = {}
        self.contadores = {}

    def procesar_llegada(self, num_servicio):
        if num_servicio not in self.colas:
            self.colas[num_servicio] = Cola()
            self.contadores[num_servicio] = 1
        
        num_atencion = self.contadores[num_servicio]
        self.colas[num_servicio].encolar(num_atencion)
        self.contadores[num_servicio] += 1
        print(f"Cliente asignado al turno: {num_atencion} (Servicio {num_servicio})")

    def procesar_atencion(self, num_servicio):
        if num_servicio in self.colas and not self.colas[num_servicio].esta_vacia():
            num_llamado = self.colas[num_servicio].desencolar()
            print(f"Llamando al turno: {num_llamado} (Servicio {num_servicio})")
        else:
            print(f"No hay clientes en espera para el servicio {num_servicio}")

def simular_sistema():
    sistema = ManejadorServicios()
    print("--Servicios de Compañia de Seguro--")
    print('Ingrese "C -número-" para registrar la llegada de un cliente')
    print('Ingrese "A -número-" para atender a un cliente')
    print('Ingrese "S" para salir del programa.\n')

    while True:
        entrada = input("Acción: ").strip().upper()
        if entrada == 'S':
            break
        
        partes = entrada.split()
        if len(partes) == 2:
            accion, num_servicio = partes[0], partes[1]
            if num_servicio.isdigit():
                num_servicio = int(num_servicio)
                if accion == 'C':
                    sistema.procesar_llegada(num_servicio)
                elif accion == 'A':
                    sistema.procesar_atencion(num_servicio)
                else:
                    print("Acción inválida")
            else:
                print("El servicio debe ser un número")
        else:
            print('Formato inválido. Use "C 1" o "A 1"')

if __name__ == "__main__":
    simular_sistema()