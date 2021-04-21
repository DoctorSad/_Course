my_list = [
    "first",
    {"name": "Max"},
    {"country": "Ukraine", "cities": ["Kiev", "Kharkiv", "Odesa", "Dnipro"]},
]
print("\n1. Using standart copy\n")
print("Original source", my_list, sep="\n")

# При копировании коллекции создается новая коллекция
# но объекты коллекции не создаются заново, а просто ссылаются на существующие
my_list_copy = my_list.copy()

my_list_copy[0] = "copy"
my_list_copy[1]["name"] = "Jane"
my_list_copy[2]["cities"].sort()
my_list_copy.append({"some": "append"})


print("Copy", my_list_copy, sep="\n")
print("Original", my_list, sep="\n")

# Для того, чтобы это исправить необходимо использовать глубокое копирование,
# т.е. копировать не только коллекцию, а и все ее значения
from copy import deepcopy

my_list = [
    "first",
    {"name": "Max"},
    {"country": "Ukraine", "cities": ["Kiev", "Kharkiv", "Odesa", "Dnipro"]},
]
print("\n2. Using deepcopy\n")
print("Original source", my_list, sep="\n")

my_list_copy = deepcopy(my_list)

my_list_copy[0] = "copy"
my_list_copy[1]["name"] = "Jane"
my_list_copy[2]["cities"].sort()
my_list_copy.append({"some": "append"})

print("Copy", my_list_copy, sep="\n")
print("Original", my_list, sep="\n")
