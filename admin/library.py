#library

class lendableitems():
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.__ischeckedout = False
    
    def checkout(self):
        self.__ischeckedout = True
    
    def checkin(self):
        self.__ischeckedout = False

    def ischeckedout(self, name, checkoutlist):
        ischeckedout = ''
        checkoutlist.append(name)

class book(lendableitems):
    def __init__(self, name, author, pubyear):
        super().__init__(name, author)
        self.pubyear = pubyear


def forceinteger(prompt):
    while True:
        try:
            prompt = int(prompt)
            return prompt
        except ValueError:
            prompt = input('please enter a valid number')

myitems = []
numitems = forceinteger(input('How many items? '))
for index in range(numitems):
    bookname = input('What is the name of this book? ')
    bookauthor = input("What is the author's name of this book? ")
    pubyear = forceinteger(input('What year was the book published? '))

    bookabook = book(bookname, bookauthor, pubyear)
    bookabook.checkout()
    myitems.append(bookabook)

for item in myitems:
    print(item.name)