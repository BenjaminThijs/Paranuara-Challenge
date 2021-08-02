from .dto.person import Person
from .exceptions import NoSuchNameException

import json

class People:
    def __init__(self, file_location: str):
        self.list = self.__populate(file_location)

    def __getitem__(self, index: int) -> Person:
        return self.list[index]

    # TODO: do this in-place?
    def __populate(self, file_location: str) -> list[Person]:
        with open(file_location, 'r') as people_file:
            return [Person(**c) for c in json.load(people_file)]

    def get_employees(self, company_id: int) -> list[Person]:
        # TODO: just make it a generator instead?
        # cast it to list to prevent issues with not expecting generator
        if type(company_id) is not int:
            raise TypeError(f"company id should be an integer, not '{type(company_id)}'")
        
        return list(filter(lambda p: p.company_id == company_id, self.list))

    def get_person_by_name(self, name: str) -> Person:
        for person in self.list:
            if person.name == name:
                return person
        else:
            raise NoSuchNameException("No such person exists")
