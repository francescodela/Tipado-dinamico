def retornar(valor):
    if isinstance(valor, int):
        print(valor * 2)
    elif isinstance(valor, str):
        print(valor + " esta bien ")
    elif isinstance(valor, float):
        print(valor / 2)
    elif isinstance(valor, list):
        print(valor + valor)
    elif isinstance(valor, bool):
        print(not valor)
    elif isinstance(valor, dict):
        print({k: v * 2 if isinstance(v, int) else v for k, v in valor.items()})
    elif isinstance(valor, tuple):
        print(tuple(reversed(valor)))
    else:
        print("Tipo de dato no soportado")

retornar(30)
retornar("frank")
retornar(103.5)
retornar([1, 6 , 3])
retornar(True)
retornar({"b": 1, "d": 2})
retornar((1, 2, 3))
