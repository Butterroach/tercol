if __name__ == "__main__":
    import __init__ as t

    for hue in range(360):
        try:
            print(t.hsv(hue, 100, 100, "tercol"), end="\r")
        except KeyboardInterrupt:
            break
    print(t.red("Some red text"))
    print(t.bgred("Some text with a red background"))
    print(t.rainbowtext("Some rainbow text"))
    print(
        t.black("█"),
        t.red("█"),
        t.green("█"),
        t.yellow("█"),
        t.blue("█"),
        t.magenta("█"),
        t.cyan("█"),
        t.white("█"),
    )
    print(
        t.gray("█"),
        t.hexa(0xFF5C5C, "█"),
        t.hexa(0xAFFF00, "█"),
        t.hexa(0xFFFFAF, "█"),
        t.hexa(0x3B78FF, "█"),
        t.hexa(0xA964B5, "█"),
        t.hexa(0xAFFFFF, "█"),
        t.white("█"),
    )
