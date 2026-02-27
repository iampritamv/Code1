class book:

    #constructor 
    def __init__(self , title , author):
        
        self.title = title 
        self.name = author

    def show(self):

        print(f"book : {self.title} by {self.name}")

book1 = book("Atomic habit" , "James clear")
book1.show()