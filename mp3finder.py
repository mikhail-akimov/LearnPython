from tinytag import TinyTag
import os
import sys
import ast
from itertools import groupby


def find_all_tracks():
    """"Return list of all .mp3 in root_dir."""
    root_dir = os.getcwd()
    tracks = []
    for root, dirs, names in os.walk(root_dir):
        for name in names:
            if name[-4::1] == '.mp3':
                tracks.append(os.path.join(root, name))
    return tracks


def tags_for_songs(tracks):
    """"Return list of dicts mp3-tags with tag path from list of tracks."""
    mp3_collection = []
    for track in tracks:
        info = get_song_info_from_mp3_tags(track)
        info['path'] = track
        mp3_collection.append(info)
    return mp3_collection


def get_song_info_from_mp3_tags(filename):
    """"Return formatted dict with mp3-tags for track from filename string."""
    song_info_dict = ast.literal_eval(str(TinyTag.get(filename)))
    for key, value in song_info_dict.items():
        if type(value) == str:
            value = value.replace('\x00', '')
            song_info_dict[key] = value
    for key, value in song_info_dict.items():
        if key == 'disc' and song_info_dict[key]:
            song_info_dict[key] = int(song_info_dict[key])
        if key == 'disc_total' and song_info_dict[key]:
            song_info_dict[key] = int(song_info_dict[key])
        if key == 'track' and song_info_dict[key]:
            song_info_dict[key] = int(song_info_dict[key])
        if key == 'track_total' and song_info_dict[key]:
            song_info_dict[key] = int(song_info_dict[key])
        if key == 'year' and song_info_dict[key]:
            song_info_dict[key] = int(song_info_dict[key])
        if key == 'duration' and song_info_dict[key]:
            song_info_dict[key] = '{}:{}'.format(int(song_info_dict[key] // 60),
                                                 int(song_info_dict[key] % 60))
    return song_info_dict


def filter_tracks(collection, artist):
    """"Return list of track tags dicts for artist."""
    result = []
    for track in collection:
        if track['artist'] == artist:
            result.append(track)
    return result


def format_discography(tracks):
    """"
    Return dicts of albums.
    Key - album name, value - list of tracks sorted by number.
    """
    discography = {}
    for key, group in groupby(tracks, lambda x: x['album']):
        discography[key] = []
        for track in group:
            discography[key].append(track)
            discography[key] = sorted(discography[key],
                                      key=lambda x: x['track'])
    return discography


def print_result(discography):
    for album in discography:
        print('{} ({})'.format(album, discography[album][0]['year']))
        if discography[album][0]['disc'] < discography[album][0]['disc_total']:
            print('    Disc {} of {}'.format(discography[album][0]['disc'],
                                             discography[album][0]['disc_total']
                                             )
                  )
        # не хватает тестовых данных, чтобы допилить сортировку по дискам
        for track in discography[album]:
            print('    {}.  "{}" {} ({})'.format(track['track'],
                                                 track['title'],
                                                 track['duration'],
                                                 track['path']
                                                 )
                  )
    return True


if __name__ == '__main__':
    print_result(format_discography(filter_tracks(tags_for_songs(find_all_tracks()), sys.argv[1])))
