from .sa import Colors


def test_sa():
    assert Colors.WHITE.hex == "f2f2e3"
    assert Colors.WHITE_LIGHT.hex == "f9f9f1"
    assert Colors.WHITE_DARK.hex == "b9b1bc"
    assert Colors.WHITE_DARKER.hex == "7f7094"

    assert Colors.BLACK.hex == "241b30"
    assert Colors.BLACK_LIGHT.hex == "3a3245"
    assert Colors.BLACK_DARK.hex == "1a1322"
    assert Colors.BLACK_DARKER.hex == "0f0b14"

    assert Colors.CYAN.hex == "00fbfd"
    assert Colors.CYAN_DARK.hex == "00b0b1"
    assert Colors.CYAN_DARKER.hex == "126671"
    assert Colors.CYAN_DARKEST.hex == "1b4151"

    assert Colors.MAGENTA.hex == "ff00f6"
    assert Colors.MAGENTA_DARK.hex == "b300ad"
    assert Colors.MAGENTA_DARKER.hex == "6c0e6f"
    assert Colors.MAGENTA_DARKEST.hex == "481550"

    assert Colors.PURPLE.hex == "aa54f9"
    assert Colors.PURPLE_DARK.hex == "6e29ad"
    assert Colors.PURPLE_DARKER.hex == "49226f"
    assert Colors.PURPLE_DARKEST.hex == "371f50"

    assert Colors.BLUE.hex == "55a8fb"
    assert Colors.BLUE_DARK.hex == "2a6daf"
    assert Colors.BLUE_DARKER.hex == "274470"
    assert Colors.BLUE_DARKEST.hex == "263050"

    assert Colors.YELLOW.hex == "f9f972"
    assert Colors.YELLOW_DARK.hex == "adad3e"
    assert Colors.YELLOW_DARKER.hex == "696437"
    assert Colors.YELLOW_DARKEST.hex == "474034"

    assert Colors.RED.hex == "e60a70"
    assert Colors.RED_DARK.hex == "9a0048"
    assert Colors.RED_DARKER.hex == "5f0e3c"
    assert Colors.RED_DARKEST.hex == "421536"

    assert Colors.GREEN.hex == "0ae4a4"
    assert Colors.GREEN_DARK.hex == "00986c"
    assert Colors.GREEN_DARKER.hex == "125a4e"
    assert Colors.GREEN_DARKEST.hex == "1b3b3f"
