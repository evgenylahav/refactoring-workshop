import unittest
from statement import statement, html_statement


class TestStatement(unittest.TestCase):
    def setUp(self):
        self.plays = {
            "hamlet": {"name": "Hamlet", "type": "tragedy"},
            "as-like": {"name": "As You Like It", "type": "comedy"},
            "othello": {"name": "Othello", "type": "tragedy"}
        }

        self.err_plays = {
            "hamlet": {"name": "Kodon", "type": "family"},
        }

        self.invoices = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 55
                },
                {
                    "playID": "as-like",
                    "audience": 35
                },
                {
                    "playID": "othello",
                    "audience": 40
                }
            ]
        }

        self.statement_result = "Statement for BigCo\n" \
                                "  Hamlet: $650.00(55 seats)\n" \
                                "  As You Like It: $490.00(35 seats)\n"\
                                "  Othello: $500.00(40 seats)\n"\
                                "Amount owed is $1,640.00\n"\
                                "You earned 47 credits\n"

        self.html_statement_result = "<h1>Statement for BigCo</h1>\n" \
                                     "<table>\n" \
                                     "<tr><th>play</th><th>seats</th><th>cost</th></tr>\n" \
                                     "  <tr><td>Hamlet</td></tr>\n" \
                                     "<td>$650.00</td></tr>\n" \
                                     "  <tr><td>As You Like It</td></tr>\n" \
                                     "<td>$490.00</td></tr>\n" \
                                     "  <tr><td>Othello</td></tr>\n" \
                                     "<td>$500.00</td></tr>\n" \
                                     "</table>\n" \
                                     "<p>Amount owed is <em>$1,640.00</em></p>\n" \
                                     "<p>You earned <em>47</em> credits</p>\n"

    def test_statement(self):
        self.assertEqual(statement(self.invoices, self.plays), self.statement_result)

    def test_html_statement(self):
        self.assertEqual(html_statement(self.invoices, self.plays), self.html_statement_result)

    def test_error_statement(self):
        with self.assertRaisesRegex(ValueError, "unknown type: family"):
            statement(self.invoices, self.err_plays)
