from pyspark.sql import SparkSession

payments = "../data/payments/payments.csv"
spark = SparkSession.builder.appName("BakeryPayments").getOrCreate()
payment_data = spark.read.text(payments).cache()

paid = payment_data.filter(payment_data.value.contains('True')).count()
not_paid = payment_data.filter(payment_data.value.contains('False')).count()

print("Payments paid: %i, payments not paid: %i" % (paid, not_paid))

spark.stop()
