for perc in range(0, 101):
    if perc == 0 or 5 <= perc <= 20 or perc % 10 == 0 or 4 < perc % 10 <= 9:
        print(f"{perc} процентов")
    elif perc == 1 or perc % 10 == 1:
        print(f"{perc} процент")
    elif 1 < perc < 5 or 1 < perc % 10 < 5:
        print(f"{perc} процента")