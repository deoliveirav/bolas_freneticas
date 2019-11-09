class Bola:
    def __init__(self, x, y, tam):
        self.x = x
        self.y = y
        self.tam = tam
        self.cor = color(random(255),
                         random(255),
                         random(255))
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
    
    def plot(self):
        circle(self.x, self.y, self.tam)
        
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x > width or self.x < 0:
            self.vx = -self.vx
        if self.y > height or self.y < 0:
            self.vy = -self.vy     
            
    def position(self):
        self.x = self.vx + random(width)
        self.y = self.vy + random(height)
    
                       
