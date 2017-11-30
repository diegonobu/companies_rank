import unittest

import company
import report

companies = [
    company.Company('IT Services', [
        '4571 778',
        '4571 917',
        '4569 3',
        '4569 2',
        '4571 544',
        '4567 4',
        '4571 1',
        '4570 1',
        '4569 0',
        '4568 2'
    ]),
    company.Company('MyBank', [
        '4568 1',
        '4571 0',
        '4569 194',
        '4571 3',
        '4570 4',
        '4567 2',
        '4568 4',
        '4568 0',
        '4570 1',
        '4569 2'
    ])
]


class TestReport(unittest.TestCase):
    def test_should_zero_be_fav(self):
        self.assertTrue(report.is_fav(0))

    def test_should_one_be_fav(self):
        self.assertTrue(report.is_fav(1))

    def test_should_two_be_neutral(self):
        self.assertFalse(report.is_fav(2))
        self.assertFalse(report.is_unfav(2))

    def test_should_three_be_unfav(self):
        self.assertTrue(report.is_unfav(3))

    def test_should_four_be_unfav(self):
        self.assertTrue(report.is_unfav(4))

    def test_should_other_numbers_be_neutral(self):
        self.assertFalse(report.is_fav(5))
        self.assertFalse(report.is_unfav(5))

        self.assertFalse(report.is_fav(6))
        self.assertFalse(report.is_unfav(6))

        self.assertFalse(report.is_fav(10))
        self.assertFalse(report.is_unfav(10))

    def test_should_summary_by_company_works(self):
        summary = report.Report(companies)
        summary = summary.summary_by_companies()

        self.assertIn('IT Services', summary.keys())
        self.assertIn('MyBank', summary.keys())

        self.assertIn('4569', summary['IT Services'])
        self.assertIn('4567', summary['IT Services'])
        self.assertIn('4571', summary['IT Services'])
        self.assertIn('4570', summary['IT Services'])
        self.assertIn('4568', summary['IT Services'])

        self.assertIn('4568', summary['MyBank'])
        self.assertIn('4571', summary['MyBank'])
        self.assertIn('4570', summary['MyBank'])
        self.assertIn('4567', summary['MyBank'])
        self.assertIn('4569', summary['MyBank'])

    def test_should_show_quantity_of_valid_answers(self):
        quantity = report.Report(companies)
        quantity = quantity.valid_answers()

        self.assertIn('IT Services', quantity.keys())
        self.assertIn('MyBank', quantity.keys())

        self.assertEqual(7, quantity['IT Services'])
        self.assertEqual(9, quantity['MyBank'])

        # def test_should_return_fav_answer_by_question(self):
        #     by_question = report.Report(companies)
        #     by_question = by_question.fav_answer_by_question()
        #
        #     self.assertIn('4567', by_question.keys())
        #     self.assertIn('4568', by_question.keys())
        #     self.assertIn('4569', by_question.keys())
        #     self.assertIn('4570', by_question.keys())
        #     self.assertIn('4571', by_question.keys())
        #
        #     self.assertIn('IT Services', by_question['4567'])
        #     self.assertIn('IT Services', by_question['4568'])
        #     self.assertIn('IT Services', by_question['4569'])
        #     self.assertIn('IT Services', by_question['4570'])
        #     self.assertIn('IT Services', by_question['4571'])
        #
        #     self.assertIn('MyBank', by_question['4567'])
        #     self.assertIn('MyBank', by_question['4568'])
        #     self.assertIn('MyBank', by_question['4569'])
        #     self.assertIn('MyBank', by_question['4570'])
        #     self.assertIn('MyBank', by_question['4571'])


if __name__ == '__main__':
    unittest.main()
