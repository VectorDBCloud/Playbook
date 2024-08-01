# Advanced Tests for ChromaDB

This folder contains advanced test scenarios and usage examples for ChromaDB, focusing on complex operations and optimizations. These tests explore the advanced capabilities of ChromaDB and provide guidance on maximizing its potential.

## Introduction

The advanced tests for ChromaDB include scenarios for performance benchmarking, complex query handling, indexing strategies, and scalability testing. These tests are designed to challenge the database under various conditions and help users understand its limits and strengths.

## Test Scenarios

### Create a Tenant with Custom Permissions
- **Purpose**: Demonstrates how to create tenants with custom permissions.
- **File**: `CreateATenantWithCustomPermissions.py`

### Search with Custom Query
- **Purpose**: Illustrates how to perform searches using custom query logic.
- **File**: `SearchWithCustomQuery.py`

### Upsert with Custom Logic
- **Purpose**: Shows how to implement upsert operations with custom logic.
- **File**: `UpsertWithCustomLogic.py`

## Advanced Functions

### Searching
- **`chromadb.advanced_search(query, vector_db)`**: Conducts advanced searches using complex criteria.
  - **Example**: `chromadb.advanced_search("deep learning models", vector_db)`
  - **Returns**: A list of search results matching the query.

### Insertion
- **`chromadb.insert_advanced(vector, vector_db)`**: Inserts a vector with additional metadata for advanced usage.
  - **Example**: `chromadb.insert_advanced([0.1, 0.5, 0.3], vector_db)`
  - **Returns**: The ID of the inserted vector.

### Update
- **`chromadb.update_vector(vector_id, new_data, vector_db)`**: Updates an existing vector's data.
  - **Example**: `chromadb.update_vector(123, [0.2, 0.6, 0.4], vector_db)`
  - **Returns**: The ID of the updated vector.

### Deletion
- **`chromadb.delete_vector(vector_id, vector_db)`**: Deletes a vector from the database.
  - **Example**: `chromadb.delete_vector(123, vector_db)`
  - **Returns**: Confirmation of deletion.


## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you have any issues or suggestions, feel free to use the issue tracker.


## License

This content is licensed under the MIT License. See the LICENSE file for more details.
