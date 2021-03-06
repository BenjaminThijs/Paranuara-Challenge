from tools.exceptions import NoSuchNameException
from tools.companies import Companies
from tools.people import People

from flask import Flask

companies = Companies("resources/companies.json")
people = People("resources/people.json")
app = Flask(__name__)

@app.get("/company/<company>")
def get_employees_for_company(company: str):
    try:
        company_id = companies.get_company_by_name(name=company).index
        employees = people.get_employees(company_id=company_id)

        code = 200 if len(employees) > 0 else 204
    except:
        code = 204

        employees = []

    # NOTE: since it wasn't mentioned how to return these employees
    # NOTE: we simply return their names
    return ({'employees': [e.name for e in employees]}, code)

@app.get("/mutualfriends/<person1_name>/<person2_name>")
def get_mutual_friends(person1_name: str, person2_name: str):
    try:
        person1, person2 = people.get_person_by_name(person1_name), people.get_person_by_name(person2_name)
    except NoSuchNameException:
        return {"error": "no such name"}, 204

    # mutual friends indexes
    mutual_friends = set(person1.friend_indeces).intersection(person2.friend_indeces)

    # mutual friends
    mutual_friends = [people[i] for i in mutual_friends]

    # mutual friends that have brown eyes and are alive (and are not one of the two people)
    mutual_friends = filter(lambda p: p.eyeColor == "brown" and p.has_died is False and p not in (person1, person2), mutual_friends)

    return {
        "person1": person1.temp(),
        "person2": person2.temp(),
        "mutual_friends": [m.name for m in mutual_friends]  # TODO: what to show here?
    }, 200

@app.get("/person/<name>")
def get_person_info(name: str):
    try:
        person = people.get_person_by_name(name=name)
    except NoSuchNameException:
        return {"error": "no such name"}, 204

    fruits = [
        "orange", "apple", "banana", "strawberry"
    ]

    vegetables = [
        "cucumber", "beetroot", "carrot", "celery"
    ]

    return {
        "username": person.name,
        "age": person.age,
        "fruits": [f for f in person.favouriteFood if f in fruits],
        "vegetables": [f for f in person.favouriteFood if f in vegetables]
    }, 200

if __name__ == "__main__":
    app.run()
