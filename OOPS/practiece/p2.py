from p1 import book_id
class book:
    def __init__(self,book_name,id,author):
        self.book_name=book_name
        self.id=id
        self.author=author
        self.ob_id=book_id(book_name,id,author)
o1=book("everything under",2345,"daisy johnson")
o2=book("introduction to dreamland",3456,"bhagat singh")
o3=book("stairway to earth",4567,"bill birchard")
print("book:2")
o2.ob_id.info()
print("book:1")
o1.ob_id.info()
print("book:3")
o3.ob_id.info()