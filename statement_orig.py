import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = "Statement for {}\n".format(invoice["customer"])
    format = lambda x: '${:,.2f}'.format(x)

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0

        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 1000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise ValueError("unknown type: {}".format(play["type"]))

        # add volume credits
        volume_credits += max(perf["audience"] - 30, 0)

        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)

        # print line for this order
        result += "  {}: {}({} seats)\n". \
            format(play["name"], format(this_amount / 100), perf["audience"])

        total_amount += this_amount

    result += "Amount owed is {}\n".format(format(total_amount / 100))
    result += "You earned {} credits\n".format(volume_credits)

    return result