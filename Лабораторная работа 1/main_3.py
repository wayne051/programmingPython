list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
n_players=(len(list_players))
# TODO Разделите участников на две команды
half_length = len(list_players) // 2
one = list_players[:half_length]
two = list_players[half_length:]
print("Общее кол-во игроков : ", n_players)
print ("Первая команда", one)
print ("Вторая команда", two)