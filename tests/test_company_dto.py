import unittest

from parameterized import parameterized

from tools.dto.company import Company

# NOTE: slightly useless to test this unless extra steps would be taken in the DTOs (data cleaning for example)
class TestCompanyDTO(unittest.TestCase):
    @parameterized.expand(
        [
            ({"index": 0, "company": "company_a"},),
            ({"index": 1, "company": "company_b"},),
            ({"index": 2, "company": "company_c"},),
            ({"index": 3, "company": "company_d"},)
        ]
    )
    def test_company_DTO(self, company_dict: dict):
        company = Company(**company_dict)

        self.assertEqual(company.index, company_dict["index"])
        self.assertEqual(company.company, company_dict["company"])
    
    @parameterized.expand(
        [
            ({"index": 0, "company": "company_a", "other_field": "value"},),
            ({"index": 1},),
            ({"company": "company_b"},)
        ]
    )
    def test_company_DTO_fails(self, company_dict: dict):
        # NOTE: since it's Python, types are not enforced by default, hence we do not check it atm
        self.assertRaises(TypeError, Company, **company_dict)
