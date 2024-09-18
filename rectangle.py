class Rectangle:
    def main(self, length: int, width: int):
        self.length = length
        self.width = width
    
  
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}