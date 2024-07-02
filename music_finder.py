from apis import spotify
from apis import twilio

user_selections = {
    'genres': [],
    'artists': []
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


def handle_genre_selection():
    print('Handle genre selection here')
    # 1. Allow user to select one or more genres using the
    #    spotify.get_genres_abridged() function
    approved_genres = spotify.get_genres_abridged()
    favorite_genres = []
    print(approved_genres)
    inputed_genres = input("Out of the list of approved genres above, which genres are your favorite?")
    favorite_genres = inputed_genres.split(",")
    print("Ok we have stored the following genres as your favorite:", favorite_genres)
    # 2. Allow user to store / modify / retrieve genres
    #    in order to get song recommendations


def handle_artist_selection():
    print('Handle artist selection here...')
    # 1. Allow user to search for an artist using
    #    spotify.get_artists() function
    search_term = input("What are your favorite artists?")
    favorite_artists = []
    favorite_artists = search_term.split(",")
##    print(favorite_artists)
    recommended_artists = []
    inputed_artists = spotify.get_artists(search_term)
    print("Here are some related artists:")
    counter = 1
    for artist in inputed_artists:
        print(counter, artist['name'])
        counter += 1
    inputed_artists = input("Which of these artists do you like?")
    recommended_artists = []
    recommended_artists = inputed_artists.split(",")
    new_favorite_artists = []
    new_favorite_artists = favorite_artists + recommended_artists
    print("Ok we have stored the following artists as your favorite:", new_favorite_artists)
        
    # 2. Allow user to store / modify / retrieve artists
    #    in order to get song recommendations


def get_recommendations():
    print('Handle retrieving a list of recommendations here...')
    # 1. Allow user to retrieve song recommendations using the
    #    spotify.get_similar_tracks() function
    # 2. List them below
    try:
        if input("Would you like to search for related songs via your preferred artists or genres?") == "genres":
            recommended_songs = spotify.get_similar_tracks(favorite_genres)
            print(recommended_songs)
        else:
            recommended_songs = spotify.get_similar_tracks(new_favorite_artists)
            print(recommended_songs)
    except:
        print("You do not have any preferred genres stored with us. Please make another selection and try again.")
        

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
