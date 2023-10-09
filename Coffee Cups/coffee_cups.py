def aroma(num):
    return (f"{' '* num}{'~ ' * 3}").rstrip()


def first_line_after_the_aroma(width, symbol):
    return f'{symbol * (width - 1)}'


def area_between_the_lines(width, num):
    return '|' + '~' * (width - (3 + num - 1)) + '|' + ' ' * (num - 1) + '|'


def line_with_the_text(width, num, text):
    symbols_needed = (width - (3 + num - 1) - len(text)) // 2
    return '|' + '~' * symbols_needed + text.upper() + '~' * symbols_needed + '|' + ' ' * (num - 1) + '|'


def base_of_glass(width, free_place):
    inside_glass_elements = width - (2 + free_place * 2)
    return ' ' * free_place + '\\' + '@' * inside_glass_elements + '/'


n = int(input())
sign_on_the_glass = input()
glass_width = 3 * n + 6
glass_height = 3 * n + 1

aroma = aroma(n)
first_top_line_and_middle_line = first_line_after_the_aroma(glass_width, "=")
between_the_lines = area_between_the_lines(glass_width, n)
text_line = line_with_the_text(glass_width, n, sign_on_the_glass)

[print(aroma) for _ in range(n)]
print(first_top_line_and_middle_line)
if n <= 3:
    print(text_line)
elif n > 3:
    rows = n - 3 + 1
    row_needed = (rows // 2) + 1
    for i in range(1, rows + 1):
        if i == row_needed:
            print(text_line)
            continue
        print(between_the_lines)

print(first_top_line_and_middle_line)
for i in range(n):
    print(base_of_glass(glass_width - n, i))
print(first_line_after_the_aroma(glass_width, "-"))
