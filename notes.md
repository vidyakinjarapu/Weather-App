### Note: 
- the Open-Meteo geocoder matches against multiple fields including
- postcodes, so numeric input may resolve to cities whose postcodes contain
- those digits (e.g. "123" → Vienna). Accepting this as expected behavior.

---
### Connecting to a database :
#### Our route  →  SQLAlchemy ORM(Python objects)  →  asyncpg driver (raw SQL)  →  PostgreSQL server


* SQLAlchemy — lets you treat tables as Python classes, queries as Python code (no raw SQL)
* asyncpg — the async PostgreSQL driver (the fast one)
* PostgreSQL — the actual database



