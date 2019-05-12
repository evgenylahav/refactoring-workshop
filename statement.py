from create_statement_data import create_statement_data


def statement(invoice, plays):
    return _render_plain_text(create_statement_data(invoice, plays))


def html_statement(invoice, plays):
    return _render_html(create_statement_data(invoice, plays))


def _render_plain_text(data):
    result = "Statement for {}\n".format(data["customer"])
    for perf in data["performances"]:
        result += "  {}: {}({} seats)\n".\
            format(perf["play"]["name"], _usd(perf["amount"]), perf["audience"])

    result += "Amount owed is {}\n".format(_usd(data["total_amount"]))
    result += "You earned {} credits\n".format(data["total_volume_credits"])

    return result


def _render_html(data):
    result = "<h1>Statement for {}</h1>\n".format(data["customer"])
    result += "<table>\n"
    result += "<tr><th>play</th><th>seats</th><th>cost</th></tr>\n"
    for perf in data["performances"]:
        result += "  <tr><td>{}</td></tr>\n".format(perf["play"]["name"])
        result += "<td>{}</td></tr>\n".format(_usd(perf["amount"]))

    result += "</table>\n"
    result += "<p>Amount owed is <em>{}</em></p>\n".format(_usd(data["total_amount"]))
    result += "<p>You earned <em>{}</em> credits</p>\n".format(data["total_volume_credits"])
    return result


def _usd(a_number):
    return '${:,.2f}'.format(a_number/100)
