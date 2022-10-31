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

    def display(self):
        print(f"{self.name} is at ({self.x}, {self.y})")

if __name__ == "__main__":

    alpha = Particle("Alpha")
    beta = Particle("Beta")
    delta = Particle("Delta")

    alpha.movedown()
    alpha.moveright()
    alpha.moveright()

    beta.moveup()
    beta.moveup()
    beta.moveright()

    delta.movedown()
    delta.movedown()
    delta.moveleft()

    alpha.display()
    beta.display()
    delta.display()



