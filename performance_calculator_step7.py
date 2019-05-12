import math


def create_performance_calculator(a_performance, a_play):
    if a_play["type"] == "tragedy":
        return TragedyCalculator(a_performance, a_play)
    elif a_play["type"] == "comedy":
        return ComedyCalculator(a_performance, a_play)
    else:
        raise ValueError("unknown type: {}".format(a_play["type"]))


class PerformanceCalculator:
    def __init__(self, a_performance, a_play):
        self.performance = a_performance
        self.play = a_play

    def volume_credits(self):
        return max(self.performance["audience"] - 30, 0)


class TragedyCalculator(PerformanceCalculator):
    def amount(self):
        result = 40000
        if self.performance["audience"] > 30:
            result += 1000 * (self.performance["audience"] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def amount(self):
        result = 30000
        if self.performance["audience"] > 20:
            result += 1000 + 500 * (self.performance["audience"] - 20)
        result += 300 * self.performance["audience"]
        return result

    def volume_credits(self):
        return super().volume_credits() + math.floor(self.performance["audience"] / 5)
