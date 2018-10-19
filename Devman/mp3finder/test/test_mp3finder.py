from mp3finder import str_to_int, find_all_tracks, tags_for_songs, get_song_info_from_mp3_tags, \
    filter_tracks, format_discography, print_result
import song_collection
import os


path = os.path.join('test', os.path.split(str(find_all_tracks()[0]))[-1])
mp3_file = os.path.split(str(find_all_tracks()[0]))[-1]
tags = get_song_info_from_mp3_tags(path)
song_collection = song_collection.song_list
discography = format_discography(filter_tracks(song_collection, 'Nine Inch Nails'))


def test_str_to_int():
    assert str_to_int('1', '12', ['1', '2', '3']) == 12
    assert str_to_int('1', 12, ['1', '2', '3']) == 12
    assert str_to_int('1', None, ['1', '2', '3']) is None
    assert str_to_int('1', 'Not_in_list', ['2', '3', '4']) == 'Not_in_list'
    assert str_to_int('1', 'String_is_not_int', ['1']) == 'String_is_not_int'


def test_find_all_tracks():
    assert mp3_file == 'test_file.mp3'
    assert isinstance(find_all_tracks(), list)


def test_get_song_info_from_mp3_tags():
    assert isinstance(tags, dict)
    assert tags.get('artist')[:8] == 'Megadeth'
    assert tags.get('title')[:8] == 'Crush Em'
    assert tags.get('path') == path


def test_tags_for_songs():
    isinstance(tags_for_songs([path]), list)

# Monkeypatching!


def test_filter_tracks():
    isinstance(filter_tracks([tags], tags.get('artist')), list)
    assert filter_tracks([tags], tags.get('artist')) == [tags]
    assert filter_tracks([tags], 'test') != [tags]


def test_format_discography():
    assert [key for key in discography] == ['The Slip']
    assert discography['The Slip'][0]['track'] < discography['The Slip'][1]['track']

