from apis import spotify
from apis import twilio

user_selections = {
    'genres': [],
    'artists': [],
    'artist_ids': []
}

def print_menu():
    print('''
---------------------------------------------------------------------
Settings / Browse Options
---------------------------------------------------------------------
1 - Select your favorite genres
2 - Select your favorite artists
3 - Discover new music
4 - Quit
---------------------------------------------------------------------
    ''')
    print('Your genres: ', user_selections.get('genres'))
    print('Your artists: ', user_selections.get('artists'))
    print('Your tracks: []')

    print('-----------------------------------------------------------------------------')
    


def handle_genre_selection():
    global genres
    print('Handle genre selection here')
    # 1. Allow user to select one or more genres using the spotify.get_genres_abridged() function
    # 2. Allow user to store / modify / retrieve genres in order to get song recommendations
    spotify_genres = spotify.get_genres_abridged()
    list_of_genres = []
    print(spotify_genres)
    genres = input('Which genres are your favorites of those listed above?')
    list_of_genres = genres.split(',')
    for genres in list_of_genres:
        if genres in spotify_genres:
            user_selections['genres'].append(genres)
    print(user_selections)


    
artist_identification = []
def handle_artist_selection():
    global artist_ids
    print('Handle artist selection here...')
    # 1. Allow user to search for an artist using
    #    spotify.get_artists() function
    # 2. Allow user to store / modify / retrieve artists
    #    in order to get song recommendations
    artists_names=[]
    global artist_identification
    artist = input('Enter the name of an artist')
    new_favorite_artists=[]
    spotify_artist = spotify.get_artists(artist)
    counter=1
    for artist in spotify_artist:
        print(counter, artist.get('name'))
        artists_names.append(artist.get('name'))
        artist_identification.append(artist.get('id'))
        counter+=1
    favorite_artists = input('What artists do you prefer?') #how do i make it so it accepts numbers instead of a string
    list_of_artists = favorite_artists.split(',')
##  if favorite_artists() == 'clear':
##      user_selections['artists'].clear()
##      user_selections['artist_ids'].clear()
    for artist in list_of_artists:
        new_favorite_artists=spotify_artist[int(artist)-1]
        user_selections['artists'].append(new_favorite_artists['name'])
        user_selections['artist_ids'].append(new_favorite_artists['id'])
    print(new_favorite_artists['name'])



def get_recommendations():
    print('Handle retrieving a list of recommendations here...')
    # 1. Allow user to retrieve song recommendations using the
    #    spotify.get_similar_tracks() function
    # 2. List them below
    try:
        track_list = spotify.get_similar_tracks(user_selections['artist_ids'], [], user_selections['genres'])
        print('track_list', track_list)
        print(spotify.get_formatted_tracklist_table(track_list))
##        return track_list
        option = input ("Do you want the program to email you a list of recommendations? Type 'yes' or 'no'.")
        if option.lower() == 'yes':
            to_email = input('What email would you like this information to be sent to?')
            subject = input('Enter a subject for the email')
            sender = input('What email is this being sent from?')
            content = spotify.get_formatted_tracklist_table_html(track_list)
            twilio.send_mail(to_email, subject, content)
        elif option.lower() == 'no':
            print('Okay. Thank you.')
    except:
        print('There are no preferred genres in your storage. Please select another number and try again.')
       
            

# Begin Main Program Loop:

while True:
    print_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        handle_genre_selection()
    elif choice == '2':
        handle_artist_selection()
    elif choice == '3':
        get_recommendations()
        # In addition to showing the user recommendations, allow them
        # to email recommendations to one or more of their friends using
        # the twilio.send_mail() function.
    elif choice == '4':
        print('Quitting...')
        break
    else:
        print(choice, 'is an invalid choice. Please try again.')
    print()
    input('Press enter to continue...')
