### Milvus
To use Milvus, initialize the database connection with the required parameters:

```
import milvus

vector_db = milvus.Milvus(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```
