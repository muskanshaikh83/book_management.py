class Book_Collection:
   def __init__(self):
    self.book={}
    def add_book(self,name,quantity):
        if quantity <=0:
        print("The book quantity is Invalid.") 
        return
        if name in self.book:
            self.book[name]+= quantity
            else:
                self.book[name]=quantity
                print("quantity",quantity,"book name",name)
    def remove_book(self,name,quantity):
        if name not in self.book:
            print("book is not found")            
            return

        if quantity<=0:
            print("An Invalid Quantity")
            return

        if quantity > self.book[name]:
            print("not enough stock to remove that quantity")
            return
        self.book[name]-=quantity
        if self.book [name]==0:
            del self.book[name]
            print("book removed from shelf ")
            else:
                print(f"{name} of{quantity}")
    def view_book(self):
        if not self.book:
            print("shelf is empty..")
            return
        for name,quantity in self.book.name():
            print(f"{name}:{quantity}")
    def total_book(self):
        total=sum(self.book.values())
        print(f"total book: {total}")


def main():
    book_collection=Book_Collection()
    while True:
        print("The collection of books")
        print("Add the books")
        print("remove the books")
        print("view book collection")
        print("get the Total books in stock")

        select=input("Enter the number (1-5)")
        if select="1":
            name=input("enter the book name:").strip()
            quantity=int(input("enter the quantity:"))
            book_collection.add_book(name,quantity)

        elif select==2:
            name=input("enter the book name:").strip()
            quantity=int(input("enter the quantity:"))
            book_collection.remove_book(name,quantity)

        elif select==3:
            book_collection.view_book()

        elif select==4:
            book_collection.total_book()
        elif select ==5:
            print("existing program")
            break
        else:
            print("invalid selection")