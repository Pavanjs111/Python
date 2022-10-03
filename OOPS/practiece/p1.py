class book_id:
    def __init__(self,book_name,id,author):
        self.book_name=book_name
        self.id=id
        self.author=author
    def info(self):
        print("book name:",self.book_name)
        print("book id:",self.id)
        print("author:",self.author)
