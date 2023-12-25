# Game-rank
a simple game rank backend based on Flask

## APIs

### Get All the Players' Time-usages in a Specific Level

- Request URL

> /rank/<level>

- Request Method

> GET

- Return Value

> | Return Parameter | Parameter Type | Desciption         |
> | ---------------- | -------------- | ------------------ |
> | code             | Integer        | whether successful |
> | message          | String         | information        |
> | data             | List           | result data        |
