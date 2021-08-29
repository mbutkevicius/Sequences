from nested_data import albums
# Represents a constant if all in caps. Do not change constants
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(song_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
        # PRESS CONTROL SHIFT UP/DOWN TO MOVE CODE UP OR DOWN A LINE
        print('Playing "{}"'.format(title))
    print("=" * 40)
