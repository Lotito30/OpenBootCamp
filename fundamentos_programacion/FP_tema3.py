def main():
    suma(1,2,3)
    micoche = Coche()
    micoche.incrementar_puertas(1)
    print(micoche)
    
def suma(a,b,c):
    resultado = a+b+c
    print(f'Resultado suma: {resultado}')

class Coche:
    puertas = 4

    def __str__ (self):
        return f'Cantidad de puertas: {self.puertas}'

    def incrementar_puertas(self,incrementar):
        self.puertas += incrementar
if __name__ == '__main__':
    main()
