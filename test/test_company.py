import unittest

import company


class TestCompany(unittest.TestCase):
    def test_collect_all_data(self):
        item = company.collect_from_file('tmp/test.txt')

        self.assertEqual(item.name, 'IT Services')
        self.assertEqual(len(item.data), 10)

        self.assertEqual(item.data[0], '4571 778')
        self.assertEqual(item.data[1], '4571 917')
        self.assertEqual(item.data[2], '4569 3')
        self.assertEqual(item.data[3], '4569 2')
        self.assertEqual(item.data[4], '4571 544')
        self.assertEqual(item.data[5], '4567 4')
        self.assertEqual(item.data[6], '4571 1')
        self.assertEqual(item.data[7], '4570 1')
        self.assertEqual(item.data[8], '4569 0')
        self.assertEqual(item.data[9], '4568 2')

    def test_zero_should_be_valid_answer(self):
        self.assertTrue(company.verify_valid_answer(0))

    def test_one_should_be_valid_answer(self):
        self.assertTrue(company.verify_valid_answer(1))

    def test_two_should_be_valid_answer(self):
        self.assertTrue(company.verify_valid_answer(2))

    def test_three_should_be_valid_answer(self):
        self.assertTrue(company.verify_valid_answer(3))

    def test_four_should_be_valid_answer(self):
        self.assertTrue(company.verify_valid_answer(4))

    def test_other_should_not_be_valid_answer(self):
        self.assertFalse(company.verify_valid_answer(5))
        self.assertFalse(company.verify_valid_answer(6))
        self.assertFalse(company.verify_valid_answer(10))
        self.assertFalse(company.verify_valid_answer(100))

    def test_should_clean_all_data(self):
        item = company.collect_from_file('tmp/test.txt')
        data = item.clean_data()

        self.assertEqual(len(data[0]), 7)

        self.assertEqual(data[0][0], ('4569', 3))
        self.assertEqual(data[0][1], ('4569', 2))
        self.assertEqual(data[0][2], ('4567', 4))
        self.assertEqual(data[0][3], ('4571', 1))
        self.assertEqual(data[0][4], ('4570', 1))
        self.assertEqual(data[0][5], ('4569', 0))
        self.assertEqual(data[0][6], ('4568', 2))


if __name__ == '__main__':
    unittest.main()
