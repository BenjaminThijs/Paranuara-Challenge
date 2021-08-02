import unittest
import json

from parameterized import parameterized

from tools.dto.company import Company
from tools.companies import Companies
from tools.exceptions import NoSuchNameException

class TestCompanies(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.companies_path = "test_resources/companies.json"

        cls.companies = Companies(cls.companies_path)

    def test_population(self):
        # NOTE: we only check if the right amount of items were added here
        with open(self.companies_path, "r") as companies_json:
            self.assertEqual(len(self.companies.list), len(json.load(companies_json)))

    @parameterized.expand(
        [
            ("company_a", Company(**{"index": 0, "company": "company_a"})),
            ("company_b", Company(**{"index": 1, "company": "company_b"})),
            ("company_c", Company(**{"index": 2, "company": "company_c"})),
            ("company_d", Company(**{"index": 3, "company": "company_d"})),
            ("company_e", Company(**{"index": 4, "company": "company_e"}))
        ]
    )
    def test_get_company_by_name(self, name: str, expected_output: Company):
        self.assertEqual(self.companies.get_company_by_name(name), expected_output)
        
    def test_get_company_without_name(self):
        self.assertRaises(TypeError, self.companies.get_company_by_name)

    def test_get_company_with_non_existent_name(self):
        self.assertRaises(NoSuchNameException, self.companies.get_company_by_name, "this name should not exist")

    def test_create_companies_with_wrong_path(self):
        self.assertRaises(FileNotFoundError, Companies, "not the real path")
