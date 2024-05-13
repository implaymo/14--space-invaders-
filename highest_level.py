class HighLevel:
    def __init__(self) -> None:
        self.high_score = 0

    def load_highscore(self, level):
        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
                if level > self.high_score:
                    with open("highscore.txt", "w") as new_file:
                        new_highscore = new_file.write(str(level))
                        self.high_score = new_highscore
                        return self.high_score
                else:
                    return self.high_score
        except FileNotFoundError:
            with open("highscore.txt", "w") as file:
                self.high_score = file.write(str(level))
                return self.high_score
            