# Flask and MySQL

## For "dev" container

- api-dev
- db-dev

## For "test" container

- api-test
- db-test

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
