from processors import PaidPaymentsProcessor


class TestPaidPaymentsProcessor:

    def test_processor(self, capsys):
        app_name = "TestBakeryPayments"
        PaidPaymentsProcessor(app_name).process()

        captured = capsys.readouterr()
        assert "Payments paid: 3, payments not paid: 5" in captured.out
