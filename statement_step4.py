import math


def statement(invoice, plays):
    def amount_for(a_performance):
        result = 0
        if play_for(a_performance)["type"] == "tragedy":
            result = 40000
            if a_performance["audience"] > 30:
                result += 1000 * (a_performance["audience"] - 30)
        elif play_for(a_performance)["type"] == "comedy":
            result = 30000
            if a_performance["audience"] > 20:
                result += 1000 + 500 * (a_performance["audience"] - 20)
            result += 300 * a_performance["audience"]
        else:
            raise ValueError("unknown type: {}".format(play_for(a_performance)["type"]))

        return result

    def play_for(a_performance):
        return plays[a_performance["playID"]]

    def volume_credits_for(perf):
        result = 0
        result += max(perf["audience"] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play_for(perf)["type"]:
            result += math.floor(perf["audience"] / 5)
        return result

    def total_amount():
        result = 0
        for perf in invoice["performances"]:
            result += amount_for(perf)
        return result

    def total_volume_credits():
        result = 0
        for perf in invoice["performances"]:
            result += volume_credits_for(perf)
        return result

    result = "Statement for {}\n".format(invoice["customer"])

    for perf in invoice["performances"]:
        this_amount = amount_for(perf)

        # print line for this order
        result += "  {}: {}({} seats)\n". \
            format(play_for(perf)["name"], usd(this_amount), perf["audience"])

    result += "Amount owed is {}\n".format(usd(total_amount()))
    result += "You earned {} credits\n".format(total_volume_credits())

    return result


def usd(a_number):
    return '${:,.2f}'.format(a_number/100)