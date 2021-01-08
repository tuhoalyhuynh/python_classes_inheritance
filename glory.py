class Crucible():
    """ This is a glory class that will display the user's crucible scores """
    def __init__(self, valor, glory, valor_streak, glory_streak):
        self.valor = valor
        self.glory = glory
        self.valor_streak = valor_streak
        self.glory_streak = glory_streak

    def ranked_win(self):
        if self.glory_streak == 5:
            self.glory_streak = 1
        else:
            self.glory_streak += 1

        if self.glory == 5500:
            self.glory = 5500
        else:
            if self.glory_streak == 1:
                self.glory += 40
            elif self.glory_streak == 2:
                self.glory += 60
            elif self.glory_streak == 3:
                self.glory += 80
            elif self.glory_streak == 4:
                self.glory += 100
            elif self.glory_streak == 5:
                self.glory += 120
        print(f"Current Glory Rank: {self.glory}")
        print(f"Current Glory Streak: {self.glory_streak}")

    def ranked_loss(self):
        if self.glory_streak == 1:
            self.glory_streak -= 1
        elif self.glory_streak == 0:
            self.glory_streak = 0
        else:
            self.glory_streak -= 2

        self.glory -= 66
        print(f"Current Glory Rank: {self.glory}")
        print(f"Current Glory Streak: {self.glory_streak}")


tuhoarex = Crucible(0, 0, 0, 0)
tuhoarex.ranked_win()
tuhoarex.ranked_win()
tuhoarex.ranked_win()
tuhoarex.ranked_win()
tuhoarex.ranked_win()
tuhoarex.ranked_loss()