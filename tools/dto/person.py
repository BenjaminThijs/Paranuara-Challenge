from dataclasses import dataclass

@dataclass
class Person:
    _id: str
    index: int
    guid: str
    has_died: bool
    balance: str
    picture: str
    age: int
    eyeColor: str
    name: str
    gender: str
    company_id: int
    email: str
    phone: str
    address: str
    about: str
    registered: str
    tags: list[str]
    friends: list[dict]
    greeting: str
    favouriteFood: str

    @property
    def friend_indeces(self):
        return [f["index"] for f in self.friends]

    # TODO: change name
    def temp(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "phone": self.phone
        }
