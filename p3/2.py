# TODO Напишите функцию find_common_participants
def find_common_participants(str_list1, str_list2, delimeter=","):
    list1 = set(str_list1.split(delimeter))
    list2 = set(str_list2.split(delimeter))
    result_list = list(list1.intersection(list2))
    result_list.sort()
    return result_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
