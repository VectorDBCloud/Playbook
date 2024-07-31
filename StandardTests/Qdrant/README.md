### Qdrant
To use Qdrant, initialize the database connection with the required parameters:

```
import qdrant

vector_db = qdrant.Qdrant(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```
