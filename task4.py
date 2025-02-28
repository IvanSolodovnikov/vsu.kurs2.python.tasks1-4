units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
         "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят",
        "восемьдесят", "девяносто"]
hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот",
            "восемьсот", "девятьсот"]
thousands = ["", "тысяча", "тысячи", "тысяч"]

def number_to_words(num):
    if num == 0:
        return "ноль"

    def convert_chunk(n):
        if n == 0:
            return ""
        elif n < 10:
            return units[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        elif 20 <= n < 100:
            return tens[n // 10] + " " + convert_chunk(n % 10)
        else:
            return hundreds[n // 100] + " " + convert_chunk(n % 100)

    def get_thousand_form(n):
        if 10 <= n % 100 < 20:
            return thousands[3]
        elif n % 10 == 1:
            return thousands[1]
        elif 2 <= n % 10 <= 4:
            return thousands[2]
        else:
            return thousands[3]

    if num < 1000:
        return convert_chunk(num).strip()
    else:
        thousand_chunk = num // 1000
        remainder = num % 1000
        thousand_word = convert_chunk(thousand_chunk) + " " + get_thousand_form(thousand_chunk)
        remainder_word = convert_chunk(remainder)
        return (thousand_word + " " + remainder_word).strip()

if __name__ == '__main__':
    number = 217045
    print(number_to_words(number))