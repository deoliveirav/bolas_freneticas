from bola import Bola

lista_bolas = []

def setup():
    size(500, 500)
    for i in range(100):
        nova_bola = Bola(250, 250, 40)
        lista_bolas.append(nova_bola)
    
def draw():
    background(0)
    for bola in lista_bolas:
        bola.plot()
        bola.move()

def keyPressed():
    if key == " ": 
        for bola in lista_bolas:
            bola.position()
            
