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

# use these constants for the messages to make sure they are consistent
_WELCOME_MESSAGE = """Welcome to the movie tracker!\nEnter a movie and rating to add it to the list."""
_GOODBYE_MESSAGE = """Thanks for using the movie tracker!\nSadly, movies will not be saved, as we still need to learn how to write to files."""

_PROMPT = """What would you like to do? """
_HELP_MESSAGE = """
You have the following command options for the movie tracker. 
    add movie,rating: add a movie and rating to the list
                        examples: 
                            ? add Princess Bride,10   
                            ? add Jurassic Shark,1
    list [filter]: list all movies and ratings, contains optional filters
                        examples:
                            ? list
                            ? list > 3
                            ? list < 2
                            ? list = 5
                            ? list Bride
    help: print this help message
    exit: exit the movie tracker
""".strip()


# COMMAND OPTION RETURNS
_ADD_COMMAND = "add"
_LIST_COMMAND = "list"
_EXIT_COMMAND = "exit"

# you can use this list for something like the following
# if command in _FILTER_OPERATION_OPTIONS:  
#    do something
# else:
#    assume it is a movie title
_FILTER_OPERATION_OPTIONS = ['<', '>', '=', '<=', '>=', '!=']

# some program constants
_MIN_STARS = 1
_MAX_STARS = 5
_SPACER = 2


def convert_str_movie_tuple(val: str) -> Tuple[str, int]:
    """
    Converts a string in the format of "movie,rating" to a tuple
    It will clean up the title by calling clean_title, and will
    convert the rating to an int. This function assumes the string
    is correct, and in the format of "movie,rating" where movie is
    a string and rating is an int. 

    For Example:
        >>> convert_str_movie_tuple("v,5")
        ('V', 5)
        >>> convert_str_movie_tuple("Princess bride  ,10")
        ('Princess Bride', 10)
        >>> convert_str_movie_tuple("   JurAssic shARk  ,    1  ")
        ('Jurassic Shark', 1)

    Args:
        val (str): String in the format of "movie,rating"

    Returns:
        Tuple[str, int]: Movie and int rating 
    """
    pass # replace with your code


def clean_title(movie: str) -> str:
    """
    Cleans a string stripping trailing and leading whitespaces,
    and converts it to title case (capwords). 

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
    pass # replace with your code


def convert_rating(val: int, min_stars: int = _MIN_STARS, max_stars: int = _MAX_STARS) -> str:
    """Converts rating to stars (*) equal
    to the rating. Any value over max_stars will only
    return max_stars stars, and any value under min_stars
    will return min_stars star.

    Args:
        val (int): the rating value
        min_stars (int, optional): the minimum number of stars to return. Defaults to _MIN_STARS.
        max_stars (int, optional): the maximum number of stars to return. Defaults to _MAX_STARS.


    Returns:
        str: stars between min_stars and max_stars
    """
    pass # replace with your code


def check_filter(movie: Tuple[str, int], filter: str) -> bool:
    """Checks if the movie title contains the filter.

    The filter can either be a string  (case insensitive) that will map to the title,
    or a filter operation and a number. The filter operation can be
    one of the following: <, >, =, <=, >=, !=. Which is meant to check
    the rating of the movie based on the number that follows. 

    if the empty string ("") is passed in, then the function will return True.

    Examples:
        >>> check_filter(("Princess Bride", 10), "Bride")
        True
        >>> check_filter(("Princess Bride", 10), "bride")
        True
        >>> check_filter(("Princess Bride", 10), "> 3")
        True
        >>> check_filter(("Princess Bride", 10), "< 3")
        False
        >>> check_filter(("Princess Bride", 10), "= 10")
        True
        >>> check_filter(("Princess Bride", 10), "= 11")
        False
        >>> check_filter(("Princess Bride", 10), "!= 10")
        False
        >>> check_filter(("Princess Bride", 10), "")
        True


    Args:
        movie (Tuple[str, int]): The movie tuple
        filter (str): The filter to check

    Returns:
        bool: True the movie meets the filter requirements.
    """
    pass # replace with your code


def print_movies(movies: List[Tuple[str, int]], filter: str = '', spacer: int = _SPACER, max_stars: int = _MAX_STARS) -> None:
    """Prints out a list of movies.

    Prints out the movies to the console along with star ratings. 

    Will filter the movies before printing based on the filter 
    passed into the function. See: check_filter() for more details.

    Uses the string format
        f"{convert_rating(rating):<{max_stars + spacer}}{movie}"

    For grading purposes, print the movies in the order that they
    appear in the list, as you loop through the list (do not sort the list, do not concatenate the strings, etc)

    Args:
        movies (List[Tuple[str, int]]): The list of movies
        filter (str, optional): The filter to apply. Defaults to ''.
        spacer (int, optional): The number of spaces between the stars and the movie title. Defaults to _SPACER.
        max_stars (int, optional): The maximum number of stars to print, used for spacing purposes. Defaults to _MAX_STARS.
    """
    pass # replace with your code


# the following function is provided for you. You do not need to modify it.
# it provides an example of a multiple return value function, it also handles
# the menu error checking, so you can assume that the command will be one of the
# following: _ADD_COMMAND, _LIST_COMMAND, _EXIT_COMMAND, and the options will be
# a string, or the empty string.
def menu() -> Tuple[str, str]:
    """
    Prompts the client for their command.

    See HELP_MESSAGE for more options. Will also
    parse the command and return the command and
    any options that were passed in.

    Returns:
        Tuple[str, str]: the command OPTION, and the value after the command, or 
        the empty string if there was no value.
    """
    check = input(_PROMPT).strip()
    command, *rest = check.split()  # this unpacks the string split by spaces into a variable, and a list of values
    command = command.casefold()
    while command not in [_ADD_COMMAND, _LIST_COMMAND, _EXIT_COMMAND]:
        print(_HELP_MESSAGE)
        check = input(_PROMPT).strip()
        command, *rest = check.split()
        command = command.casefold()    
    return command, " ".join(rest) 


def run() -> None:
    """
    Runs the star rating application.
    """
    print(_WELCOME_MESSAGE)
    command, options = '', ''
    movies = []
    # add your while loop here
    # it will loop until the command is _EXIT_COMMAND
    # inside the loop, you will need to check the command
    # and call the appropriate function
    # you will also need to update the movies list
    # dont' forget to call command, options = menu() at the start of the loop! 


    print(_GOODBYE_MESSAGE)


if __name__ == "__main__":
    run()
