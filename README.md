# bakery-payments-spark-processor
A data processing study based on Apache Spark 3.

## Requirements

- Python 3.8+
- Java with envvar `JAVA_HOME` setted

Optional:

- Pipenv
- Make

You can install all dependencies and creating a virtualenv with pipenv (https://pipenv.readthedocs.io/en/latest/install/)
by running:

`pipenv install`

Make a local copy of `local.env` file as `.env`. Once this project uses python-dotenv lib, all environment variables in .env value will be used in local running.

## Running 

Just run `processors.py` file as a regular python file: 

`python src/processors.py`

or with GNU make:

`make run`

## Tests

For tests running, you should install all development dependencies.<br>
Run all project tests with:

`pytest`
