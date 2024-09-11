class Coffee():
    #Constructor
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def verificar_presupuesto(self, presupuesto):
        #Verificar si el presupuesto es valido
        if not isinstance(presupuesto, (int, float)):
            print("Ingresa un numero entero o decimal")
            exit()
        if presupuesto < 0:
            print("Lo siento, no tienes dinero")
            exit()

    def obtener_cambio(self, presupuesto):
        return presupuesto - self.precio

    def vender(self, presupuesto):
        self.verificar_presupuesto(presupuesto)
        if presupuesto >= self.precio:
            print(f"Puedes comprar el cafe {self.nombre}")
            if presupuesto == self.precio:
                print("Esta completo")
            else:
                print(f"Aqui esta tu cambio {self.obtener_cambio(presupuesto)}$")
                exit()

small = Coffee("Pequeño", 2)
regular = Coffee("Regular", 5)
big = Coffee("Grande", 6)

try:
    user_budget = float(input("¿Cual es tu presupuesto?"))
except ValueError:
    exit("Por favor, ingresa un numero")

for coffee in [big, regular, small]:
    coffee.vender(user_budget)