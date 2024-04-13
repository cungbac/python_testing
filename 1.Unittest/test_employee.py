import unittest
from employee import Employee, len_joke
from unittest.mock import patch, MagicMock

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownClass')
    
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Bac', 'Tran', 5000)
        self.emp_2 = Employee('Corey', 'Schafer', 6000)

    def tearDown(self) -> None:
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Bac.Tran@email.com')
        self.assertEqual(self.emp_2.email, 'Corey.Schafer@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Bac Tran')
        self.assertEqual(self.emp_2.fullname, 'Corey Schafer')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Tran')
        self.assertEqual(self.emp_2.fullname, 'Jane Schafer')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Tran/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Schafer/June')
            self.assertEqual(schedule, 'Bad Response!')

    @patch('employee.requests.get')
    def test_monthly_schedule_2(self, mocked_get):
        mocked_get.return_value.ok = True
        mocked_get.return_value.text = 'Success'

        schedule = self.emp_1.monthly_schedule('May')
        mocked_get.assert_called_with('http://company.com/Tran/May')
        print(schedule)
        self.assertEqual(schedule, 'Success')

        mocked_get.return_value.ok = False

        schedule = self.emp_2.monthly_schedule('June')
        # print(schedule)
        mocked_get.assert_called_with('http://company.com/Schafer/June')
        self.assertEqual(schedule, 'Bad Response!')

    @patch('employee.get_joke')
    def test_len_monthly_schedule(self, mocked_get):
        mocked_get.return_value = 'hello world'
        len_joke()
        self.assertEqual(len_joke(), 3)


if __name__ == "__main__":
    unittest.main()