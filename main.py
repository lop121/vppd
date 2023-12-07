"""vvpd 4"""


def lighten(color: str, percent: int) -> str:
    """света делаем"""
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
    r = min(255, r + r * percent // 100)
    g = min(255, g + g * percent // 100)
    b = min(255, b + b * percent // 100)

    new_color = f"#{r:02X}{g:02X}{b:02X}"
    print_colored_text("Я очень люблю ВВПД!", new_color)
    return new_color


def darken(color: str, percent: int) -> str:
    '''даем тени'''
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
    r = max(0, r - r * percent // 100)
    g = max(0, g - g * percent // 100)
    b = max(0, b - b * percent // 100)

    new_color = f"#{r:02X}{g:02X}{b:02X}"
    print_colored_text("Я очень люблю ВВПД!", new_color)
    return new_color


def print_colored_text(text: str, color: str) -> None:
    '''текст вывод терминал'''
    print(
        f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};"
        f"{int(color[5:], 16)}m{text}\033[0m"
    )


def main() -> None:
    """Main function"""
    print('Чтобы выйти из программы, пропишите - #000000 0')
    while True:
        print('Пример: #112233 100')
        try:
            color, procent = input('Введите нужные значения через пробел: ').split()
            if color == '#000000' and int(procent) == 0:
                break
        except ValueError:
            print('Что-то не так...')
            continue
        try:
            choice = input('Что нужно сделать?\n'
                           '(1) Затемнить текст\n'
                           '(2) Осветлить текст\n'
                           'Ваш выбор: ')
            if choice == '1':
                darken(color, int(procent))
            elif choice == '2':
                lighten(color, int(procent))
            else:
                print('Что-то не так...')
        except ValueError:
            print('Что-то не то...')


if __name__ == '__main__':
    main()
