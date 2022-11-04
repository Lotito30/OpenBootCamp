lista_paises = []
pregunta_finalizar = "Si"
while pregunta_finalizar != "No":
    pregunta_pais = input("Ingresa un pais: ").capitalize()
    lista_paises.append(pregunta_pais)
    pregunta_finalizar = input("Quieres ingresar mas paises?: ").capitalize()

lista_paises = sorted(list(set(lista_paises)))
print(lista_paises)