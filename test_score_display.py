from flappy import score_display, font, screen 
# Tests that the score and high score surfaces are centered on the screen. 
def test_score_display_centering():
        game_state = "game_over"
        score = 10
        high_score = 5
        score_display(game_state, score, high_score)
        score_surface = font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288 // 2, 50))
        high_score_surface = font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288 // 2, 425))
        assert score_rect.center == (144, 50)
        assert high_score_rect.center == (144, 425)
