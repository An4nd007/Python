class publisher:
    def __init__(self,n):
         self.name = n
              
class book(publisher):
    def __init__(self,n,t,a):
         super().__init__(n)
         self.title = t
         self.author = a
                
class python(book):
    def __init__(self,n,t,a,p,pgs):
        super().__init__(n,t,a)
        self.price = p
        self.pages = pgs
               
    def display(self):
        print("Publisher name: ",self.name)
        print("Book title:",self.title)
        print("Author name:",self.author)
        print("Price:",self.price)
        print("Number of pages:",self.pages)
pl = python("python","introduction to python","jeeva jose",450,300)
pl.display()
