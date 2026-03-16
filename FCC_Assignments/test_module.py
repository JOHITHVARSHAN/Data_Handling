# Unit tests for demographic_data_analyzer.py

import unittest
import pandas as pd
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data=False)

    def test_race_count(self):
        # Test that race_count is a pandas Series
        self.assertIsInstance(self.data['race_count'], pd.Series)
        # Test that it has the expected races
        expected_races = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
        for race in expected_races:
            self.assertIn(race, self.data['race_count'].index)

    def test_average_age_men(self):
        # Test that average_age_men is a float
        self.assertIsInstance(self.data['average_age_men'], float)
        # Test that it's reasonable (between 30 and 50)
        self.assertGreater(self.data['average_age_men'], 30)
        self.assertLess(self.data['average_age_men'], 50)

    def test_percentage_bachelors(self):
        # Test that percentage_bachelors is a float
        self.assertIsInstance(self.data['percentage_bachelors'], float)
        # Test that it's between 0 and 100
        self.assertGreaterEqual(self.data['percentage_bachelors'], 0)
        self.assertLessEqual(self.data['percentage_bachelors'], 100)

    def test_higher_education_rich(self):
        # Test that higher_education_rich is a float
        self.assertIsInstance(self.data['higher_education_rich'], float)
        # Test that it's between 0 and 100
        self.assertGreaterEqual(self.data['higher_education_rich'], 0)
        self.assertLessEqual(self.data['higher_education_rich'], 100)

    def test_lower_education_rich(self):
        # Test that lower_education_rich is a float
        self.assertIsInstance(self.data['lower_education_rich'], float)
        # Test that it's between 0 and 100
        self.assertGreaterEqual(self.data['lower_education_rich'], 0)
        self.assertLessEqual(self.data['lower_education_rich'], 100)

    def test_min_work_hours(self):
        # Test that min_work_hours is an int
        self.assertIsInstance(self.data['min_work_hours'], int)
        # Test that it's positive
        self.assertGreater(self.data['min_work_hours'], 0)

    def test_rich_percentage(self):
        # Test that rich_percentage is a float
        self.assertIsInstance(self.data['rich_percentage'], float)
        # Test that it's between 0 and 100
        self.assertGreaterEqual(self.data['rich_percentage'], 0)
        self.assertLessEqual(self.data['rich_percentage'], 100)

    def test_highest_earning_country(self):
        # Test that highest_earning_country is a string
        self.assertIsInstance(self.data['highest_earning_country'], str)

    def test_highest_earning_country_percentage(self):
        # Test that highest_earning_country_percentage is a float
        self.assertIsInstance(self.data['highest_earning_country_percentage'], float)
        # Test that it's between 0 and 100
        self.assertGreaterEqual(self.data['highest_earning_country_percentage'], 0)
        self.assertLessEqual(self.data['highest_earning_country_percentage'], 100)

    def test_top_IN_occupation(self):
        # Test that top_IN_occupation is a string
        self.assertIsInstance(self.data['top_IN_occupation'], str)

if __name__ == "__main__":
    unittest.main()