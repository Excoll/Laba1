# 1. Створити список із 10 int та 10 str
main_list = [5, 12, 3, 8, 25, 1, 16, 7, 30, 2,
             "яблуко", "банан", "ананас", "виноград", "київ",
             "будинок", "гора", "дерево", "зима", "літо"]

# 2. Розділяємо список на числа та строки
int_list = [x for x in main_list if isinstance(x, int)]
str_list = [x for x in main_list if isinstance(x, str)]

# 3. Сортування чисел по зростанню
int_list_sorted = sorted(int_list)

# 4. Сортування строк від "а" до "я" (алфавітно)
str_list_sorted = sorted(str_list, key=str.lower)

# 5. Об’єднати їх у один відсортований список
sorted_main_list = int_list_sorted + str_list_sorted

# 6. Знайти всі елементи, кратні двом
even_list = [x for x in int_list if x % 2 == 0]

# 7. Створити список зі строк у капсі
str_caps_list = [x.upper() for x in str_list]

# 8. Вивести всі списки
print("Головний відсортований список:", sorted_main_list)
print("Список лише парних чисел:", even_list)
print("Список строк у капсі:", str_caps_list)