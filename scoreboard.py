class ScoreBoard():
    """ A class to report scoring information. """

    def __init__(self, ai_settings, screen, stats):
        """ Initialize scorekeeping attributes. """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

    