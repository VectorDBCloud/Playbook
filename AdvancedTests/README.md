## Advanced Usage

This section covers advanced usage of the Vector Databases, including functions for searching, inserting, updating, and deleting vectors.

### pgvector

The following functions are available for advanced usage of pgvector:

* `pgvector.search(query, vector_db)`: Searches for vectors in the database that match the query.
	+ Example: `pgvector.search("hello world", vector_db)`
	+ Returns: A list of vectors that match the query
* `pgvector.insert(vector, vector_db)`: Inserts a new vector into the database.
	+ Example: `pgvector.insert([1, 2, 3], vector_db)`
	+ Returns: The ID of the newly inserted vector
* `pgvector.update(vector, vector_db)`: Updates an existing vector in the database.
	+ Example: `pgvector.update([1, 2, 3], vector_db)`
	+ Returns: The ID of the updated vector
* `pgvector.delete(vector, vector_db)`: Deletes a vector from the database.
	+ Example: `pgvector.delete([1, 2, 3], vector_db)`
	+ Returns: The ID of the deleted vector

### ChromaDB

The following functions are available for advanced usage of ChromaDB:

* `chromadb.search(query, vector_db)`: Searches for vectors in the database that match the query.
	+ Example: `chromadb.search("hello world", vector_db)`
	+ Returns: A list of vectors that match the query
* `chromadb.insert(vector, vector_db)`: Inserts a new vector into the database.
	+ Example: `chromadb.insert([1, 2, 3], vector_db)`
	+ Returns: The ID of the newly inserted vector
* `chromadb.update(vector, vector_db)`: Updates an existing vector in the database.
	+ Example: `chromadb.update([1, 2, 3], vector_db)`
	+ Returns: The ID of the updated vector
* `chromadb.delete(vector, vector_db)`: Deletes a vector from the database.
	+ Example: `chromadb.delete([1, 2, 3], vector_db)`
	+ Returns: The ID of the deleted vector

### Milvus

The following functions are available for advanced usage of Milvus:

* `milvus.search(query, vector_db)`: Searches for vectors in the database that match the query.
	+ Example: `milvus.search("hello world", vector_db)`
	+ Returns: A list of vectors that match the query
* `milvus.insert(vector, vector_db)`: Inserts a new vector into the database.
	+ Example: `milvus.insert([1, 2, 3], vector_db)`
	+ Returns: The ID of the newly inserted vector
* `milvus.update(vector, vector_db)`: Updates an existing vector in the database.
	+ Example: `milvus.update([1, 2, 3], vector_db)`
	+ Returns: The ID of the updated vector
* `milvus.delete(vector, vector_db)`: Deletes a vector from the database.
	+ Example: `milvus.delete([1, 2, 3], vector_db)`
	+ Returns: The ID of the deleted vector

### Qdrant

The following functions are available for advanced usage of Qdrant:

* `qdrant.search(query, vector_db)`: Searches for vectors in the database that match the query.
	+ Example: `qdrant.search("hello world", vector_db)`
	+ Returns: A list of vectors that match the query
* `qdrant.insert(vector, vector_db)`: Inserts a new vector into the database.
	+ Example: `qdrant.insert([1, 2, 3], vector_db)`
	+ Returns: The ID of the newly inserted vector
* `qdrant.update(vector, vector_db)`: Updates an existing vector in the database.
	+ Example: `qdrant.update([1, 2, 3], vector_db)`
	+ Returns: The ID of the updated vector
* `qdrant.delete(vector, vector_db)`: Deletes a vector from the database.
	+ Example: `qdrant.delete([1, 2, 3], vector_db)`
	+ Returns: The ID of the deleted vector
