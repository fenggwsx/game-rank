# Game-rank
A simple game rank backend based on Flask.

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
