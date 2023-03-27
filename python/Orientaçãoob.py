class Celular:
    marca = "Nokia"
    modelo = "Tijolão"
    cor = "Azul"
    tem_camera = False
    bateria = "Infinita"
    
    def fazer_ligações(self):
        print("Fazendo ligação...")
        
    def jogar_cobrinha(self):
        print("Jogando cobrinha...")
        
    def despertador(self):
        print("Despértando...")

celular = Celular()
print(celular.marca)
print(celular.modelo)
print(celular.bateria)
print(celular.tem_camera    )