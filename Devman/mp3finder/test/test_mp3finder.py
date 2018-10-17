from mp3finder import str_to_int


def test_str_to_int():
    assert str_to_int('1', '12', ['1', '2', '3']) == 12
    assert str_to_int('1', 12, ['1', '2', '3']) == 12
    assert str_to_int('1', None, ['1', '2', '3']) is None
    assert str_to_int('1', 'Not_in_list', ['2', '3', '4']) == 'Not_in_list'
    assert str_to_int('1', 'String_is_not_int', ['1']) == 'String_is_not_int'


