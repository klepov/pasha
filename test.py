# -*- coding: utf-8 -*-
import random

import calendar

__author__ = 'Dima'


def create_semester(count):
    """
    :param count: принимает количество дней в семестре
    :return: возвращяет пустой семестр
    """
    week_total = []

    countDayInSemester = count
    for week in range(countDayInSemester):
        week_total.append([])
        for couple_0 in range(1):
            week_total[week].append(couple_0)
            for couple_1 in range(1):
                week_total[week].append(couple_1)
                for couple_2 in range(1):
                    week_total[week].append(couple_2)
                    for couple_2 in range(1):
                        week_total[week].append(couple_2)

    prepair_semester = week_total
    return prepair_semester


def create_schedule(id_group,day_on_semestr):
    """
    :param id_group: принимает номер группы
    :param day_on_semestr: принимает созданный семестр
    :return: возвращяет заполненый предметами пары
    """
    semestr = day_on_semestr
    need_object = \
        ['philosof', 24], \
        ['angl', 16], \
        ['fiz-ra', 16], \
        ['Mat_log', 26], \
        ['econom', 36], \
        ['pravo', 38], \
        ['gavr', 38], \
        ['obj', 17], \
        ['sys_prog', 64], \
        ['python', 77], \



    name = ''
    num = 0
    for i in range(len(need_object)):
        name = need_object[i][0]
        hours = need_object[i][1]

        object = [name, hours]

        prepared_schedule = generate_object_for_day(object, semestr)

    # print(prepared_schedule)
    return  id_group,prepared_schedule


def generate_object_for_day(object, semester):
    """
    :param object: принимает кол-во пар предмета
    :param semester: принимает семестр
    :return: возвраящяет сгенерированый список с указанным предметом
    """

    hours_need = object[1]
    name_for_object = object[0]
    print(hours_need)

    for i in range(len(semester)):

        rand = random.randrange(4)

        point_on_day = semester[i][rand]

        if point_on_day != 0:

            while point_on_day != 0:

                # пока не будет 0, искать

                # проверка, если в этой ячеки место
                for i2 in range(4):

                    rand = i2
                    check = semester[i][rand]
                    # если есть пустая ячейка - поставить курсор туда
                    if check == 0:

                        semester[i][rand] = name_for_object
                        hours_need -= 1

                        # выходим из цикла
                        point_on_day = 0
                        break

                    # если нет - перети на следующий день
                    elif i2 == 3:
                        point_on_day = 0
                        break
        # если курсор на нуле - поставить предмет и отнять час
        elif point_on_day == 0:
            semester[i][rand] = name_for_object
            hours_need -= 1

        if hours_need == 0:
            return semester


def equals_group(list_group):
    """
        сравнение расписания на следующей день с новой группой.
        возвращяет True если есть совпадение
    """

    cheking  = False

    for i in range(len(list_group)):

        for i2 in range(len(list_group)):
            if i2 == i:
                continue
            for in_day_couple in range(129):
                for in_couple in range(4):
                    # print("in_couple ",in_couple," in_day_couple ", in_day_couple," i2 ", i2, " i ", i)
                    if list_group[i][in_day_couple][in_couple] == 0 \
                            and list_group[i2][in_day_couple][in_couple] == 0:
                        continue

                    elif list_group[i][in_day_couple][in_couple] \
                            == list_group[i2][in_day_couple][in_couple]:
                        # print(list_group[i][in_day_couple][in_couple])

                        list_group[i][in_day_couple] = random.sample(list_group[i][in_day_couple],len(list_group[i][in_day_couple]))
                        # print(list_group[i][in_day_couple][in_couple])

                        cheking = True


    return cheking


                # group2[1][in_day_couple] = random.sample(group2[1][in_day_couple],
                #                                          len(group2[1][in_day_couple]))
                # cheking = True




def compare_date_with_schedule(sem_with_obj):
    print(sem_with_obj)
    """
    метод склеивает расписание с датой
    :return: склееное расписание
    """
    count = 0
    for month in range(1, 7):
        days = calendar.monthrange(2015, month)  # узнаем сколько дней
        days = days[1] + 1  # счет с нуля
        for day in range(1, days):

            check = calendar.weekday(2015, month,
                                     day)  # узнать день недели. если больше 5(скипнуть/субботу.воскресение)
            if check == 5 or check == 6:
                print(" weekend ")
                continue
            else:
                print("год - 2015", " месяц - ", month, " день - ", day, "| пары -", sem_with_obj[1][count])
                count += 1


all_group = []
sem = create_semester(129)
sem2 = create_semester(129)
sem3 = create_semester(129)

sem_with_obj = create_schedule("32",sem)
sem_with_obj2 = create_schedule("36",sem2)
sem_with_obj3 = create_schedule("22",sem3)


all_group.append(sem_with_obj[1])
all_group.append(sem_with_obj2[1])
all_group.append(sem_with_obj3[1])



print(all_group)

i = equals_group(all_group)
while i:
    i = equals_group(all_group)

print(all_group)
# compare_date_with_schedule(sem_with_obj)





