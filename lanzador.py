from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta

def lanzador_main():
    vehiculos = [
        Coche("rojo", 4, 150, 1200),
        Coche("azul", 4, 200, 2000),
        Bicicleta("verde", 2, "bh", "bmx", "urbana"),
        Bicicleta("blanca", 2, "orbea", "r2", "deportiva"),
        Camioneta("negro", 4, 100, 2200, "ford", "ranger", 1000),
        Motocicleta("blanca", 2, "Suzuki", "GSXR", "Deportiva", 300, 999)
    ]
    return vehiculos  # Devolvemos la lista para usarla en main.py

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()
    else:
        for vehiculo in vehiculos:
            print(f"Clase: {vehiculo.__class__.__name__}")
            for atributo, valor in vehiculo.__dict__.items():
                print(f"{atributo}: {valor}")
            print()