### pgvector

To use pgvector, initialize the database connection with the required parameters:

```
python
import pgvector

vector_db = pgvector.PgVector(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```
