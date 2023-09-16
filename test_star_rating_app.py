""" 
Homework 5: Tester for Star Rating App
===========================
Course:   CS 5001
Student:  UPDATE
Semester: UPDATE

Your test code for star rating app.
"""
import star_rating_app as app  # by doing this, we can just use app.function_name instead of star_rating_app.function_name


def test_convert_str_movie_tuple() -> int:
    """ tests convert_str_movie_tuple 
    with multiple inputs.
    
    Returns:
        int: number of tests that failed
    """
    failed = 0
    # test 1
    expected = ("Princess Bride", 10)
    actual = app.convert_str_movie_tuple("Princess Bride,10")
    if expected != actual:
        failed += 1
        print("test_convert_str_movie_tuple failed")
        print("expected:", expected)
        print("actual:", actual)
    # add additional tests

    return failed


# write a function for every function in star rating app *EXCEPT*
# run, menu, print_movies - those three you should test by running
# the program and manually testing them. 



def main():
    failed = 0
    failed += test_convert_str_movie_tuple()

    if failed == 0:
        print("All tests passed!")
    else:
        print("Number of tests failed:", failed)


if __name__ == "__main__":
    main()




