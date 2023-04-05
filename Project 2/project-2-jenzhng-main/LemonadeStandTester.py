import unittest
from LemonadeStand import LemonadeStand, MenuItem

class TestLemonadeStand(unittest.TestCase):  # The class name can be whatever you want
  """
  Contains unit tests for the LemonadeStand class   
  """

  def test_1(self):  
    """Test init method and get methods"""
    stand_1 = LemonadeStand('Lemons R Us')
    self.assertEqual(stand_1.get_name(), 'Lemons R Us')
	
  def test_2(self):
    stand_1 = LemonadeStand('Get your lemons')
    item1 = MenuItem('cannoli', 0.5, 1.5)
    stand_1.add_menu_item(item1)
    day_0_sales = {
    'cannoli' : 1}
    stand_1.enter_sales_for_today(day_0_sales)
    self.assertEqual(stand_1.total_profit_for_menu_item('cannoli'), 1.0)
    
  def test_3(self):
    stand_1 = LemonadeStand('Step right up')
    item1 = MenuItem('banana', 0.5, 1.5)
    stand_1.add_menu_item(item1)
    day_0_sales = {
    'banana' : 1}
    stand_1.enter_sales_for_today(day_0_sales)
    for key in stand_1._menu_item:
       self.assertIn('banana', stand_1._menu_item)
	   
  def test_4(self):
    stand_1 = LemonadeStand('Sunny day')
    item1 = MenuItem('peach', 0.5, 1.5)
    stand_1.add_menu_item(item1)
    item2 = MenuItem('pear', 0.2, 1)
    stand_1.add_menu_item(item2)
    day_0_sales = {
	'peach' : 5,
	'pear'   : 2
    }
    stand_1.enter_sales_for_today(day_0_sales) 
    self.assertEqual(stand_1.total_profit_for_stand(), 5.4)

  def test_5(self):
    stand_1 = LemonadeStand('Private')
    item1 = MenuItem('bearclaw', 0.5, 1.5)
    stand_1.add_menu_item(item1)
    day_0_sales = {
	'bearclaw' : 5
    }
    stand_1.enter_sales_for_today(day_0_sales) 
    self.assertEqual(stand_1.total_sales_for_menu_item('bearclaw'), 5)
    

if __name__ == '__main__':    
  unittest.main(exit=False)

