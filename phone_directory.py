# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


__path__ = 'phoneDirectory.txt'


def reading(path):
    phoneDirectory = []
    with open(path, 'r', encoding='utf-8') as file:
        i = 1
        for line in file:
            list_ = line.split()
            dict_ = {
                "id" : i,
                "last_name" : list_[0],
                "first_name" : list_[1],
                "second_name" : list_[2],
                "number_phone" : list_[3],
        }   
            
            phoneDirectory.append(dict_)
            i += 1
    return phoneDirectory


def printing(phoneDirectory):
    for i in phoneDirectory:
        print(*(f"{v}" for v in i.values()))
    return None


def add_contact(path):
    with open(path, 'a', encoding='utf-8') as file:
        print("Введите ФИО, тел, резделенные пробелами")
        s = input()
        while len(s.split()) < 4:
            print("Вы ввели некорректные данные!!!")
            s = input("Введите ФИО, тел, резделенные пробелами ")
        file.write("\n" + s)

def find_contact(phoneDirectory):
    print("Введите критерии для поиска контакта:")
    criteria = {}
    criteria["last_name"] = input("Фамилия: ")
    criteria["first_name"] = input("Имя: ")

    found_contact = find_contact_by_criteria(phoneDirectory, criteria)
    if found_contact:
        print("Контакт найден")
        printing(found_contact)
        update_option = input("Хотите изменить этот контакт? (да/нет): ")
        if update_option.lower() == "да":
            new_data = {
            "last_name": input("Новая фамилия: "),
            "first_name": input("Новое имя: "),
            "second_name": input("Новое отчество: "),
            "number_phone": input("Новый номер телефона: "),
            }
            update_contact_in_file(__path__, found_contact, new_data)
    else:
        print("Контакт не найден")
            

def update_contact_in_file(path, old_data, new_data): # путь, словарь, словарь
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    updated_lines = []
    result_dict = {k: v for d in old_data for k, v in d.items()}
    for line in lines:
        contact_info = line.split()
        if (contact_info[0] == result_dict["last_name"] and 
            contact_info[1] == result_dict["first_name"] and 
            contact_info[2] == result_dict["second_name"] and 
            contact_info[3] == result_dict["number_phone"]):
                updated_line = f"{new_data['last_name']} {new_data['first_name']} {new_data['second_name']} {new_data['number_phone']} \n"
                updated_lines.append(updated_line)
        else:
                updated_lines.append(line)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)
        
    
def find_contact_by_criteria(phoneDirectory, criteria):
    found_contacts = []
    for contacts in phoneDirectory:
        matches_criteria = all(
            key in contacts and contacts[key] == value for key, value in criteria.items()
        )
        if matches_criteria:
            found_contacts.append(contacts)
        return found_contacts


def copy_contact(from_path, to_path, line_number):
    with open(from_path, 'r', encoding='utf-8') as from_file:
        lines = from_file.readlines()
    with open(to_path, 'a', encoding='utf-8') as to_file:
        to_file.write(lines[line_number-1])


def main():

    while True:
        print("Что хотите сделать?")
        print("1: Вывести данные")
        print("2: Записать новый контакт")
        print("3: Найти контакт")
        print("4: Скопировать контакт в другой файл")
        print("0: Выйти")
        x = input()
        phoneDirectory = (reading(__path__))
        
        if x == "0":
            break
        elif x == "1":
            printing(phoneDirectory)
        elif x == "2":
            add_contact(__path__)
        elif x == "3":
            find_contact(phoneDirectory)
        elif x == "4":
            print("Введите номер строки для копирования:")
            line_number = int(input())
            copy_contact(__path__, 'newPhoneDirectory.txt', line_number)
        else:
            print("неверная команда")

if __name__ == "__main__":
    main()