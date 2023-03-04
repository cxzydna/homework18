"""Test data module"""

from implemented import directors_service, genres_service, movies_service


def create_data(database):
    database.drop_all()
    database.create_all()

    movies = [
        {
            'title': 'Harry Potter and the Sorcerers Stone',
            'description': "An orphaned boy enrolls in a school of wizardry, "
                           "where he learns the truth about himself, "
                           "his family and the terrible evil that haunts "
                           "the magical world.",
            'trailer': 'https://www.imdb.com/video/vi3115057433/?ref_=tt_vi_i_1',
            'year': 2001,
            'rating': 'PG',
            'genre_id': 1,
            'director_id': 1
        },
        {
            'title': 'Harry Potter and the Chamber of Secrets',
            'description': "An ancient prophecy seems to be coming true "
                           "when a mysterious presence begins stalking the "
                           "corridors of a school of magic and leaving "
                           "its victims paralyzed.",
            'trailer': 'https://www.imdb.com/video/vi1705771289/?playlistId'
                       '=tt0295297&ref_=tt_ov_vi',
            'year': 2002,
            'rating': 'PG',
            'genre_id': 1,
            'director_id': 1
        },

        {
            'title': 'Harry Potter and the Prisoner of Azkaban',
            'description': "Harry Potter, Ron and Hermione return to Hogwarts "
                           "School of Witchcraft and Wizardry for their third "
                           "year of study, where they delve into the mystery "
                           "surrounding an escaped prisoner who poses a "
                           "dangerous threat to the young wizard.",
            'trailer': 'https://www.imdb.com/video/vi2007761177/?playlistId'
                       '=tt0304141&ref_=tt_ov_vi',
            'year': 2004,
            'rating': 'PG',
            'genre_id': 1,
            'director_id': 2
        },

        {
            'title': 'Harry Potter and the Goblet of Fire',
            'description': "Harry Potter finds himself competing in a "
                           "hazardous tournament between rival schools of "
                           "magic, but he is distracted by recurring "
                           "nightmares.",
            'trailer': 'https://www.imdb.com/video/vi2611740953/?playlistId=tt0330373&ref_=tt_pr_ov_vi',
            'year': 2005,
            'rating': 'PG-13',
            'genre_id': 1,
            'director_id': 3
        },

        {
            'title': 'Harry Potter and the Order of the Phoenix',
            'description': "Warning about Lord Voldemort's return "
                           "scoffed at, Harry and Dumbledore are targeted "
                           "by the Wizard authorities as an authoritarian "
                           "bureaucrat slowly seizes power at Hogwarts.",
            'trailer': 'https://www.imdb.com/video/vi2192310553/?playlistId=tt0373889&ref_=tt_pr_ov_vi',
            'year': 2007,
            'rating': 'PG-13',
            'genre_id': 1,
            'director_id': 4
        },

        {
            'title': 'Harry Potter and the Half-Blood Prince',
            'description': "As Harry Potter begins his sixth year at "
                           "Hogwarts, he discovers an old book marked as "
                           "'the property of the Half-Blood Prince' and "
                           "begins to learn more about Lord Voldemort's "
                           "dark past.",
            'trailer': 'https://www.imdb.com/video/vi1061421849/?playlistId=tt0417741&ref_=tt_ov_vi',
            'year': 2009,
            'rating': 'PG',
            'genre_id': 1,
            'director_id': 4
        },

        {
            'title': 'Harry Potter and the Deathly Hallows: Part 1',
            'description': "As Harry, Ron and Hermione race against time "
                           "and evil to destroy the Horcruxes, they uncover "
                           "the existence of the three most powerful objects "
                           "in the wizarding world: the Deathly Hallows.",
            'trailer': 'https://www.imdb.com/video/vi1023514905/?playlistId=tt0926084&ref_=tt_ov_vi',
            'year': 2010,
            'rating': 'PG-13',
            'genre_id': 1,
            'director_id': 4
        },

        {
            'title': 'Harry Potter and the Deathly Hallows: Part 2',
            'description': "Harry, Ron, and Hermione search for Voldemort's "
                           "remaining Horcruxes in their effort to destroy "
                           "the Dark Lord as the final battle rages on "
                           "at Hogwarts.",
            'trailer': 'https://www.imdb.com/video/vi128621593/?playlistId=tt1201607&ref_=tt_ov_vi',
            'year': 2011,
            'rating': 'PG-13',
            'genre_id': 1,
            'director_id': 4
        }]

    directors = [
        {'name': "Chris Columbus"},
        {'name': "Alfonso Cuarón"},
        {'name': "Mike Newell"},
        {'name': "David Yates"}
    ]

    for movie in movies:
        movies_service.post_movie(movie)

    for director in directors:
        directors_service.post_director(director)

    genres_service.post_genre({'name': "Fantasy"})
