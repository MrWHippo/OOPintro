

class rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def stretchY(self, factor):
        self.h *= factor
    
    def stretchX(self, factor):
        self.w *= factor

    def draw(self):
        row = "#"
        for i in range(self.h):
                print(row*self.w)
                


if __name__ == "__main__":
    rect1 = rectangle(3,5)
    rect1.draw()
    x = int(input("Enter StretchX value: "))
    rect1.stretchX(x)
    y = int(input("Enter StretchY value: "))
    rect1.stretchY(y)
    rect1.draw()


    
