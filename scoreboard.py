import pygame


class ScoreBoard():
    """ A class to report scoring information. """

    def __init__(self, ai_settings, screen, stats):
        """ Initialize scorekeeping attributes. """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_scrore()

    def prep_scrore(self):
        """ Turn the score into a rendered image. """
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                        self.ai_settings.bg_color)