import unittest
import json

from parameterized import parameterized

from tools.people import People
from tools.exceptions import NoSuchNameException


class TestPeople(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.people_path = "test_resources/people.json"

        cls.people = People(cls.people_path)
    
    def test_population(self):
        # NOTE: we only check if the right amount of items were added here
        with open(self.people_path, "r") as people_json:
            self.assertEqual(len(self.people.list), len(json.load(people_json)))

    @parameterized.expand(
        [
            (0,),
            (1,),
            (2,),
            (3,),
            (-1,)
        ]
    )
    def test_index_control(self, index: int):
        self.assertEqual(self.people[index], self.people.list[index])

    @parameterized.expand(
        [
            (4, IndexError),
            (10, IndexError),
            ("not an index", TypeError)
        ]
    )
    def test_index_control_fails(self, index: int, error_type: type):
        self.assertRaises(error_type, self.people.__getitem__, index)

    @parameterized.expand(
        [
            (0, []),
            (1, [1]),
            (2, [2]),
            (3, [0, 3]),
            (10, [])
        ]
    )
    def test_get_employees(self, company_id: int, expected_employee_ids: list[int]):
        employees = self.people.get_employees(company_id=company_id)

        # NOTE: we only check if the index is correct, not the entire object (for brevity)
        self.assertEqual([p.index for p in employees], expected_employee_ids)
    
    @parameterized.expand(
        [
            ("index",),
            (True,),
            ([],),
            (set(),),
            ({},)
        ]
    )
    def test_get_employees(self, company_id):
        self.assertRaises(TypeError, self.people.get_employees, company_id)

    @parameterized.expand(
        [
            ("Carmella Lambert", 0),
            ("Decker Mckenzie", 1),
            ("Bonnie Bass", 2),
            ("Rosemary Hayes", 3)
        ]
    )
    def test_get_person_by_name(self, name: str, expected_person_id: int):
        self.assertEqual(self.people.get_person_by_name(name).index, expected_person_id)

    
    @parameterized.expand(
        [
            ("John Doe",)
        ]
    )
    def test_get_person_by_name_fails(self, name: str):
        self.assertRaises(NoSuchNameException, self.people.get_person_by_name, name)
