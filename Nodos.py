class Nodo:
    def __init__(self):
        self.INFO = None
        self.LIGA = None  # Inicia vacío (NIL)


def crea_inicio():
    P = Nodo()
    P.INFO = input("Dato inicial (INFO): ")
    P.LIGA = None
    
    RES = int(input("¿Más nodos? (Sí: 1, No: 0): "))
    while RES == 1:
        Q = Nodo()
        Q.INFO = input("Nuevo dato (INFO): ")
        Q.LIGA = P  # El nuevo nodo apunta al inicio actual
        P = Q       # El nuevo nodo pasa a ser el primero
        RES = int(input("¿Más nodos? (Sí: 1, No: 0): "))
    return P


def inserta_inicio(P, DATO):
    Q = Nodo()
    Q.INFO = DATO
    Q.LIGA = P
    return Q  # Nuevo inicio de la lista


def inserta_final(P, DATO):
    Q = Nodo()
    Q.INFO = DATO
    Q.LIGA = None
    
    if P is None:
        return Q
        
    T = P
    visitados = set()
    while T.LIGA is not None and T.LIGA not in visitados:  # Avanza hasta el último
        visitados.add(T)
        T = T.LIGA
    T.LIGA = Q
    return P


def inserta_antes_X(P, DATO, X):
    if P is None:
        return P

    Q = P
    BAND = 1  # 1 si encuentra a X, 0 si no está
    T = None  # Guarda el nodo anterior a Q
    visitados = set()
    
    while (Q.INFO != X) and (BAND == 1):
        visitados.add(Q)
        if Q.LIGA is not None and Q.LIGA not in visitados:
            T = Q
            Q = Q.LIGA
        else:
            BAND = 0
            
    if BAND == 1:
        NUEVO = Nodo()
        NUEVO.INFO = DATO
        if P == Q:  # Si X está en el primer nodo
            NUEVO.LIGA = P
            P = NUEVO
        else:       # Mete el nuevo nodo entre T y Q
            T.LIGA = NUEVO
            NUEVO.LIGA = Q
    else:
        print(f"Nodo '{X}' no encontrado.")
        
    return P


def inserta_despues_X(P, DATO, X):
    if P is None:
        return P

    Q = P
    BAND = 1
    visitados = set()
    
    while (Q.INFO != X) and (BAND == 1):
        visitados.add(Q)
        if Q.LIGA is not None and Q.LIGA not in visitados:
            Q = Q.LIGA
        else:
            BAND = 0
            
    if BAND == 1:
        T = Nodo()
        T.INFO = DATO
        T.LIGA = Q.LIGA  # Conecta el nuevo nodo después de Q
        Q.LIGA = T
    else:
        print(f"Nodo '{X}' no encontrado.")
        
    return P


def inserta_posicion(P, DATO, POS):
    if POS < 1:
        print("La posición debe ser mayor o igual a 1.")
        return P
        
    if POS == 1 or P is None:
        Q = Nodo()
        Q.INFO = DATO
        Q.LIGA = P
        return Q
        
    T = P
    cont = 1
    visitados = set()
    while cont < (POS - 1) and T.LIGA is not None and T.LIGA not in visitados:
        visitados.add(T)
        T = T.LIGA
        cont += 1
        
    if cont == (POS - 1):
        Q = Nodo()
        Q.INFO = DATO
        Q.LIGA = T.LIGA
        T.LIGA = Q
    else:
        print(f"La posición {POS} está fuera del tamaño de la lista.")
        
    return P


def obtener_camino(inicio):
    camino = []
    actual = inicio
    while actual is not None and actual not in camino:  # Guarda los nodos en orden
        camino.append(actual)
        actual = actual.LIGA
    return camino, actual  # Devuelve la lista de nodos y dónde cerró ciclo (si hay)


def buscar_nodo(P, P2, DATO):
    for inicio in (P, P2):
        camino, _ = obtener_camino(inicio)
        for nodo in camino:
            if nodo.INFO == DATO:
                return nodo
    return None


def dos_nodos_a_uno(P, P2, DATO_1, DATO_2, DESTINO):
    # Guardamos todos los nodos actuales para no perder ninguno
    nodos_antes, _ = obtener_camino(P)
    nodos_rama2, _ = obtener_camino(P2)
    todos = nodos_antes + [n for n in nodos_rama2 if n not in nodos_antes]

    nodo1 = buscar_nodo(P, P2, DATO_1)
    nodo2 = buscar_nodo(P, P2, DATO_2)
    nodo_dest = buscar_nodo(P, P2, DESTINO)
    
    if not nodo1 or not nodo2 or not nodo_dest:
        print("Uno o más nodos no existen en la lista.")
        return P, P2
        
    # Ambos nodos apuntan al mismo destino
    nodo1.LIGA = nodo_dest
    nodo2.LIGA = nodo_dest

    # Si algún nodo quedó desconectado de P, pasa a ser el inicio de P2
    camino_P, _ = obtener_camino(P)
    for n in todos:
        if n not in camino_P:
            P2 = n
            break
            
    return P, P2


def mostrar_extremos(P, P2=None):
    if P is None:
        print("La lista está vacía.\n")
        return
    cam1, _ = obtener_camino(P)
    if P2 is not None:
        cam2, _ = obtener_camino(P2)
        print(f"Inicios: P=[{P.INFO}], P2=[{P2.INFO}] | Último nodo: [{cam1[-1].INFO}]\n")
    else:
        print(f"Primer nodo: [{P.INFO}] | Último nodo alcanzado: [{cam1[-1].INFO}]\n")


def recorrer_lista_grafica(P, P2=None):
    print("\n--- VISTA GRÁFICA DE LA LISTA ---")
    cam1, ciclo1 = obtener_camino(P)
    
    # Caso 1: Hay una segunda rama P2 que se une a la lista principal (Forma de Y)
    if P2 is not None:
        cam2, _ = obtener_camino(P2)
        union = next((n for n in cam1 if n in cam2), None)
        
        if union and cam1.index(union) > 0 and cam2.index(union) > 0:
            idx1 = cam1.index(union)
            idx2 = cam2.index(union)
            
            s1 = " -> ".join(f"[{n.INFO}]" for n in cam1[:idx1])
            s2 = " -> ".join(f"[{n.INFO}]" for n in cam2[:idx2])
            sc = " -> ".join(f"[{n.INFO}]" for n in cam1[idx1:]) + (" -> NIL" if not ciclo1 else f" -> [{ciclo1.INFO}] (Ciclo)")
            
            ancho = max(len(s1), len(s2))
            print(f"P  : {s1} " + "─" * (ancho - len(s1) + 2) + "┐")
            print(" " * (ancho + 8) + f"├──> {sc}")
            print(f"P2 : {s2} " + "─" * (ancho - len(s2) + 2) + "┘")
            mostrar_extremos(P, P2)
            return

    # Caso 2: Dos nodos apuntan al mismo formando un ciclo hacia atrás
    if ciclo1 is not None:
        idx = cam1.index(ciclo1)
        str_antes = "".join(f"[{n.INFO}] -> " for n in cam1[:idx])
        str_ciclo = " -> ".join(f"[{n.INFO}]" for n in cam1[idx:])
        
        print(str_antes + str_ciclo + " ──┐")
        print(" " * len(str_antes) + " ▲" + " " * (len(str_ciclo) + 1) + "│")
        print(" " * len(str_antes) + " └" + "─" * (len(str_ciclo) + 1) + "┘")
        mostrar_extremos(P, P2)
        return

    # Caso 3: Lista normal en una sola línea
    print(" -> ".join(f"[{n.INFO}]" for n in cam1) + " -> NIL")
    mostrar_extremos(P, P2)


if __name__ == "__main__":
    P = crea_inicio()
    P2 = None  # Guarda la segunda rama si se dividen los caminos
    recorrer_lista_grafica(P, P2)
    
    while True:
        print("1. Inicio | 2. Final | 3. Antes de X | 4. Después de X | 5. Posición | 6. Extremos | 7. Dos nodos a uno | 8. Salir")
        op = input("Opción: ")
        
        if op == "1":
            P = inserta_inicio(P, input("Dato: "))
        elif op == "2":
            P = inserta_final(P, input("Dato: "))
        elif op == "3":
            P = inserta_antes_X(P, input("Dato: "), input("Referencia X: "))
        elif op == "4":
            P = inserta_despues_X(P, input("Dato: "), input("Referencia X: "))
        elif op == "5":
            dato = input("Dato: ")
            pos = int(input("Posición (1, 2, 3...): "))
            P = inserta_posicion(P, dato, pos)
        elif op == "6":
            print()
            mostrar_extremos(P, P2)
            continue
        elif op == "7":
            n1 = input("Primer nodo que va a apuntar: ")
            n2 = input("Segundo nodo que va a apuntar: ")
            dest = input("Nodo destino al que ambos apuntarán: ")
            P, P2 = dos_nodos_a_uno(P, P2, n1, n2, dest)
        elif op == "8":
            break
        else:
            continue
            
        recorrer_lista_grafica(P, P2)