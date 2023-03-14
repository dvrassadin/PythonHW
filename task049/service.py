def load_data(file_name: str) -> dict:
    contacts = {}
    with open(file_name, "r") as file:
        for el in file.read().split("\n"):
            contact = el.split(", ")
            if contact != [""]:
                contacts[contact[0]] = contact[1]
    return contacts


def print_contacts(contacts: dict):
    for count, key in enumerate(sorted(contacts)):
        print(f"{count + 1}\t{key}\t{contacts[key]}")


def find_contacts(contacts: dict, text: str):
    for key in sorted(contacts):
        if key.lower().__contains__(text.lower()) or contacts[key].replace(" ", "").replace("-", "").__contains__(text):
            print(f"{key}\t{contacts[key]}")


def add_data(file_name: str, name: str, number: str):
    with open(file_name, "a") as file:
        file.writelines(f"{name}, {number}\n")
