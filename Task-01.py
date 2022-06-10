# Задача 1. Работа с файлом

def action(ask, answer='Неверный ввод. Пожалуйста, введите \'да\' или \'нет\'.', trays=3):
    while trays:
        ask_enter = input(ask)
        if ask_enter.lower() == 'да':
            return 1
        elif ask_enter.lower() == 'нет':
            return 0
        else:
            trays -= 1
            print(answer)
            print('Осталось попыток:', trays)
    print('Ввод завершен')


print(action('Вы действительно хотите выйти? '))


print(action('Вы хотите сохранить документ? ', answer='Чего-чего?'))


print(action('Вы действительно хотите выйти? ', trays=5))
