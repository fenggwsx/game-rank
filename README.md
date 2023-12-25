# Game-rank

A simple game rank backend based on Flask and Sqlite3.

## How to Use

- \[Optional\] Create a python virtual environment.
- Install Python3 and Sqlite3 if not installed
- Change your directory to this project
- \[Optional\] Activate the virtual environment if you have prepared one
- Install these packages: `flask`, `flask_restful`, `gunicorn`
- Execute this command: `gunicorn app:app`
- Enjoy the backend!

## APIs

### Get All the Players' Time-usages in a Specific Checkpoint

- Request URL

> /rank/\<checkpoint\>

- Request Method

> GET

- Return Parameters

> | Return Parameter | Parameter Type | Desciption         |
> | ---------------- | -------------- | ------------------ |
> | code             | Integer        | whether successful |
> | message          | String         | information        |
> | data             | List           | result data        |

### Update a Player's Time-usage in a Specific Checkpoint

- Request URL

> /rank/\<checkpoint\>

- Request Method

> POST

- Request Parameters

> | Request Parameter | Parameter Type   | Desciption         |
> | ----------------- | ---------------- | ------------------ |
> | username          | String, not null | in the json file   |
> | checkpoint        | String, not null | in the url path    |
> | time              | Float, not null  | in the json file   |

- Return Parameters

> | Return Parameter | Parameter Type | Desciption         |
> | ---------------- | -------------- | ------------------ |
> | code             | Integer        | whether successful |
> | message          | String         | information        |
> | data             | None           |                    |
