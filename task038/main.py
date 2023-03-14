# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

import service as s

file_name = "task038/contacts.txt"

print("Contacts")
while True:
    action = input(
        "Enter the number of action:\n1 — Show all\n2 — Find\n3 — Add\n4 — Edit\n5 - Delete\n0 — Exit\n>>> ")
    if action == "0":  # Exit
        print()
        break
    elif action == "1":  # Show all contacts
        s.print_contacts(s.load_data(file_name))
        print()
    elif action == "2":  # Find contacts by name or by number
        text = input("Enter what to find: ")
        s.find_contacts(s.load_data(file_name), text)
        print()
    elif action == "3":  # Add contact
        first_name = input("Enter the first name: ")
        second_name = input("Enter the second name: ")
        number = input("Enter the number: ")
        s.add_data(file_name, first_name + " " + second_name, number)
        print()
    elif action == "4":  # Edit contact
        contacts = s.load_data(file_name)
        s.print_contacts(contacts)
        count = int(input("\nThe number of contact you want to edit: "))
        s.edit_contact(contacts, count - 1)
        s.save_data(file_name, contacts)
        print()
    elif action == "5":  # Delete contact
        contacts = s.load_data(file_name)
        s.print_contacts(contacts)
        count = int(input("\nThe number of contact you want to delete: "))
        s.delete_contact(contacts, count - 1)
        s.save_data(file_name, contacts)
        print()
    else:
        print("The number is incorrect.")
