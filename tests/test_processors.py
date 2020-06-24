from processors import PaidPaymentsProcessor


class TestPaidPaymentsProcessor:

    def test_processor(self, capsys, payments_csv):
        app_name = "TestBakeryPayments"
        PaidPaymentsProcessor(app_name).process(payments_csv)

        captured = capsys.readouterr()
        assert "Payments paid: 2, payments not paid: 1" in captured.out
