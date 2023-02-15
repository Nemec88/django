import requests


def pars_summary(id):
    half = 0
    mark = 0
    summary_list = [{}]
    list_event = ['Goal', 'Yellow Card', 'Substitution']
    result_summary_list = []
    url_symmary = f'https://d.flashscore.com/x/feed/df_sui_1_{id}'
    response = requests.get(url_symmary, headers={
        "x-fsign": "SW9D1eZo"})  # Передаем ключь
    res = (response.text).split('¬')

    for i in res[:-2]:
        key = i.split('÷')[0]
        value = i.split('÷')[1]
        if 'AC' in key:
            half += 1
        elif '~' in key:
            summary_list.append({key: [value, half]})
        elif summary_list[-1].get(key):
            summary_list[-1][key].append(value)
        else:
            summary_list[-1].update({key: [value]})
    # for t in summary_list:
    #     print(t)

    for i in list_event:
        for z in range(1, 3):
            for e in summary_list:
                if i in e.get('IK', 'No')[0] and e.get('~III')[1] == z:
                    commanda = e.get('IA')
                    event = e.get('IK', 0)
                    t = e.get('IB', 0)
                    player = e.get('IF', 0)
                    number_time = e.get('~III', 0)[1]
                    result_summary_list.append(event + t + player)
                elif '~MIT' in e and mark == 5:
                    ref = e.get('MIV')[0]
                    country_ref = e.get('MIV')[3]
                    result_summary_list.append(['REFEREE', ref, country_ref])
            mark += 1

    # return result_summary_list

    # for t in result_summary_list:
    #     print(t)



    # for n in range(len(list_event)):
    #     for i in summary_list[1:]:
    #         # print(i)
    #         if list_event[n] in i.get('IK', 'No')[0] and i.get('~III')[1] == 1 and i.get('IA')[0] == '1' \
    #                 or list_event[n] in i.get('IK', 'No')[0] and i.get('~III')[1] == 2 and i.get('IA')[0] == '1':                                         # События первого тайма
    #             commanda = i.get('IA')
    #             event = i.get('IK', 0)
    #             t = i.get('IB', 0)
    #             player = i.get('IF', 0)
    #             number_time = i.get('~III', 0)[1]
    #             result_summary_list_1.append(commanda + event + t + player)
    #         elif list_event[n] in i.get('IK', 'No')[0] and i.get('~III')[1] == 2 and i.get('IA')[0] == '2'\
    #                 or list_event[n] in i.get('IK', 'No')[0] and i.get('~III')[1] == 1 and i.get('IA')[0] == '2':                                       # События второго тайма
    #             commanda = i.get('IA')
    #             event = i.get('IK', 0)
    #             t = i.get('IB', 0)
    #             player = i.get('IF', 0)
    #             number_time = i.get('~III', 0)[1]
    #             result_summary_list_2.append(commanda + event + t + player)
    #         elif '~MIT' in i and mark == 0:                                                                             # MATCH INFORMATION
    #             ref = i.get('MIV')[0]
    #             country_ref = i.get('MIV')[3]
    #             result_summary_list_3.append([33, ref, country_ref])
    #             mark += 1

    # return result_summary_list_1, result_summary_list_2, result_summary_list_3
    # result_summary_list = result_summary_list_1 + result_summary_list_2 + result_summary_list_3
    # print(result_summary_list_1)
    # print()
    # print(result_summary_list_2)
    # print()
    # print(result_summary_list_3)




    # for t in summary_list:
    #     print(t)


    # for el in summary_list:
    #     if el.get('AC'):
    #         half += 1
    #     elif '~III' in el:
    #         commanda = el.get('IA')
    #         event = el.get('IK', 0)
    #         t = el.get('IB', 0)
    #         player = el.get('IF', 0)
    #         number = el.get('IA', 0)
    #         if result_summary_list[int(*commanda) -1][0].get(event[0]):                                                 # Значение есть
    #             result_summary_list[int(*commanda) -1][0][event[0]].append([*commanda, event, *t, *player, *number])
    #         else:
    #             result_summary_list[int(*commanda) -1][0][event[0]] = [*commanda, event, *t, *player, *number]
    #     elif '~MIT' in el:
    #         result_summary_list[2].append(el)

    # print(result_summary_list)


    # for z in result_summary_list:
    #     print(z)






    # for el in summary_list:
    #     # print(el.get('IA'))
    #     if el.get('IA') == ['1']:
    #         result_summary_list[0].append(el)
    #     elif el.get('IA') == ['2']:
    #         result_summary_list[1].append(el)
    #     elif el.get('~MIT') == ['REF']:
    #         result_summary_list[2].append(el)
    #
    # print(result_summary_list)


    # for z in result_summary_list:
    #     print(z)
    #     print()


if __name__ == '__main__':
    pars_summary('r53uxoKR')
