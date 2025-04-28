:- discontiguous assertz/3, movie/5.

% Regla 1: Si una película es de género Action y Fantasy, entonces es Adventure y tiene duración larga
assertz(adventure(X) :- action(X), fantasy(X), run_time_long(X)).

% Regla 2: Si una película es de género Adventure y tiene duración larga, entonces es Action y Fantasy
assertz(action(X), fantasy(X) :- adventure(X), run_time_long(X)).

% Regla 3: Si una película tiene calificación alta, es Adventure y tiene duración larga, entonces es Action y Fantasy
assertz(action(X), fantasy(X) :- rating_high, adventure(X), run_time_long(X)).

% Regla 4: Si una película es de género Action y Fantasy y tiene calificación alta, entonces es Adventure y tiene duración larga
assertz(adventure(X), run_time_long(X) :- rating_high, action(X), fantasy(X)).

% Regla 5: Si una película es de género Adventure y tiene duración larga, entonces tiene calificación alta y es Action y Fantasy
assertz(rating_high, action(X), fantasy(X) :- adventure(X), run_time_long(X)).

% Regla 6: Si una película es de género Action y Fantasy, entonces tiene calificación alta y es Adventure y tiene duración larga
assertz(rating_high, adventure(X), run_time_long(X) :- action(X), fantasy(X)).

% Regla 7: Si una película tiene duración media y es de género Animation, entonces es Adventure y Comedy
assertz(adventure(X), comedy(X) :- run_time_medium, animation(X)).


% Base de datos de películas
:- dynamic action/1, fantasy/1, adventure/1, run_time_long/1, rating_high/1, comedy/1.

movie('The Shawshank Redemption', 1994, 9.3, 'Drama', '2h 22m').
movie('The Godfather', 1972, 9.2, 'Crime,Drama', '2h 55m').
movie('The Dark Knight', 2008, 9.0, 'Action,Crime,Drama', '2h 32m').
movie('The Godfather Part II', 1974, 9.0, 'Crime,Drama', '3h 22m').
movie('12 Angry Men', 1957, 9.0, 'Crime,Drama', '1h 36m').
movie('Schindler\'s List', 1993, 9.0, 'Biography,Drama,History', '3h 15m').
movie('The Lord of the Rings: The Return of the King', 2003, 9.0, 'Action,Adventure,Drama', '3h 21m').
movie('Pulp Fiction', 1994, 8.9, 'Crime,Drama', '2h 34m').
movie('The Lord of the Rings: The Fellowship of the Ring', 2001, 8.8, 'Action,Adventure,Drama', '2h 58m').
movie('The Good, the Bad and the Ugly', 1966, 8.8, 'Adventure,Western', '2h 58m').
movie('Forrest Gump', 1994, 8.8, 'Drama,Romance', '2h 22m').
movie('Fight Club', 1999, 8.8, 'Drama', '2h 19m').
movie('The Lord of the Rings: The Two Towers', 2002, 8.8, 'Action,Adventure,Drama', '2h 59m').
movie('Inception', 2010, 8.8, 'Action,Adventure,Sci-Fi', '2h 28m').
movie('Star Wars: Episode V - The Empire Strikes Back', 1980, 8.7, 'Action,Adventure,Fantasy', '2h 4m').
movie('The Matrix', 1999, 8.7, 'Action,Sci-Fi', '2h 16m').
movie('Goodfellas', 1990, 8.7, 'Biography,Crime,Drama', '2h 25m').
movie('One Flew Over the Cuckoo\'s Nest', 1975, 8.7, 'Drama', '2h 13m').
movie('Se7en', 1995, 8.6, 'Crime,Drama,Mystery', '2h 7m').
movie('Seven Samurai', 1954, 8.6, 'Action,Drama', '3h 27m').
movie('It\'s a Wonderful Life', 1946, 8.6, 'Drama,Family,Fantasy', '2h 10m').
movie('The Silence of the Lambs', 1991, 8.6, 'Crime,Drama,Thriller', '1h 58m').
movie('City of God', 2002, 8.6, 'Crime,Drama', '2h 10m').
movie('Saving Private Ryan', 1998, 8.6, 'Drama,War', '2h 49m').
movie('Interstellar', 2014, 8.6, 'Adventure,Drama,Sci-Fi', '2h 49m').
movie('Life Is Beautiful', 1997, 8.6, 'Comedy,Drama,Romance', '1h 56m').
movie('The Green Mile', 1999, 8.6, 'Crime,Drama,Fantasy', '3h 9m').
movie('Star Wars: Episode IV - A New Hope', 1977, 8.6, 'Action,Adventure,Fantasy', '2h 1m').
movie('Terminator 2: Judgment Day', 1991, 8.6, 'Action,Sci-Fi', '2h 17m').
movie('Back to the Future', 1985, 8.5, 'Adventure,Comedy,Sci-Fi', '1h 56m').
movie('Spirited Away', 2001, 8.6, 'Animation,Adventure,Family', '2h 5m').
movie('The Pianist', 2002, 8.5, 'Biography,Drama,Music', '2h 30m').
movie('Psycho', 1960, 8.5, 'Horror,Mystery,Thriller', '1h 49m').
movie('Parasite', 2019, 8.5, 'Drama,Thriller', '2h 12m').
movie('Léon: The Professional', 1994, 8.5, 'Action,Crime,Drama', '1h 50m').
movie('The Lion King', 1994, 8.5, 'Animation,Adventure,Drama', '1h 28m').
movie('Gladiator', 2000, 8.5, 'Action,Adventure,Drama', '2h 35m').
movie('American History X', 1998, 8.5, 'Crime,Drama', '1h 59m').
movie('The Departed', 2006, 8.5, 'Crime,Drama,Thriller', '2h 31m').
movie('The Usual Suspects', 1995, 8.5, 'Crime,Drama,Mystery', '1h 46m').
movie('The Prestige', 2006, 8.5, 'Drama,Mystery,Sci-Fi', '2h 10m').
movie('Whiplash', 2014, 8.5, 'Drama,Music', '1h 46m').
movie('Casablanca', 1942, 8.5, 'Drama,Romance,War', '1h 42m').
movie('Grave of the Fireflies', 1988, 8.5, 'Animation,Drama,War', '1h 29m').
movie('Harakiri', 1962, 8.6, 'Action,Drama,Mystery', '2h 13m').
movie('The Intouchables', 2011, 8.5, 'Biography,Comedy,Drama', '1h 52m').
movie('Modern Times', 1936, 8.5, 'Comedy,Drama,Romance', '1h 27m').
movie('Once Upon a Time in the West', 1968, 8.5, 'Western', '2h 45m').
movie('Rear Window', 1954, 8.5, 'Mystery,Thriller', '1h 52m').
movie('Cinema Paradiso', 1988, 8.5, 'Drama,Romance', '2h 35m').
movie('The Elephant Man', 1980, 8.2, 'Biography,Drama', '2h 4m').
movie('The Great Dictator', 1940, 8.4, 'Comedy,Drama,War', '2h 5m').
movie('Avengers: Infinity War', 2018, 8.4, 'Action,Adventure,Sci-Fi', '2h 29m').
movie('Witness for the Prosecution', 1957, 8.4, 'Crime,Drama,Mystery', '1h 56m').
movie('Aliens', 1986, 8.4, 'Action,Adventure,Sci-Fi', '2h 17m').
movie('Spider-Man: Into the Spider-Verse', 2018, 8.4, 'Animation,Action,Adventure', '1h 57m').
movie('American Beauty', 1999, 8.4, 'Drama', '2h 2m').
movie('Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb', 1964, 8.4, 'Comedy,War', '1h 35m').
movie('The Dark Knight Rises', 2012, 8.4, 'Action,Drama', '2h 44m').
movie('Oldboy', 2003, 8.4, 'Action,Drama,Mystery', '2h 0m').
movie('Inglourious Basterds', 2009, 8.3, 'Adventure,Drama,War', '2h 33m').
movie('Amadeus', 1984, 8.4, 'Biography,Drama,Music', '2h 40m').
movie('Coco', 2017, 8.4, 'Animation,Adventure,Comedy', '1h 45m').
movie('Toy Story', 1995, 8.3, 'Animation,Adventure,Comedy', '1h 21m').
movie('Joker', 2019, 8.4, 'Crime,Drama,Thriller', '2h 2m').
movie('Braveheart', 1995, 8.4, 'Biography,Drama,History', '2h 58m').
movie('The Boat', 1981, 8.4, 'Drama,War', 'Not Available').
movie('Avengers: Endgame', 2019, 8.4, 'Action,Adventure,Drama', '3h 1m').
movie('Princess Mononoke', 1997, 8.4, 'Animation,Action,Adventure', 'PG-13').
movie('Once Upon a Time in America', 1984, 8.3, 'Crime,Drama', '3h 49m').
movie('Good Will Hunting', 1997, 8.3, 'Drama,Romance', 'R').
movie('Your Name.', 2016, 8.4, 'Animation,Drama,Fantasy', '1h 46m').
movie('3 Idiots', 2009, 8.4, 'Comedy,Drama', 'PG-13').
movie('Singin\' in the Rain', 1952, 8.3, 'Comedy,Musical,Romance', 'G').
movie('Requiem for a Dream', 2000, 8.3, 'Drama', 'Unrated').
movie('Toy Story 3', 2010, 8.3, 'Animation,Adventure,Comedy', 'G').
movie('High and Low', 1963, 8.4, 'Crime,Drama,Mystery', 'Not Rated').
movie('Capernaum', 2018, 8.4, 'Drama', 'R').
movie('Star Wars: Episode VI - Return of the Jedi', 1983, 8.3, 'Action,Adventure,Fantasy', 'PG').
movie('Eternal Sunshine of the Spotless Mind', 2004, 8.3, 'Drama,Romance,Sci-Fi', 'R').
movie('2001: A Space Odyssey', 1968, 8.3, 'Adventure,Sci-Fi', 'G').
movie('Reservoir Dogs', 1992, 8.3, 'Crime,Thriller', 'R').
movie('Come and See', 1985, 8.4, 'Drama,Thriller,War', 'Not Rated').
movie('The Hunt', 2012, 8.3, 'Drama', 'R').
movie('Citizen Kane', 1941, 8.3, 'Drama,Mystery', 'PG').
movie('M', 1931, 8.3, 'Crime,Mystery,Thriller', 'Passed').
movie('Lawrence of Arabia', 1962, 8.3, 'Adventure,Biography,Drama', 'Approved').
movie('North by Northwest', 1959, 8.3, 'Action,Adventure,Mystery', 'Approved').
movie('Vertigo', 1958, 8.3, 'Mystery,Romance,Thriller', 'PG').
movie('Ikiru', 1952, 8.3, 'Drama', 'Not Rated').
movie('Amélie', 2001, 8.3, 'Comedy,Romance', 'R').
movie('The Apartment', 1960, 8.3, 'Comedy,Drama,Romance', 'Approved').
movie('A Clockwork Orange', 1971, 8.3, 'Crime,Sci-Fi', 'X').
movie('Double Indemnity', 1944, 8.3, 'Crime,Drama,Film-Noir', 'Passed').
movie('Full Metal Jacket', 1987, 8.3, 'Drama,War', 'R').
movie('Top Gun: Maverick', 2022, 8.3, 'Action,Drama', 'PG-13').
movie('Scarface', 1983, 8.3, 'Crime,Drama', 'R').
movie('Hamilton', 2020, 8.4, 'Biography,Drama,History', 'PG-13').
movie('Incendies', 2010, 8.3, 'Drama,Mystery', 'R').
movie('To Kill a Mockingbird', 1962, 8.3, 'Crime,Drama', 'Approved').
movie('Heat', 1995, 8.3, 'Action,Crime,Drama', 'R').
movie('The Sting', 1973, 8.3, 'Comedy,Crime,Drama', 'PG').
movie('Up', 2009, 8.3, 'Animation,Adventure,Comedy', 'PG').
movie('A Separation', 2011, 8.3, 'Drama', 'PG-13').
movie('Metropolis', 1927, 8.3, 'Drama,Sci-Fi', 'Not Rated').
movie('Taxi Driver', 1976, 8.2, 'Crime,Drama', 'R').
movie('L.A. Confidential', 1997, 8.2, 'Crime,Drama,Mystery', 'R').
movie('Die Hard', 1988, 8.2, 'Action,Thriller', 'R').
movie('Snatch', 2000, 8.2, 'Comedy,Crime', 'R').
movie('Indiana Jones and the Last Crusade', 1989, 8.2, 'Action,Adventure', 'PG-13').
movie('Bicycle Thieves', 1948, 8.3, 'Drama', 'Not Rated').
movie('Like Stars on Earth', 2007, 8.3, 'Drama,Family', 'PG').
movie('1917', 2019, 8.2, 'Action,Drama,War', 'R').
movie('Downfall', 2004, 8.2, 'Biography,Drama,History', 'R').
movie('Dangal', 2016, 8.3, 'Action,Biography,Drama', 'Not Rated').
movie('For a Few Dollars More', 1965, 8.2, 'Western', 'R').
movie('Batman Begins', 2005, 8.2, 'Action,Crime,Drama', 'PG-13').
movie('The Kid', 1921, 8.3, 'Comedy,Drama,Family', 'Passed').
movie('Some Like It Hot', 1959, 8.2, 'Comedy,Music,Romance', 'Passed').
movie('The Father', 2020, 8.2, 'Drama,Mystery', 'PG-13').
movie('All About Eve', 1950, 8.2, 'Drama', 'Passed').
movie('The Wolf of Wall Street', 2013, 8.2, 'Biography,Comedy,Crime', 'R').
movie('Green Book', 2018, 8.2, 'Biography,Comedy,Drama', 'PG-13').
movie('Judgment at Nuremberg', 1961, 8.3, 'Drama,War', 'Approved').
movie('Casino', 1995, 8.2, 'Crime,Drama', 'R').
movie('Ran', 1985, 8.2, 'Action,Drama,War', 'R').
movie('Pan\'s Labyrinth', 2006, 8.2, 'Drama,Fantasy,War', 'R').
movie('The Truman Show', 1998, 8.2, 'Comedy,Drama', 'PG').
movie('There Will Be Blood', 2007, 8.2, 'Drama', 'R').
movie('Unforgiven', 1992, 8.2, 'Drama,Western', 'R').
movie('The Sixth Sense', 1999, 8.2, 'Drama,Mystery,Thriller', 'PG-13').
movie('Shutter Island', 2010, 8.2, 'Mystery,Thriller', 'R').
movie('A Beautiful Mind', 2001, 8.2, 'Biography,Drama', 'PG-13').
movie('Jurassic Park', 1993, 8.2, 'Action,Adventure,Sci-Fi', 'PG-13').
movie('Yojimbo', 1961, 8.2, 'Action,Drama,Thriller', 'Not Rated').
movie('The Treasure of the Sierra Madre', 1948, 8.2, 'Adventure,Drama,Western', 'Passed').
movie('Monty Python and the Holy Grail', 1975, 8.2, 'Adventure,Comedy,Fantasy', 'PG').
movie('The Great Escape', 1963, 8.2, 'Adventure,Drama,History', 'Approved').
movie('No Country for Old Men', 2007, 8.2, 'Crime,Drama,Thriller', 'R').
movie('Spider-Man: No Way Home', 2021, 8.2, 'Action,Adventure,Fantasy', 'PG-13').
movie('Kill Bill: Vol. 1', 2003, 8.2, 'Action,Crime,Drama', 'R').
movie('Rashomon', 1950, 8.2, 'Crime,Drama,Mystery', 'Not Rated').
movie('The Thing', 1982, 8.2, 'Horror,Mystery,Sci-Fi', 'R').
movie('Finding Nemo', 2003, 8.2, 'Animation,Adventure,Comedy', 'G').
movie('The Elephant Man', 1980, 8.2, 'Biography,Drama', 'PG').
movie('Chinatown', 1974, 8.2, 'Drama,Mystery,Thriller', 'R').
movie('Raging Bull', 1980, 8.2, 'Biography,Drama,Sport', 'R').
movie('V for Vendetta', 2005, 8.2, 'Action,Drama,Sci-Fi', 'R').
movie('Gone with the Wind', 1939, 8.2, 'Drama,Romance,War', 'Passed').
movie('Lock, Stock and Two Smoking Barrels', 1998, 8.2, 'Action,Comedy,Crime', 'R').
movie('Inside Out', 2015, 8.2, 'Animation,Adventure,Comedy', 'PG').
movie('Dial M for Murder', 1954, 8.2, 'Crime,Thriller', 'PG').
movie('The Secret in Their Eyes', 2009, 8.2, 'Drama,Mystery,Romance', 'R').
movie('Howl\'s Moving Castle', 2004, 8.2, 'Animation,Adventure,Family', 'PG').
movie('Three Billboards Outside Ebbing, Missouri', 2017, 8.1, 'Comedy,Crime,Drama', 'R').
movie('The Bridge on the River Kwai', 1957, 8.2, 'Adventure,Drama,War', 'PG').
movie('Trainspotting', 1996, 8.1, 'Drama', 'R').
movie('Prisoners', 2013, 8.1, 'Crime,Drama,Mystery', 'R').
movie('Warrior', 2011, 8.2, 'Action,Drama,Sport', 'PG-13').
movie('Fargo', 1996, 8.1, 'Crime,Thriller', 'R').
movie('Gran Torino', 2008, 8.1, 'Drama', 'R').
movie('My Neighbor Totoro', 1988, 8.1, 'Animation,Comedy,Family', 'G').
movie('Catch Me If You Can', 2002, 8.1, 'Biography,Crime,Drama', 'PG-13').
movie('Million Dollar Baby', 2004, 8.1, 'Drama,Sport', 'PG-13').
movie('Children of Heaven', 1997, 8.2, 'Drama,Family,Sport', 'PG').
movie('Blade Runner', 1982, 8.1, 'Action,Drama,Sci-Fi', 'R').
movie('The Gold Rush', 1925, 8.1, 'Adventure,Comedy,Drama', 'Passed').
movie('Before Sunrise', 1995, 8.1, 'Drama,Romance', 'R').
movie('12 Years a Slave', 2013, 8.1, 'Biography,Drama,History', 'R').
movie('Klaus', 2019, 8.2, 'Animation,Adventure,Comedy', 'PG').
movie('Harry Potter and the Deathly Hallows: Part 2', 2011, 8.1, 'Adventure,Family,Fantasy', 'PG-13').
movie('On the Waterfront', 1954, 8.1, 'Crime,Drama,Thriller', 'Approved').
movie('Ben-Hur', 1959, 8.1, 'Adventure,Drama', 'G').
movie('Gone Girl', 2014, 8.1, 'Drama,Mystery,Thriller', 'R').
movie('The Grand Budapest Hotel', 2014, 8.1, 'Adventure,Comedy,Crime', 'R').
movie('Wild Strawberries', 1957, 8.1, 'Drama,Romance', 'Not Rated').
movie('The General', 1926, 8.1, 'Action,Adventure,Comedy', 'Passed').
movie('The Third Man', 1949, 8.1, 'Film-Noir,Mystery,Thriller', 'Approved').
movie('In the Name of the Father', 1993, 8.1, 'Biography,Crime,Drama', 'R').
movie('The Deer Hunter', 1978, 8.1, 'Drama,War', 'R').
movie('Barry Lyndon', 1975, 8.1, 'Adventure,Drama,War', 'PG').
movie('Hacksaw Ridge', 2016, 8.1, 'Biography,Drama,History', 'R').
movie('The Wages of Fear', 1953, 8.2, 'Adventure,Drama,Thriller', 'Not Rated').
movie('Memories of Murder', 2003, 8.1, 'Crime,Drama,Mystery', 'Not Rated').
movie('Sherlock Jr.', 1924, 8.2, 'Action,Comedy,Romance', 'Passed').
movie('Wild Tales', 2014, 8.1, 'Comedy,Drama,Thriller', 'R').
movie('Mr. Smith Goes to Washington', 1939, 8.1, 'Comedy,Drama', 'Passed').

% Ejemplo de clasificación
% Se puede clasificar películas según las reglas definidas
assertz(action(X) :- movie(X, _, Rating, Genre, _), sub_string(Genre, _, _, _, 'Action'), Rating >= 8.0).
assertz(fantasy(X) :- movie(X, _, Rating, Genre, _), sub_string(Genre, _, _, _, 'Fantasy'), Rating >= 8.0).
assertz(adventure(X) :- movie(X, _, Rating, Genre, _), sub_string(Genre, _, _, _, 'Adventure'), Rating >= 8.0).
assertz(run_time_long(X) :- movie(X, _, _, _, RunTime), RunTime @> '2h').
assertz(rating_high :- movie(_, _, Rating, _, _), Rating >= 8.0).