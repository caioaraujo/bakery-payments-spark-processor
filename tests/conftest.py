import csv

import pytest


@pytest.fixture(scope="session")
def payments():
    return [
        {
            "value": "1020.10",
            "expiration_date": "2020-07-01",
            "date_payment": "2020-06-01",
            "is_paid": True,
            "branch_id": 1,
        },
        {
            "value": "888.0",
            "expiration_date": "2020-02-01",
            "date_payment": "2020-10-01",
            "is_paid": False,
            "branch_id": 1,
        },
        {
            "value": "456.33",
            "expiration_date": "2020-02-01",
            "date_payment": "2020-01-01",
            "is_paid": True,
            "branch_id": 1,
        },
    ]


@pytest.fixture(scope="session")
def payments_csv(tmpdir_factory, payments):
    fn = tmpdir_factory.mktemp("data").join("payments.csv")
    with open(fn, 'w') as csvfile:
        fieldnames = ["value", "expiration_date", "date_payment", "is_paid", "branch_id"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(payments)

    return str(fn)
