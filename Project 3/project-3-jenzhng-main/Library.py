# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 1/25/2023
# Description: Class named LibraryItem with six data members (library_item_id, title, location, checked_out_by, requested_by,
#                  date_checked_out). Subclasses Book, Movie, Album.
#              Class named Library with three data members (holdings, members, current_date)
#              Class named Patron with four data members (patron_id, name, checked_out_items, fine_amount)

class LibraryItem:
    '''
        Represents LibraryItem
    '''
    def __init__(self, library_item_id, title, location="ON_SHELF", checked_out_by=None, requested_by=None,
                 date_checked_out=None):
        '''
            Creates a LibraryItem object with six data members (library_item_id, title, location, checked_out_by, requested_by,
            date_checked_out). Subclasses Book, Movie, Album.
        '''
        self._library_item_id = library_item_id
        self._title = title
        self._location = location
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by
        self._date_checked_out = date_checked_out
    def get_library_item_id(self):
        return self._library_item_id
    def get_title(self):
        return self._title
    def get_location(self):
        return self._location
    def set_location(self, status):
        self._location = status
    def get_checked_out_by(self):
        return self._checked_out_by
    def set_checked_out_by(self, patron):
        self._checked_out_by = patron
    def get_requested_by(self):
        return self._requested_by
    def set_requested_by(self, patron):
        self._requested_by = patron
    def get_date_checked_out(self):
        return self._date_checked_out
    def set_date_checked_out(self, date):
        self._date_checked_out = date

class Book(LibraryItem):
    '''
        Subclass of LibraryItem. Represents Book object.
    '''
    def __init__(self, library_item_id, title, author):
        '''
            Creates a Book object that inherits from LibraryItem with additional data member author.
        '''
        super(Book, self).__init__(library_item_id, title)
        self._author = author
    def get_author(self):
        '''
            Returns the author.
        '''
        return self._author

class Movie(LibraryItem):
    '''
            Subclass of LibraryItem. Represents Movie object.
    '''
    def __init__(self, library_item_id, title, director):
        '''
                Creates a Movie object that inherits from LibraryItem with additional data member director.
        '''
        super(Movie, self).__init__(library_item_id, title)
        self._director = director
    def get_director(self):
        '''
            Returns the director.
        '''
        return self._director
class Album(LibraryItem):
    '''
        Subclass of LibraryItem. Represents Album object.
    '''
    def __init__(self, library_item_id, title, artist):
        '''
            Creates a Album object that inherits from LibraryItem with additional data member artist.
        '''
        super(Album, self).__init__(library_item_id, title)
        self._artist = artist
    def get_artist(self):
        '''
            Returns the director.
        '''
        return self._artist




class Patron:
    '''
        Represents Patron
    '''
    def __init__(self, patron_id, name, checked_out_items={}, fine_amount=0):
        '''
            Creates a Patron object with four data members (patron_id, name, checked_out_items, fine_amount).
        '''
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = checked_out_items
        self._fine_amount = fine_amount
    def get_patron_id(self):
        '''
            Returns the patron_id.
        '''
        return self._patron_id
    def get_checked_out_items(self):
        '''
            Returns checked_out_items.
        '''
        return self._checked_out_items
    def get_fine_amount(self):
        '''
            Returns the fine_amount.
        '''
        return self._fine_amount
    def add_library_item(self, item):
        '''
            Add library_item to patron list of checked out items
        :param item:
        :return:
        '''
        self._checked_out_items.update({item.get_library_item_id(): item})
    def remove_library_item(self, item):
        '''
            Remove library_item to patron list of checked out items
        :param item:
        :return:
        '''
        if item in self._checked_out_items:
            del self._checked_out_items[item]
    def amend_fine(self, amount):
        '''
            Change patron fine amount
        :param amount:
        :return:
        '''
        self._fine_amount += amount

class Library:
    '''
        Represents Library
    '''
    def __init__(self, holdings={}, members={}, current_date=0):
        '''
            Creates a library object with three data members (holdings, members, current_date)
        :param holdings:
        :param members:
        :param current_date:
        '''
        self._holdings = holdings
        self._members = members
        self._current_date = current_date
    def add_library_item(self, item):
        '''
            Add library item to library holdings
        :param item:
        :return:
        '''
        self._holdings.update({item.get_library_item_id(): item})

    def add_patron(self, patron):
        '''
            Add patron to library members
        :param patron:
        :return:
        '''
        self._members.update({patron.get_patron_id(): patron})

    def lookup_library_item_from_id(self, item):
        '''
            Search library item from id
        :param item:
        :return:
        '''
        if item in self._holdings:
            return self._holdings[item]
        else:
            return None
    def lookup_patron_from_id(self, patron):
        '''
            Search patron from id
        :param patron:
        :return:
        '''
        if patron in self._members:
            return self._members[patron]
        else:
            return None
    def check_out_library_item(self, patron, item):
        '''
            Check out an item from library according to patron
        :param patron:
        :param item:
        :return:
        '''
        patron_exists = False
        for key in self._members:
            if key == patron:
                patron_exists = True
        if item not in self._holdings:
            return "item not found"
        for key in self._holdings:
            if key == item:
                item_exists = True
                if self._holdings[key].get_location() == "CHECKED_OUT":
                    return "item already checked out"
                if self._holdings[key].get_requested_by() and self._holdings[key].get_requested_by() != patron:
                    return "item on hold by other patron"
                if patron_exists and item_exists:
                    self._holdings[key].set_date_checked_out(self._current_date)
                    self._holdings[key].set_checked_out_by(patron)
                    self._members[patron].add_library_item(self._holdings[key])
                    self._holdings[key].set_location("CHECKED_OUT")
                    if self._holdings[key].get_requested_by() == patron:
                        self._holdings[key].set_requested_by(None)
                        return "check out successful"
                    else:
                        return "check out successful"

    def return_library_item(self, item):
        '''
            Return library item
        :param item:
        :return:
        '''
        if item not in self._holdings:
            return "item not found"
        if self._holdings[item].get_location() != "CHECKED_OUT":
            return "item already in library"

        if item in self._holdings:
            self._members[self._holdings[item].get_checked_out_by()].remove_library_item(item)
            self._holdings[item].set_location("ON_SHELF")
            self._holdings[item].set_checked_out_by(None)
            return "return successful"



    def request_library_item(self, patron, item):
        '''
            Request hold on library item
        :param patron: 
        :param item: 
        :return: 
        '''
        if patron not in self._members:
            return "patron not found"
        if item not in self._holdings:
            return "item not found"
        if self._holdings[item].get_requested_by() != None:
            return "item already on hold"
        else:
            self._holdings[item].set_requested_by(patron)
            if self._holdings[item].get_location() == "ON_SHELF":
                self._holdings[item].set_location("ON_HOLD_SHELF")
                return "request successful"
            return "request successful"

    def pay_fine(self, patron, amount):
        '''
            Subtract fine from patron account
        :param patron: 
        :param amount: 
        :return: 
        '''
        if patron not in self._members:
            return "patron not found"
        else:
            self._members[patron].amend_fine(-abs(amount))
            return "payment successful"
    def increment_current_date(self):
        '''
            Increment date by one day
        :return: 
        '''
        self._current_date += 1

        for key in self._holdings:
            if self._holdings[key].get_checked_out_by() != None:
                self._members[self._holdings[key].get_checked_out_by()].amend_fine(0.1)

def main():
    # Use a breakpoint in the code line below to debug your script.
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")

    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())


    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")
    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)

    lib.add_patron(p1)
    lib.add_patron(p2)

    print(lib.check_out_library_item("bcd", "456"))
    
    #print(lib.check_out_library_item("abc", "567"))
    loc = a1.get_location()
    # print(loc)
    #print(lib.return_library_item("456"))
    lib.request_library_item("abc", "456")
    for _ in range(7):
        lib.increment_current_date()
    p2_fine = p2.get_fine_amount()

if __name__ == '__main__':
    main()
