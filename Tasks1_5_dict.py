# Создайте словарь содержащий данные о человеке. В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
# Выведите на экран все данные о человеке по ключам.
# Добавьте в словарь ключ и значение размера ноги.
# Удалите из словаря возраст.

person = {
    "name": "Alex",
    "age": 23,
    "gender": "man",
    "height": 192,
    "weight": 80
}

for key in person:
    print(person[key])

for key, value in person.items():
    print(key, value)


person["foot"] = 44
del person["age"]

print(person)