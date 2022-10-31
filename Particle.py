class Particle:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0 
    
    def moveup(self):
        self.y += 1

    def movedown(self):
        self.y -= 1

    def moveright(self):
        self.x += 1

    def moveleft(self):
        self.x -= 1

    def display(self, name):
        print(f"{name} is at ({self.x}, {self.y})")

if __name__ == "__main_":

    alpha = Particle("Alpha")
    beta = Particle("Beta")
    delta = {}

    for x in range(6):
        delta.append(Particle(x))
        

    alpha.movedown()
    alpha.moveright()
    alpha.moveright()

    beta.moveup()
    beta.moveup()
    beta.moveright()

    alpha.display("Alpha")
    beta.display("Beta")

    for x in range(6):
        print(delta[x])



