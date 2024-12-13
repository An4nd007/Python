class Rect():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print("area:",a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("perimeter:",p)
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
data=Rect(l,b)
data.area()
data.perimeter()
