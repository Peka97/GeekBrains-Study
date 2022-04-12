while True:
    duration = int(input('Введите число: '))
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    reply = ""
    if 0 < days:
        if days == 0 or 5 <= days <= 20 or days % 10 == 0 or 4 < days % 10 <= 9:
            reply += f"{days} дней"
        elif days == 1 or days % 10 == 1:
            reply += f"{days} день"
        elif 1 < days < 5 or 1 < days % 10 < 5:
            reply += f"{days} дня"
    if 0 < hours:
        if hours == 0 or 5 <= hours <= 20 or hours % 10 == 0 or 4 < hours % 10 <= 9:
            reply += f" {hours} часов"
        elif hours == 1 or hours % 10 == 1:
            reply += f" {hours} час"
        elif 1 < hours < 5 or 1 < hours % 10 < 5:
            reply += f" {hours} часа"
    if 0 < minutes:
        if minutes == 0 or 5 <= minutes <= 20 or minutes % 10 == 0 or 4 < minutes % 10 <= 9:
            reply += f" {minutes} минут"
        elif minutes == 1 or minutes % 10 == 1:
            reply += f" {minutes} минута"
        elif 1 < minutes < 5 or 1 < minutes % 10 < 5:
            reply += f" {minutes} минуты"
    if 0 < seconds:
        if seconds == 0 or 5 <= seconds <= 20 or seconds % 10 == 0 or 4 < seconds % 10 <= 9:
            reply += f" {seconds} секунд"
        elif seconds == 1 or seconds % 10 == 1:
            reply += f" {seconds} секунда"
        elif 1 < seconds < 5 or 1 < seconds % 10 < 5:
            reply += f" {seconds} секунды"
    print(reply)

