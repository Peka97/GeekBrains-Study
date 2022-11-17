def currency_rates(x, lst):
    for idx, text in enumerate(lst):
        if text == x.lower() or text == x.upper():
            return text, lst[idx + 1]
    return None


def currency_rates_sys(argv, lst):
    program, *args = argv
    for idx, text in enumerate(lst):
        if text == args[0].lower() or text == args[0].upper():
            print(f"{text} {lst[idx + 1]}")
            return text, lst[idx + 1]
    return None
