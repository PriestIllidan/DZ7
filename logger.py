from datetime import datetime

def calc_logger(result):
    time = datetime.now().strftime('%d.%m.%y - %H:%M')
    with open('file.txt', 'a') as file:
        file.write(f'{result}, {time}\n')