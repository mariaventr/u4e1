from tkinter import *
from tkinter import ttk

class IPCCalculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Cálculo del IPC")

        # Etiquetas
        ttk.Label(self.root, text="Item").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.root, text="Vestimenta").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.root, text="Alimentos").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self.root, text="Educación").grid(row=3, column=0, padx=5, pady=5)
        ttk.Label(self.root, text="Cantidad").grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Precio Año Base").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self.root, text="Precio Año Actual").grid(row=0, column=3, padx=5, pady=5)

        # Marcos para ingresar datos
        self.entry_vestimenta_cantidad = ttk.Entry(self.root, width=15)
        self.entry_vestimenta_cantidad.grid(row=1, column=1, padx=5, pady=5)
        self.entry_alimentos_cantidad = ttk.Entry(self.root, width=15)
        self.entry_alimentos_cantidad.grid(row=2, column=1, padx=5, pady=5)
        self.entry_educacion_cantidad = ttk.Entry(self.root, width=15)
        self.entry_educacion_cantidad.grid(row=3, column=1, padx=5, pady=5)
        self.entry_vestimenta_precio_base = ttk.Entry(self.root, width=15)
        self.entry_vestimenta_precio_base.grid(row=1, column=2, padx=5, pady=5)
        self.entry_alimentos_precio_base = ttk.Entry(self.root, width=15)
        self.entry_alimentos_precio_base.grid(row=2, column=2, padx=5, pady=5)
        self.entry_educacion_precio_base = ttk.Entry(self.root, width=15)
        self.entry_educacion_precio_base.grid(row=3, column=2, padx=5, pady=5)
        self.entry_vestimenta_precio_actual = ttk.Entry(self.root, width=15)
        self.entry_vestimenta_precio_actual.grid(row=1, column=3, padx=5, pady=5)
        self.entry_alimentos_precio_actual = ttk.Entry(self.root, width=15)
        self.entry_alimentos_precio_actual.grid(row=2, column=3, padx=5, pady=5)
        self.entry_educacion_precio_actual = ttk.Entry(self.root, width=15)
        self.entry_educacion_precio_actual.grid(row=3, column=3, padx=5, pady=5)

        # Botones
        btn_calcular = ttk.Button(self.root, text="Calcular IPC", command=self.calcular_ipc)
        btn_calcular.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        btn_salir = ttk.Button(self.root, text="Salir", command=self.root.quit)
        btn_salir.grid(row=5, column=2, sticky="w", padx=5, pady=5)

        # Resultado
        self.label_resultado = ttk.Label(self.root, text="")
        self.label_resultado.grid(row=6, column=0, padx=5, pady=5)

    def calcular_ipc(self):
        try:
            cantidad_vestimenta_2022 = float(self.entry_vestimenta_cantidad.get())
            precio_base_vestimenta = float(self.entry_vestimenta_precio_base.get())
            cantidad_vestimenta_2023 = float(self.entry_vestimenta_precio_actual.get())
            
            cantidad_alimentos_2022 = float(self.entry_alimentos_cantidad.get())
            precio_base_alimentos = float(self.entry_alimentos_precio_base.get())
            cantidad_alimentos_2023 = float(self.entry_alimentos_precio_actual.get())
            
            cantidad_educacion_2022 = float(self.entry_educacion_cantidad.get())
            precio_base_educacion = float(self.entry_educacion_precio_base.get())
            cantidad_educacion_2023 = float(self.entry_educacion_precio_actual.get())
            
            costo_base_vestimenta = cantidad_vestimenta_2022 * precio_base_vestimenta
            costo_actual_vestimenta = cantidad_vestimenta_2023 * precio_base_vestimenta
            
            costo_base_alimentos = cantidad_alimentos_2022 * precio_base_alimentos
            costo_actual_alimentos = cantidad_alimentos_2023 * precio_base_alimentos
            
            costo_base_educacion = cantidad_educacion_2022 * precio_base_educacion
            costo_actual_educacion = cantidad_educacion_2023 * precio_base_educacion
            
            ipc_vestimenta = int((costo_actual_vestimenta / costo_base_vestimenta - 1) * 100)
            ipc_alimentos = int((costo_actual_alimentos / costo_base_alimentos - 1) * 100)
            ipc_educacion = int((costo_actual_educacion / costo_base_educacion - 1) * 100)
            
            self.label_resultado.config(text=f"IPC: Vestimenta {ipc_vestimenta}%, Alimentos {ipc_alimentos}%, Educación {ipc_educacion}%")
        except ValueError:
            self.label_resultado.config(text="Error: Llene todos los campos")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = IPCCalculator()
    app.run()
