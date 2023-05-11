from flappy import update_score

# Tests that the function updates the high score correctly when the score is higher than the current high score. 
def test_score_higher_than_high_score():
        assert update_score(10, 5) == 10

# Tests that the function updates the high score correctly when the score is equal to the current high score. 
def test_score_equal_to_high_score():
        assert update_score(5, 5) == 5

# Tests that the function correctly handles decimal scores and high scores. 
def test_decimal_scores():
        assert update_score(3.14, 2.71) == 3.14