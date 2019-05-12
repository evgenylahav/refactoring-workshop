from performance_calculator_step7 import create_performance_calculator


def create_statement_data(invoice, plays):
    def play_for(a_performance):
        return plays[a_performance["playID"]]

    def total_amount(data):
        result = 0
        for perf in data["performances"]:
            result += perf['amount']
        return result

    def total_volume_credits(data):
        result = 0
        for perf in data["performances"]:
            result += perf["volume_credits"]
        return result

    def enrich_performance(a_performance):
        calculator = create_performance_calculator(a_performance, play_for(a_performance))
        result = a_performance.copy()
        result["play"] = calculator.play
        result["amount"] = calculator.amount()
        result["volume_credits"] = calculator.volume_credits()
        return result

    result = {}
    result['customer'] = invoice['customer']
    result['performances'] = list(map(enrich_performance, invoice['performances']))
    result["total_amount"] = total_amount(result)
    result["total_volume_credits"] = total_volume_credits(result)
    return result
