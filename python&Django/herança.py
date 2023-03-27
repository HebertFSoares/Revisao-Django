class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print("VRUM VRUM")
    
    def frear(self):
        print("Skiiiii")
        
    def buzinar(self):
        print("BI-Bi BI-BI")
    
    
class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992
    
uno = Uno()
uno.acelerar()
print(uno.numero_rodas)