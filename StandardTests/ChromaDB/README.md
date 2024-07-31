### ChromaDB

To use ChromaDB, initialize the database connection with the required parameters:

```
import chromadb

vector_db = chromadb.ChromeDB(
    host='your_host', 
    port=5432, 
    database='your_database', 
    username='your_username', 
    password='your_password'
)
```
