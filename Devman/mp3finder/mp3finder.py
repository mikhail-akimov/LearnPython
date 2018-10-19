from tinytag import TinyTag
import os
import sys
from itertools import groupby


def find_all_tracks():
    """"Return list of all .mp3 in root_dir."""
    root_dir = os.getcwd()
    tracks = []
    for root, dirs, names in os.walk(root_dir):
        for name in names:
            if os.path.splitext(name)[1] == '.mp3':
                tracks.append(os.path.join(root, name))
    return tracks


def tags_for_songs(tracks):
    """"Return list of dicts mp3-tags from list of tracks."""
    return [get_song_info_from_mp3_tags(track) for track in tracks]


def str_to_int(key, value, fields):
    """"Return converted key from str to int for fields."""
    result = value
    if key in fields and value:
        try:
            result = int(value)
        except:
            pass
    return result


def get_song_info_from_mp3_tags(filename):
    """"Return dict with mp3-tags + path for track from filename string."""
    song_info_dict = {}
    tags = TinyTag.get(filename)
    all_attrs = dir(tags)
    mp3_attrs = [attr_name for attr_name in all_attrs if not attr_name.startswith('_')]

    for attr in mp3_attrs:
        song_info_dict[attr] = getattr(tags, attr)
    song_info_dict['path'] = filename

    for key, value in song_info_dict.items():
        if type(value) == str:
            value = value.replace('\x00', '')
            song_info_dict[key] = value
    for key, value in song_info_dict.items():
        fields_to_int = ('disc', 'disc_total', 'track', 'track_total', 'year')

        song_info_dict[key] = str_to_int(key, song_info_dict[key], fields_to_int)

        if key == 'duration' and song_info_dict[key]:
            try:
                song_info_dict[key] = '{}:{}'.format(int(song_info_dict[key] // 60),
                                                     int(song_info_dict[key] % 60))
            except:
                pass

    return song_info_dict


def filter_tracks(collection, artist):
    """"Return list of track tags dicts for artist."""
    return [track for track in collection if track['artist'] == artist]


def format_discography(tracks):
    """"
    Return dicts of albums.
    Key - album name, value - list of tracks sorted by number.
    """
    discography = {}
    for key, group in groupby(tracks, lambda x: x['album']):
        discography[key] = list(group)
        discography[key] = sorted(discography[key], key=lambda x: x['track'])
    return discography


def print_result(discography):
    for album in discography:
        album_item = discography[album]
        album_first_item = discography[album][0]
        print(discography[album])
        print('{} ({})'.format(album, album_first_item['year']))
        if album_first_item['disc'] and album_first_item['disc_total']:
            if album_first_item['disc'] < album_first_item['disc_total']:
                print('    Disc {} of {}'.format(album_first_item['disc'],
                                                 album_first_item['disc_total']
                                                 )
                      )
        for track in album_item:
            print('    {}.  "{}" {} ({})'.format(track['track'],
                                                 track['title'],
                                                 track['duration'],
                                                 track['path']
                                                 )
                  )
    return True


if __name__ == '__main__':
    print_result(format_discography(filter_tracks(tags_for_songs(find_all_tracks()), sys.argv[1])))
