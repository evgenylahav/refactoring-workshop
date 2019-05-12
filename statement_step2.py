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

    total_amount = 0
    volume_credits = 0
    result = "Statement for {}\n".format(invoice["customer"])
    format = lambda x: '${:,.2f}'.format(x)

    for perf in invoice["performances"]:
        this_amount = amount_for(perf)

        # add volume credits
        volume_credits += max(perf["audience"] - 30, 0)

        # add extra credit for every ten comedy attendees
        if "comedy" == play_for(perf)["type"]:
            volume_credits += math.floor(perf["audience"] / 5)

        # print line for this order
        result += "  {}: {}({} seats)\n". \
            format(play_for(perf)["name"], format(this_amount / 100), perf["audience"])

        total_amount += this_amount

    result += "Amount owed is {}\n".format(format(total_amount / 100))
    result += "You earned {} credits\n".format(volume_credits)

    return result
