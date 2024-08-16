people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Cho","house":"RavenClaw"}
]

# def f(person):
#     return person["name"]
# people.sort(key = f)

people.sort(key = lambda person: person["name"])

print(people)