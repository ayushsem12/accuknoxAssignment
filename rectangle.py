#The main method takes length and width as arguments to initialize an instance of the Rectangle class.

class Rectangle:
    def main(self, length: int, width: int):
        self.length = length
        self.width = width
    
 #The __iter__ method allows the object to be iterable
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
