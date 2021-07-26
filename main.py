from flask import Flask
import json

app = Flask(__name__)

@app.get("/company/<company>")
def company(company: str):
    with open('resources/companies.json', 'r') as companies_file:
        try:
            company_id = next(filter(lambda c: c['company'] == company, json.load(companies_file)))["index"]
        except StopIteration:
            return None

    with open('resources/people.json', 'r') as people_file:
        people = filter(lambda p: p["company_id"] == company_id, json.load(people_file))

    employees = list(people)
    code = 200 if len(employees) > 0 else 204
    return ({'employees': employees}, code)

@app.get("/mutualfriends/<person1>/<person2>")
def common(person1: str, person2: str):
    with open("resources/people.json", "r") as people_json:
        people = json.load(people_json)

    person1 = next(filter(lambda p: p["name"] == person1, people))
    person2 = next(filter(lambda p: p["name"] == person2, people))

    friends = lambda p: [f["index"] for f in p["friends"]]

    # mutual friends indexes
    mutual_friends = set(friends(person1)).intersection(friends(person2))

    # mutual friends
    mutual_friends = [people[i] for i in mutual_friends]

    # mutual friends that have brown eyes and are alive
    mutual_friends = filter(lambda p: p["eyeColor"] == "brown" and p["has_died"] is False, mutual_friends)

    cast = lambda p: {"name": p["name"], "age": p["age"], "address": p["address"], "phone": p["phone"]}

    return {
        "person1": cast(person1),
        "person2": cast(person2),
        "mutual_friends": [m for m in mutual_friends]
    }, 200

@app.get("/person/<person>")
def person(person: str):
    with open("resources/people.json", "r") as people_json:
        people = json.load(people_json)

    def get_person():
        return next(filter(lambda p: p["name"] == person, people))

    person = get_person()

    fruits = [
        "orange", "apple", "banana", "strawberry"
    ]

    vegetables = [
        "cucumber", "beetroot", "carrot", "celery"
    ]

    return {
        "username": person["name"],
        "age": person["age"],
        "fruits": [f for f in person["favouriteFood"] if f in fruits],
        "vegetables": [f for f in person["favouriteFood"] if f in vegetables]
    }, 200

if __name__ == "__main__":
    app.run()
