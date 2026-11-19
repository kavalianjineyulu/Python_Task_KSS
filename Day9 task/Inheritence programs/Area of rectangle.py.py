class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length * self.width
        print("length:",self.length)
        print("width:",self.width)
        print("area of rectangle:",area)
r1 = rectangle(10,5)
r1.calculate_area()
