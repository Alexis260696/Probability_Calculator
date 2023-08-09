import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls_drawn)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_matching = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_dict = {color: drawn_balls.count(color) for color in drawn_balls}
        matching = all(drawn_balls_dict.get(color, 0) >= count for color, count in expected_balls.items())
        if matching:
            count_matching += 1
    probability = count_matching / num_experiments
    return probability
