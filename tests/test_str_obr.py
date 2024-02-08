from greb import str_obr


def test_str_obr():
    assert str_obr("a", "aabhgajhbb") == 2


def test_str_obr2():
    assert str_obr("a", "bhgjhbb") == 0
