class Animal:
    
    def emitir_som(self):
        print("Qualquer Som")
        
class Cachorro(Animal):
    
    def emitir_som(self):
        print("Au Au!")
        
class Gato(Animal):
    def emitir_som(self):
        print("Miau Miau!")
    
cachorro = Cachorro()
gato = Gato()
print("Gato")
gato.emitir_som()
print("Cachorro")
cachorro.emitir_som() 