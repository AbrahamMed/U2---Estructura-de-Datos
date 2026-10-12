import tkinter as tk
from tkinter import messagebox

class SimuladorPila:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Pila (LIFO)")
        self.root.geometry("350x500")

        #Crear la pila
        self.pila = []
        self.limite_pila = 8 #Límite que este en la ventana

        #Interfaz
        
        #Marco para los controles
        frame_controles = tk.Frame(root)
        frame_controles.pack(pady=15)

        #Escritura del texto
        self.entrada = tk.Entry(frame_controles, width=10, font=("Arial", 12))
        self.entrada.grid(row=0, column=0, padx=5)

        #Botón para apilar (push)
        btn_push = tk.Button(frame_controles, text="Apilar (Push)", bg="lightgreen", command=self.apilar)
        btn_push.grid(row=0, column=1, padx=5)

        #Botón  para desapilar(pop)
        btn_pop = tk.Button(frame_controles, text="Desapilar (Pop)", bg="salmon", command=self.desapilar)
        btn_pop.grid(row=0, column=2, padx=5)

        #Donde se dibujará la pila
        self.canvas = tk.Canvas(root, width=200, height=400, bg="white", relief=tk.SUNKEN, bd=2)
        self.canvas.pack(pady=10)

        #Crear la pila vacia al comenzar
        self.dibujar_pila()

    #Pila

    def apilar(self):
        valor = self.entrada.get()
        if not valor:
            messagebox.showwarning("Aviso", "Por favor, escribe un valor para apilar.")
            return
        
        if len(self.pila) >= self.limite_pila:
            messagebox.showwarning("Aviso", "La pila está llena")
            return

        #Agregar el valor
        self.pila.append(valor)
        self.entrada.delete(0, tk.END) #Limpiar la entrada
        self.dibujar_pila() #Actualizar lo ingresado 

    def desapilar(self):
        if not self.pila:
            messagebox.showwarning("Aviso", "La pila ya está vacía")
            return

        #Quitar ultimo valor que entro
        self.pila.pop()
        self.dibujar_pila()

    def dibujar_pila(self):
        #Limpiar para volver a crear
        self.canvas.delete("all")
        
        #Tamaño del bloque
        x0 = 50
        y0 = 380
        ancho = 100
        alto = 45

        #Se recorre la pila y se crea cada bloque
        for i, valor in enumerate(self.pila):
            y_actual = y0 - (i * alto)
            
            #Rectangulo del bloque
            self.canvas.create_rectangle(
                x0, y_actual - alto, x0 + ancho, y_actual, 
                fill="lightblue", outline="black"
            )
            
            #Escribir dentro del bloque
            self.canvas.create_text(
                x0 + (ancho / 2), y_actual - (alto / 2), 
                text=valor, font=("Arial", 12, "bold")
            )

#Para ejecutar el programa
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = SimuladorPila(ventana_principal)
    ventana_principal.mainloop()