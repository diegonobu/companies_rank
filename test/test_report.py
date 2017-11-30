import unittest

import company
import report


class TestReport(unittest.TestCase):
    def setUp(self):
        self.companies = [
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
        summary = report.Report(self.companies)
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


if __name__ == '__main__':
    unittest.main()
