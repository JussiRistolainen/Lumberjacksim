import pygame



class Timecount:

    def __init__(self,window,  Second, Minute, Hour, Day):
        self.window = window
        self.Second = Second
        self.Minute = Minute
        self.Hour = Hour
        self.Day = Day
        self.Mil = 0
        self.Black = (150, 150, 150)
        self.Darkness = (115, 118, 83)

        self.logs = 3
        self.matches = 3




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

        matchboxFont = self.Font.render("MatchBox:{0}".format(self.logs), 1,
                                      self.Black)
        self.matchboxR = matchboxFont.get_rect()
        self.matchboxR.center = (300, 20)



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
        matchboxFont = self.Font.render("{0:01}".format(self.matches), 1, self.Black)
        self.window.blit(matchboxFont, self.matchboxR)


    def get_time(self):
        return [self.Mil, self.Second, self.Minute]


    def update_items(self, object_list, pos, icon):
        picked_up_items = self.lift_item(object_list, pos, icon)
        for i in picked_up_items:
            if i[2] == 'Log':
                self.logs += 1
            if i[2] == 'Matches':
                self.matches += 5


    def craft_flame(self):
        self.logs -= 3
        self.matches -= 1

    def craft_torch(self):
        self.logs -= 1
        self.matches -= 1

    def light_match(self):
        self.matches -= 1

    def get_wood(self):
        return self.logs

    def get_matches(self):
        return self.matches

    def lift_item(self, object_list, position, icon):
        del_list = []
        del_item = []
        is_on_flame = False
        for index, i in enumerate(object_list):
            if i[4][0] < position[0] < i[4][2] and i[4][1] < position[1] < i[4][3] and i[3] == 1:
                if icon != 3 and icon !=4 and i[2] != 'fire':
                    del_list.append(index)
                    del_item.append(i)
                elif icon == 3 and self.matches >= 1:
                    if i[2] == "Log":
                        del_list.append(index)
                        object_list.append([i[0], i[1], 'fire', 0, [position[0]-30, position[1]-25, position[0]+30, position[1]+5], 0, 1])
                elif icon == 4 and self.logs >= 1:
                    if i[2] == "fire":
                        i[6] += 1
                        is_on_flame = True
                    if i[2] == 'fireplace':
                        i[6] += 1
                        self.logs -= 1
                        is_on_flame = True
        if icon == 4 and self.logs >= 1 and is_on_flame == False:
            object_list.append([position[0], position[1], 'Log', 0, [position[0] - 35, position[1] - 15, position[0] + 32, position[1] + 10]])
            self.logs -= 1
        for i in del_list:
            object_list.pop(i)
        return del_item


