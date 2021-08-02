from .dto.company import Company

import json

class Companies:
    def __init__(self, file_location: str):
        self.list = self.__populate(file_location)

    # TODO: do this in-place?
    def __populate(self, file_location: str) -> list[Company]:
        with open(file_location, 'r') as companies_file:
            return [Company(**c) for c in json.load(companies_file)]

    def get_company_by_name(self, name: str) -> Company:
        for company in self.list:
            if company.company == name:
                return company
        else:
            raise Exception("No such company exists")
