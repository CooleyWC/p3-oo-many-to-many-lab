import ipdb

class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        new_contract_obj = Contract(self, book, date, royalties)
        return new_contract_obj
    
    def total_royalties(self):
        total_money = 0
        for contract in Contract.all:
            if contract.author == self:
                total_money += contract.royalties
        return total_money

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book 
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @property
    def book(self):
        return self._book
    
    @property
    def date(self):
        return self._date
    
    @property
    def royalties(self):
        return self._royalties
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception('must be an Author class')

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception('must be a Book class')

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception('must be a date and a string')

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception('must be an integer')
        
    @classmethod    
    def contracts_by_date(cls, date):
        matching_contracts_by_date = []
        for contract in cls.all:
            if contract.date == date:
                matching_contracts_by_date.append(contract)
        return matching_contracts_by_date
