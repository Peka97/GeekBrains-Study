def count_substrings(word: str) -> str:
    result = set()
    for i in range(len(word)):
        for j in range(len(word)):
            result.add(hash(word[i:j]))
    return f"Количество различных подстрок в этой строке: {len(result)}"


if __name__ == '__main__':
    # Задача не настроена на надежность защиты, потому воспользовался встроенной функцией hash()
    print(count_substrings('papa'))
