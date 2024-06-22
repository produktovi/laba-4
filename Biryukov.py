from enum import Enum
from abc import abstractmethod
class TelephoneDictionary():
    def __init__(self):
        self.dictionary = {}
    def Add_abonent(self, name: str, telephone: str):
        self.dictionary[name] = telephone
        print (f'Абонент {name}  добавлен')
    def Edit_abonent(self, name: str, telephone: str):
        if telephone:
            self.dictionary[name] = telephone
            print(f'Номер телефона абонента {name} изменён')
        else:
            print(f"Абонента {name} не существует")
    def lookup_abonent(self, name: str):
        telephone = self.dictionary.get(name, None)
        if telephone:
            print(f"У абонента {name} номер телефона {telephone}")
        else:
            print(f"Абонента {name} нет")
    def delete_abonent(self, name: str):
        self.dictionary.pop(name)
        print(f'Абонент {name} удалён')
    def __str__(self):
        ret_dict = ""
        for key, value in self.dictionary.items():
            ret_dict += f'{key}: {value}\n'
        return ret_dict
abonents = TelephoneDictionary()
abonents.Add_abonent("Илья", "+7-956-465-23-78")
abonents.Add_abonent("Андрей", "+7-967-440-12-84")
abonents.Add_abonent("Вова", "+7-902-785-13-40")
print(abonents)
abonents.delete_abonent("Вова")
abonents.Edit_abonent("Влад", "+7-905-732-13-63")
abonents.lookup_abonent("Влад")
print(abonents)