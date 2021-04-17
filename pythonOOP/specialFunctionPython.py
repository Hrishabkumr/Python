class Book():
    
    def __init__(self,title,name,pages):
        self.title = title
        self.name = name
        self.pages = pages
        
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return (f'{self.title} {self.name} {self.pages}')
    
    def __del__(self):
        print('Deleting object')

book = Book('Python Books','Learning',200)


print(book)
        