import unittest
from banker import Account,Saving, Fixed
class TestBanker(unittest.TestCase):
    def setUp(self):
        self.saving = Saving("Timothy Wikedzi","0136856611",2000)
        self.fixed = Fixed("Gladness Wikedzi","0159556116",2000,365,0.5)

    #Saving account test cases
    def test_saving_instance(self):
        self.assertIsInstance(self.saving, Saving, msg='The object should be an instance of the Saving class')
    
    def test_saving_parent_object(self):
        self.assertIsInstance(self.saving, Account, msg='The Saving Object should be an instance of the Account class')
    
    def test_saving_deposit(self):
        balance_after_deposit = self.saving.deposit(430);
        self.assertEqual(self.saving.getBalance(), balance_after_deposit,msg='The account balance should be updated after deposit')
    
    def test_saving_withdraw(self):
        balance_after_withdraw = self.saving.withdraw(1200);
        self.assertEqual(self.saving.getBalance(), balance_after_withdraw,
                        msg='The account balance should be larger than the withdraw amount')

    #Fixed Account test cases
    def test_fixed_instance(self):
        self.assertIsInstance(self.fixed, Fixed, msg='The object should be an instance of the Fixed class')
    
    def test_fixed_parent_object(self):
        self.assertIsInstance(self.fixed, Account, msg='The Fixed Object should be an instance of the Account class')


if __name__ == '__main__':
    unittest.main()