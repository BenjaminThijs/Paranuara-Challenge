import unittest
import json

from tools.dto.person import Person

# NOTE: slightly useless to test this unless extra steps would be taken in the DTOs (data cleaning for example)
class TestPersonDTO(unittest.TestCase):
    # NOTE: we do everything in one big bunch here, while splitting it up would be better
    # NOTE: due to the low amount of things to actually test (other than DTO defaults) there is no real point in splitting it up
    def test_people_DTO(self):
        # NOTE: this code is less clean, I could not immediately figure out a way to parameterize this without copying a block of text in the code
        with open("test_resources/people.json", "r") as people_json:
            people = json.load(people_json)

        for person_dict in people:
            with self.subTest(person_dict=person_dict):
                person = Person(**person_dict)

                # NOTE: we are not going to check everything here, only the important bits, for brevity sake
                self.assertEqual(person._id, person_dict["_id"])
                self.assertEqual(person.index, person_dict["index"])
                self.assertEqual(person.has_died, person_dict["has_died"])
                self.assertEqual(person.phone, person_dict["phone"])
                self.assertEqual(person.eyeColor, person_dict["eyeColor"])
                self.assertEqual(person.name, person_dict["name"])
                self.assertEqual(person.friends, person_dict["friends"])
                self.assertEqual(person.favouriteFood, person_dict["favouriteFood"])

                # Check some of the extra things we implemented in the Person DTO
                self.assertEqual(person.friend_indeces, [friend["index"] for friend in person.friends])
                self.assertEqual(person.temp(), {"name": person.name, "age": person.age, "address": person.address, "phone": person.phone})
