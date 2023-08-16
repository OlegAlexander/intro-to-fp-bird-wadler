units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def convert2(n: int) -> str:
    match divmod(n, 10):
        case (0, u): return units[u - 1]
        case (1, u): return teens[u]
        case (t, 0): return tens[t - 2]
        case (t, u): return tens[t - 2] + "-" + units[u - 1]
        case _: return "error"


def convert3(n: int) -> str:
    match divmod(n, 100):
        case (0, t): return convert2(t)
        case (h, 0): return units[h - 1] + " hundred"
        case (h, t): return units[h - 1] + " hundred and " + convert2(t)
        case _: return "error"


def convert6(n: int) -> str:
    match divmod(n, 1000):
        case (0, h): return convert3(h)
        case (m, 0): return convert3(m) + " thousand"
        case (m, h): return convert3(m) + " thousand" + link(h) + convert3(h)
        case _: return "error"


def link(h: int) -> str:
    return " and " if h < 100 else " "


def convert(n: int) -> str:
    assert 0 < n < 1_000_000, f"{n} is out of range 1 - 999,999"
    return convert6(n)
