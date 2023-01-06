import re


def generator_numbers(string=""):
    list_str = string.split(" ")
    l = len(list_str)
    i = 0
    while i < l:
        if re.search(r"\d+", list_str[i]):
            m = re.search(r"\d+", list_str[i])
            start = m.start()
            end = m.end()
            res = int(m.string[m.start():m.end()])
            yield res
        i = i + 1


def sum_profit(string):
    sum = 0
    list_numb = generator_numbers(string)
    for i in list_numb:
        sum = sum + i
    return sum


print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))
