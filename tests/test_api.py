import unittest
import requests

from parameterized import parameterized

from tools.people import People

# NOTE: we are assuming that the original json data will be used for these tests
# NOTE: hence, changing the data will cause a lot of these tests to fail, since they require pre-determined results
# NOTE: while making it dynamic is possible, that would mean implementing code again, which is something to be avoided as much as possible in tests
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_base = "http://localhost:5000"
        
        cls.people_path = "resources/people.json"
        cls.people = People(cls.people_path)

    @parameterized.expand(
        [
            ("PERMADYNE", [
                "Frost Foley",
                "Luna Rodgers",
                "Boyer Raymond",
                "Solomon Cooke",
                "Walter Avery",
                "Hester Malone",
                "Arlene Erickson"
            ]),
            ("LINGOAGE", [
                "Sue Tyson",
                "Hobbs Lang",
                "Shelly Koch",
                "Santiago Baker",
                "Lolita Walls",
                "Shari Farrell",
                "Gordon Wolfe"
            ])
        ]
    )
    def test_get_employees(self, company_name: str, expected_employees: list[str], endpoint: str ="/company/{}"):
        response = requests.get(self.api_base + endpoint.format(company_name))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"employees": expected_employees})

    @parameterized.expand(
        [
            ("NETBOOK", 204),
            ("this company does not exist", 204),
            (5, 204)
        ]
    )
    def test_get_employees_fails(self, company_name: str, status_code: int, endpoint: str ="/company/{}"):
        response = requests.get(self.api_base + endpoint.format(company_name))
        self.assertEqual(response.status_code, status_code)

    # NOTE: making the code somewhat dynamic here, to show that it's possible
    @parameterized.expand(
        [
            ("Carmella Lambert", "Decker Mckenzie", []),
            ("Goodwin Cook", "Tammy Lowery", ["Decker Mckenzie"])
        ]
    )
    def test_get_mutual_friends(self, person1_name: str, person2_name: str, mutual_friends: list[str], endpoint: str ="/mutualfriends/{}/{}"):
        response = requests.get(self.api_base + endpoint.format(person1_name, person2_name))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "mutual_friends": mutual_friends,
            "person1": self.people.get_person_by_name(person1_name).temp(),
            "person2": self.people.get_person_by_name(person2_name).temp()
        })
    
    def test_get_mutual_friends_only_one_person(self, endpoint: str ="/mutualfriends/{}"):
        response = requests.get(self.api_base + endpoint.format("Carmella Lambert"))
        
        # TODO: make sure it's not a 404?
        self.assertEqual(response.status_code, 404)

    def test_get_mutual_friends_non_existent_person(self, endpoint: str ="/mutualfriends/{}/{}"):
        response = requests.get(self.api_base + endpoint.format("Carmella Lambert", "not a real name"))
        
        self.assertEqual(response.status_code, 204)

    @parameterized.expand(
        [
            ("Rosemary Hayes", {"age":30,"fruits":["orange","apple"],"username":"Rosemary Hayes","vegetables":["carrot","celery"]}),
            ("Carmella Lambert", {"age":61,"fruits":["orange","apple","banana","strawberry"],"username":"Carmella Lambert","vegetables":[]})
        ]
    )
    def test_get_person_info(self, name: str, expected_result: dict, endpoint: str="/person/{}"):
        response = requests.get(self.api_base + endpoint.format(name))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
        
    def test_get_person_info_non_existent_name(self, endpoint: str="/person/{}"):
        response = requests.get(self.api_base + endpoint.format("not a real name"))
        
        self.assertEqual(response.status_code, 204)

    @parameterized.expand(
        [
            ("/",),
            ("/test",),
            ("/index",)
        ]
    )
    def test_bad_endpoints(self, endpoint: str):
        response = requests.get(self.api_base + endpoint)

        # TODO: custom 404 page, and checking if it's valid?
        self.assertEqual(response.status_code, 404)
