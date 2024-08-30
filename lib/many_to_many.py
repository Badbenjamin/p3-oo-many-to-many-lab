class Author:
    
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name

    def __repr__(self):
        return f"<{self.name}>"
    
    def contracts(self):
        result = []
        # return self.all
        for contract in Contract.all:
            if contract.author is self:
                result.append(contract)
        return result
    
    def books(self):
        result = []
        for contract in Contract.all:
            if contract.author is self:
                result.append(contract.book)
        return result
    
    def sign_contract(self, book, date, royalties):
        # print(self)
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author is self:
                total += contract.royalties
        return total


class Book:
    
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
        else:
            raise Exception
        
    def contracts(self):
        result = []
        for contract in Contract.all:
            if contract.book is self:
                result.append(contract)
        return result
        
        # if isinstance(author, Author):
        #     self.author = author
        # else:
        #     raise Exception
        
    def __repr__(self):
        return f"<{self.title}>"
    
    def authors(self):
        result = []
        for contract in Contract.all:
            # print(contract.author)
            # print(self)
            if contract.book == self:
                result.append(contract.author)
        return result




class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception
        
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception
        
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception
        
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception
        
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        result = []
        for contract in cls.all:
            if contract.date == date:
                result.append(contract)
        return result

        
    def __repr__(self):
        return f"<Author={self.author}, Book={self.book}, Date={self.date} Royalties=${self.royalties}>"
        

jk = Author("jk")
harry_potter = Book("harry potter")
hp2 = Book("hp2")
hp3 = Book("hp3")

fydor = Author("dostyoyevsky")
the_double = Book("the double")

hp_con = Contract(jk, harry_potter, "2000", 1000)
hp2_con = Contract(jk, hp2, "2010", 4000)
double_con = Contract(fydor, the_double, "1900", 500)

jk.sign_contract(hp3, "2020", 100000)

hp3.authors()