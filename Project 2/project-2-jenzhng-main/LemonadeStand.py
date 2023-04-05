# Author: Jenny Zhong
# GitHub username: jenzhng
# Date: 1/18/2023
# Description: Class named LemonadeStand with four data members.
#              Class named SalesForDay with two data members.
#              Class named MenuItem with three data members.


class MenuItem:
    '''
    Represents MenuItem 
    '''
    def __init__(self, name, cost, price):
        '''
        Creates a MenuItem object with three data members: name, cost, price.
        '''
        self._name = name
        self._cost = cost
        self._price = price
    
    def get_name(self):
        '''
        Returns the name.
        '''
        return self._name
    def get_cost(self):
        '''
        Returns the cost.
        '''
        return self._cost
    def get_price(self):
        '''
        Returns the price
        '''
        return self._price

class SalesForDay:
    '''
    Represents SalesForDay 
    '''
    def __init__(self, day, sales_dict):
        '''
        Creates a SalesForDay object with two data members: day, sales_dict
        '''
        self._day = day
        self._sales_dict = sales_dict
    def get_day(self):
        '''
        Returns the day
        '''
        return self._day
    def get_sales_dict(self):
        '''
        Returns the sales_dict
        '''
        return self._sales_dict   
class LemonadeStand:
    '''
    Represents LemonadeStand 
    '''
    def __init__(self, name, day=0, menu_item={}, sales_for_today=[]):
        '''
        Creates a LemonadeStand object with four data members: name, day, dict of MenuItems, and list of SalesForDay objects
        '''
        self._name = name
        self._day = day
        self._menu_item = menu_item
        self._sales_for_today = sales_for_today
    def get_name(self):
        '''
        Returns the name.
        '''
        return self._name
    def add_menu_item(self, item):
        '''
        Takes a MenuItem object as an argument and adds it to the menu dictionary
        '''
        self._menu_item.update({item.get_name():item}) 
    def enter_sales_for_today(self, sales_dict):
        
        for key in sales_dict:
            if key not in self._menu_item:
                raise InvalidSalesItemError
        for key in self._menu_item:
            if key not in sales_dict:
                sales_dict[key] = 0
        self._sales_for_today.append(SalesForDay(self._day, sales_dict))
        self._day += 1
    def sales_of_menu_item_for_day(self, day):
        '''
        Return sales of menu item for day
        '''
        for key in self._sales_for_today:
            if key.get_day() == day:
                return key.get_sales_dict()
    
    def total_sales_for_menu_item(self, item_name):
        '''
        Returns total sales for particular menu item
        '''
        sales = 0
        for day in self._sales_for_today:
            sales += day.get_sales_dict()[item_name]
        return sales
        
    def total_profit_for_menu_item(self, item_name):
        '''
        Subtracts total cost from total price in sales of particular item and returns profit for particular item
        '''
        return self._menu_item[item_name].get_price() * self.total_sales_for_menu_item(item_name) - self._menu_item[item_name].get_cost() * self.total_sales_for_menu_item(item_name)

    def total_profit_for_stand(self):
        '''
        Returns total profit for stand
        '''
        total = 0
        for key in self._menu_item:
            total += self.total_profit_for_menu_item(key)
        return total
        
class InvalidSalesItemError(Exception):
    pass


def main():
	stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
	item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
	stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
	item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
	stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
	item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
	stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'
	day_0_sales = {
		'lemonade' : 5,
		'cookie'   : 2,
		'cannoli' : 0
	}
	#stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
	#print(f"lemonade profit = {stand.total_profit_for_menu_item('ice')}")
	try:
		stand.enter_sales_for_today(day_0_sales) 
	except(InvalidSalesItemError):
		print("This is an invalid sales item.")

if __name__ == "__main__":
    main()

