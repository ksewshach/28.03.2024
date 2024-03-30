# 3.Напишите функцию, которая принимает два аргумента - строку и словарь слов для замены. Функция должна заменить все указанные слова в строке и вернуть измененную строку.
import random
def task_three(string, **kwargs):
    words:list = string.split(' ')
    kwargs_list:list = list(kwargs.values())
    i:int = 0
    for word in words:
        while (i+1) <= len(words):
            words[i] = kwargs_list[random.randint(0, min(len(words), len(kwargs_list)))-1]
            i+=1
    words = ' '.join(words)
    return words
dictionary:dict = dict(one="жёлтый", two="машина", three="водичка", four="ничего", five="слово", six="коза", seven="дерево")
string:str = input('Введите строку для замены: ')
print(f'Введённая строка: {string}\nНовая строка: {task_three(string, **dictionary)}')


# 4. Создайте функцию, которая принимает произвольное количество именованных аргументов и выводит их в порядке возрастания ключей.
def task_four(**kwargs):
    new_list = sorted(kwargs.values())
    return new_list
print(f'Отсортированный список: {task_four(g="4", u="63", i="865", d="12", n="0", k="76", l="3")}')
    