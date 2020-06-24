from pyspark.sql import SparkSession


class PaidPaymentsProcessor:

    def __init__(self, app_name="BakeryPayments"):
        self.app_name = app_name

    def process(self):
        payments = "./data/payments/payments.csv"
        spark = SparkSession.builder.appName(self.app_name).getOrCreate()
        payment_data = spark.read.text(payments).cache()

        paid = payment_data.filter(payment_data.value.contains('True')).count()
        not_paid = payment_data.filter(payment_data.value.contains('False')).count()

        print("Payments paid: %i, payments not paid: %i" % (paid, not_paid))

        spark.stop()


if __name__ == '__main__':
    PaidPaymentsProcessor().process()
