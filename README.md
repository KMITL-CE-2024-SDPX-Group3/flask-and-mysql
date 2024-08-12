# Flask and MySQL

## For "dev" container

| Container Name | Local Port | Container Port |
| -------------- | ---------- | -------------- |
| api-dev        | 8081       | 5000           |
| db-dev         | 3310       | 3306           |

## For "test" container

| Container Name | Local Port | Container Port |
| -------------- | ---------- | -------------- |
| api-test       | 8082       | 5000           |
| db-test        | 3311       | 3306           |

## Start running

- Dockerfile.dev and docker-compose.dev use for develop

### Start container

```bash
docker compose up -d
```

### Stop container

```bash
docker compose down
```

### After edit Dockerfile, run this command

```bash
docker compose up -d --build
```

## Test API (for "dev" api)

### Base URL

```url
http://localhost:8081
```

### GET user [GET]

```url
http://localhost:8081/user/<user-id>
```

### CREATE user [POST]

user information format

```json
{
  "name": "John Doe",
  "age": 28
}
```

```url
http://localhost:8081/user
```
