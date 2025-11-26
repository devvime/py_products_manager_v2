# APIRest with FatsAPI

### Run with Docker

```bash
docker compose up -d
```

### Create virtual env

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Init migrations

(venv)
```bash
alembic init migrations
```

### Create migration

(venv)
```bash
alembic revision --autogenerate -m "your migration message"
```

### Execute migration

(venv)
```bash
alembic upgrade head
```
### Migration rollback

(venv)
```bash
alembic downgrade -1
# alembic downgrade <VERSION_ID>
```