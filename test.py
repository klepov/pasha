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


def create_schedule(day_on_semestr):
    """
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
 \
 \
 \
 \
            # need_object =['Mat_log',52],\
    #          ['sys_prog',127],\
    #          ['philosof',48],\
    #          ['python',153],\
    #          ['obj',34],\
    #          ['gavr',76],\
    #          ['fiz-ra',32],\
    #          ['angl',32],\
    #          ['econom',72],\
    #          ['pravo',76],\




    name = ''
    num = 0
    for i in range(len(need_object)):
        name = need_object[i][0]
        hours = need_object[i][1]

        object = [name, hours]

        prepared_schedule = generate_object_for_day(object, semestr)

    # print(prepared_schedule)

    return prepared_schedule


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
            return hours_need, semester


def equals_group(group1, group2):
    """
        сравнение расписания на следующей день с новой группой.
        возвращяет True если есть совпадение
    """
    len_group_1 = len(group1[1])
    len_group_2 = len(group2[1])

    if len_group_1 == len_group_2:
        false = 0
        true = True

        for in_day_couple in range(len_group_1):
            for in_couple in range(4):
                checking_group1 = group1[1][in_day_couple][in_couple]
                checking_group2 = group2[1][in_day_couple][in_couple]

                if checking_group1 == 0 and checking_group2 == 0:
                    continue
                elif checking_group1 == checking_group2:
                    # print(checking_group1," equally ",checking_group2)

                    group2[1][in_day_couple] = random.sample(group2[1][in_day_couple],len(group2[1][in_day_couple]))
                    true = True

                else:
                    # print(" false ")
                    true = False



def compare_date_with_schedule():
    """
    метод склеивает расписание с датой
    и возвращяет результат
    :return:
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


sem = create_semester(129)
sem2 = create_semester(129)

print(sem)

sem_with_obj = create_schedule(sem)
sem_with_obj2 = create_schedule(sem2)

equals_group(sem_with_obj, sem_with_obj2)
print(sem_with_obj)
print(sem_with_obj2)
#
# print(sem_with_obj,'\n',sem_with_obj2,'\n','\n',)
#
# for i in range(len(sem_with_obj[1])):
#     print(sem_with_obj[1][i])
#
#
# calendar_semester = 6
# compare_date_with_sc
()





