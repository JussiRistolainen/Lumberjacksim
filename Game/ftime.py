import pygame


class Timecount:

    def __init__(self,window,  Second, Minute, Hour, Day):
        self.window = window
        self.Second = Second
        self.Minute = Minute
        self.Hour = Hour
        self.Day = Day
        self.Mil = 0
        self.logs = 0
        self.Black = (150, 150, 150)
        self.Darkness = (115, 118, 83)



    def update_time(self):
        self.Mil += 1
        if self.Mil == 10:
            self.Second += 1
            self.Mil = 0
        if self.Second == 60:
            self.Minute += 1
            self.Second = 0
        if self.Minute == 60:
            self.Hour += 1
            self.Minute = 0
        if self.Hour == 12:
            self.Day += 1
            self.Hour = 0

        self.Font = pygame.font.SysFont("Trebuchet MS", 25)
        DayFont = self.Font.render("Day:{0:03}".format(self.Day), 1, self.Black)  # zero-pad day to 3 digits
        self.DayFontR = DayFont.get_rect()
        self.DayFontR.center = (100, 20)
        # Hour
        HourFont = self.Font.render("Hour:{0:02}".format(self.Hour), 1, self.Black)  # zero-pad hours to 2 digits
        self.HourFontR = HourFont.get_rect()
        self.HourFontR.center = (1120, 20)
        # Minute
        MinuteFont = self.Font.render("Minute:{0:02}".format(self.Minute), 1,
                                      self.Black)  # zero-pad minutes to 2 digits
        self.MinuteFontR = MinuteFont.get_rect()
        self.MinuteFontR.center = (1165, 20)

        SecondFont = self.Font.render("Second:{0:02}".format(self.Second), 1,
                                      self.Black)  # zero-pad Seconds to 2 digits
        self.SecondFontR = SecondFont.get_rect()
        self.SecondFontR.center = (1200, 20)

        logFont = self.Font.render("Log:{0}".format(self.logs), 1,
                                      self.Black)
        self.logFontR = logFont.get_rect()
        self.logFontR.center = (200, 20)



    def update_overlay(self):
        SecondFont = self.Font.render("{0:02}".format(self.Second), 1, self.Black)
        self.window.blit(SecondFont, self.SecondFontR)
        MinuteFont = self.Font.render("{0:02}:".format(self.Minute), 1, self.Black)
        self.window.blit(MinuteFont, self.MinuteFontR)
        HourFont = self.Font.render("{0:02}:".format(self.Hour), 1, self.Black)
        self.window.blit(HourFont, self.HourFontR)
        DayFont = self.Font.render("Day:{0:01}".format(self.Day), 1, self.Black)
        self.window.blit(DayFont, self.DayFontR)
        logFont = self.Font.render("{0:01}".format(self.logs), 1, self.Black)
        self.window.blit(logFont, self.logFontR)


    def get_time(self):
        return [self.Mil, self.Second, self.Minute]


    def update_items(self, picked_up_items):
        for i in picked_up_items:
            if i[2] == 'Log':
                self.logs += 1

