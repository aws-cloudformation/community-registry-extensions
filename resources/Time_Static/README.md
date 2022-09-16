# AwsCommunity::Time::Static

Creates a static time with the following properties:

## Properties
None

## Attributes
The following properties you can use in a `GetAtt`

| Attribute  | Type | Description |
| ------------- | ------------- | ------------- |
| **Id**  | string  | UTC returns the time in UTC format.
| **Day**  | integer  | Day returns the day of the month.
| **Hour** | integer  | Hour returns the hour within the day, in the range [0, 23].
| **Minute** | integer  | Minute returns the minute offset within the hour, in the range [0, 59].
| **Month** | integer  | Month returns the month of the year.
| **Second** | integer  | Second returns the second offset within the minute, in the range [0, 59].
| **Unix** | integer  | Unix returns a Unix time, the number of seconds elapsed since January 1, 1970 UTC.
| **Year** | integer  | Year returns the year.


## Development

Open two tabs in your terminal.

Create a virtual environment.

```sh
cd resources/Time_Static
python3 -m venv .env
source .env/bin/activate
pip install -r src/requirements.txt
sam local start-lambda
```

In another tab, run cfn test:

```sh
cd resources/Time_Static
source .env/bin/activaate
cfn test -- -k "contract_create_delete or contract_create_create or contract_create_read or contract_check_asserts_work"
```
