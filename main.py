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


