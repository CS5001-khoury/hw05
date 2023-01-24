"""
Homework 5: Star Rating App
===========================
Course:   CS 5001
Student:  UPDATE
Semester: UPDATE

An application that queries the client for movie titles
and a rating for each movie.
"""
from typing import List, Tuple
import string

_MIN_STARS = 1
_MAX_STARS = 5
# don't forget to add _SPACING here set to 2


def add_movie(val : str = '') -> Tuple[str, int]:
    """
    Gets a movie and rating from the client.
    if not input is provided, get_movie_by_input()
    is called with its values returned.

    
    For Example:
        >>> add_movie("v,5")
        ('V', 5)
        >>> add_movie("Princess bride  ,10")
        ('Princess Bride', 10)
        >>> add_movie("   JurAssic shARk  ,    1  ")
        ('Jurassic Shark', 1)

        assume avatar and 3 are entered
        >>> add_movie()              # doctest: +NORMALIZE_WHITESPACE
        Enter a movie:
        Enter a rating 1-5: 
        ('Avatar', 3)


    Returns:
        Tuple[str, int]: Movie and int rating 
    """
    return ('', 0) # replace


def get_movie_by_input() -> Tuple[str, int]:
    """Gets a movie by input, first asking for the movie 
    than the rating. Uses get_valid_int to confirm
    rating is a number



    Returns:
        Tuple[str, int]: moving title, rating
    """
    movie = clean_title(input("Enter a movie: "))
    rating = get_valid_int(f"Enter a rating {_MIN_STARS}-{_MAX_STARS}: ")
    return (movie, rating)

def clean_title(movie: str) -> str:
    """
    Cleans a string stripping trailing and leading whitespaces,
    and converts it to title case. 

    Examples:
        >>> clean_title("     v")
        'V'
        >>> clean_title("Princess bride  ")
        'Princess Bride'
        >>> clean_title("it's a wonderful life")
        'It's A Wonderful Life'

    See:
        https://docs.python.org/3/library/stdtypes.html#string-methods

    Arguments:
        movie (str): movie title to clean
    Returns:
        str : the movie in title case, and leading and trailing spaces removed
    """
    return '' #replace


def get_valid_int(prompt: str) -> int:
    """Prompts the user for an int value, and keep
    repeating until a numeric value is entered.
    Will not accept negative or decimal values (every number must be a digit)

    Args:
        prompt (str): the string to prompt the client with

    Returns:
        int: the final value
    """
    return 0 # replace with 04 homework

def convert_rating(val: int) -> str:
    """Converts rating to stars (*) equal
    to the rating. Any value over _MAX_STARS will only
    return _MAX_STARS stars, and any value under _MIN_STARS
    will return _MIN_STARS star.

    Args:
        val (int): the rating value

    Returns:
        str: stars between _MIN_STARS and _MAX_STARS
    """
    return '*' # replace with 04 homework


def print_movies(movies: List[Tuple[str, int]]) -> None:
    """Prints out a list of movies.

    Prints out the movies to the console along with star ratings. 

    The print will have the star ratings on the left
    padded with _MAX_STARS+_SPACING total spaces before the movie title.
    This means if the star rating is *, there will be six spaces 
    before the movie title, whereas if the star rating
    is ***** there will be two spaces

    Args:
        movies (List[Tuple[str, int]]): A list of movies 
    """
    pass  # use a while loop


def menu() -> Tuple[str, str]:
    """prompts the client for their command.

    Options include: Add, List, Exit, or the Movie,Rating

    Returns:
        Tuple[str, str]: lowercase value, and original value of response
    """
    check = input("""What would you like to do (add, list, exit)? """)
    return (check.casefold(), check)  # left as an example


def run() -> None:
    """
    Runs the star rating application.
    """
    command, raw = menu()
    movies = []
    ## update while  loop from 04 adding option, changing function calls


if __name__ == "__main__":
    run()
