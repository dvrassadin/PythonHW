def load_data(file_name: str) -> list:
    contacts = []
    with open(file_name, "r") as file:
        for el in file.read().split("\n"):
            if el != "":
                contacts.append(el.split(", "))
    return sorted(contacts)


def print_contacts(contacts: list):
    for count, el in enumerate(contacts):
        print(f"{count + 1}\t{el[0]}\t{el[1]}")


def find_contacts(contacts: list, text: str):
    count = 0
    for el in contacts:
        if el[0].lower().__contains__(text.lower()) or el[1].replace(" ", "").replace("-", "").__contains__(text):
            count += 1
            print(f"{count}\t{el[0]}\t{el[1]}")


def add_data(file_name: str, name: str, number: str):
    with open(file_name, "a") as file:
        file.writelines(f"\n{name}, {number}")


def save_data(file_name: str, contacts: list):
    with open(file_name, "w") as file:
        for el in contacts:
            file.write(f"\n{el[0]}, {el[1]}")


def delete_contact(contacts: list, index: int):
    if index < len(contacts):
        contacts.pop(index)
    else:
        print("There isn't a contacts with this number.")


def edit_contact(contacts: list, index: int):
    if index < len(contacts):
        action = input(
            "What do you want to edit:\n1 — First_name\n2 — Second name\n3 — Phone number\n0 — Exit\n>>> ")
        if action == "0":  # Exit
            return
        elif action == "1":  # First name
            new_first_name = input("Enter the new first name: ")
            second_name = contacts[index][0].split(" ")[1]
            contacts[index][0] = new_first_name + " " + second_name
        elif action == "2":  # Second name
            new_second_name = input("Enter the new second name: ")
            first_name = contacts[index][0].split(" ")[0]
            contacts[index][0] = first_name + " " + new_second_name
        elif action == "3":  # Phone number
            new_number = input("Enter the new phone number: ")
            contacts[index][1] = new_number
        else:
            print("The number is incorrect.")
    else:
        print("There isn't a contacts with this number.")
