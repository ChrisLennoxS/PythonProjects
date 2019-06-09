class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # using f string literal
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        return self.__str__() + " has been deleted"


my_new_book = Book("Maze Runner", "James Dashner", 304)
print(my_new_book)
print(len(my_new_book))
print(my_new_book.__del__())

