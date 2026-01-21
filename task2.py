# TODO Напишите функцию find_common_participants
def find_common_participants (list1, list2, r = ","):
    list1 = set(participants_first_group.split(r))
    list2 = participants_second_group.split(r)
    common_participants = list(list1.intersection(list2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group, r = "|")
print("Общие участники:", common)
