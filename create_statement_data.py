from performance_calculator import create_performance_calculator


def create_statement_data(invoice, plays):
    def play_for(a_performance):
        return plays[a_performance["playID"]]

    def total_amount(data):
        return sum([x["amount"] for x in data["performances"]])

    def total_volume_credits(data):
        return sum([x["volume_credits"] for x in data["performances"]])

    def enrich_performance(a_performance):
        calculator = create_performance_calculator(a_performance, play_for(a_performance))
        result = a_performance.copy()
        result["play"] = calculator.play
        result["amount"] = calculator.amount
        result["volume_credits"] = calculator.volume_credits
        return result

    result = dict()
    result["customer"] = invoice["customer"]
    result["performances"] = [enrich_performance(x) for x in invoice["performances"]]
    result["total_amount"] = total_amount(result)
    result["total_volume_credits"] = total_volume_credits(result)
    return result
