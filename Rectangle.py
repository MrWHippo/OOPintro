

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

class framedRectangle(rectangle):
    def __init__(self, width, height, symbol):
        super().__init__(width,height)
        self.framedsymbol = symbol
    
    def draw(self):
        frame = "#"
        row = "."
        print(frame*(self.w +4))
        for i in range(self.h):
            print(frame, row*self.w, frame) 
        print(frame*(self.w + 4))

                


if __name__ == "__main__":
    rect1 = framedRectangle(2,6,"#")
    rect1.draw()
    x = int(input("Enter StretchX value: "))
    rect1.stretchX(x)
    y = int(input("Enter StretchY value: "))
    rect1.stretchY(y)
    rect1.draw()
    


    
