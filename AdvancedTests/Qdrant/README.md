# Advanced Tests for Qdrant

This folder contains advanced test scenarios and usage examples for Qdrant, focusing on complex operations and optimizations. These tests explore the advanced capabilities of Qdrant and provide guidance on maximizing its performance and functionality.

## Introduction

The advanced tests for Qdrant include scenarios such as performance benchmarking, handling complex queries, optimizing indexing strategies, and testing scalability. These scenarios are designed to evaluate the database's advanced features and explore its limits under various conditions.

## Test Scenarios

### Create a Tenant with Custom Permissions
- **Purpose**: Demonstrates how to create tenants with custom permissions.
- **File**: `CreateATenantWithCustomPermissions.py`

### Delete Collection with Custom Logic
- **Purpose**: Shows how to delete collections using custom logic.
- **File**: `DeleteCollectionWithCustomLogic.py`

### Get Collection with Custom Filter
- **Purpose**: Retrieves collections using custom filters for more specific queries.
- **File**: `GetCollectionWithCustomFilter.py`

### Search with Custom Query
- **Purpose**: Illustrates how to perform searches using custom query logic.
- **File**: `SearchWithCustomQuery.py`

### Upsert with Custom Logic
- **Purpose**: Demonstrates upsert operations with custom logic.
- **File**: `UpsertWithCustomLogic.py`

## Advanced Functions

### Searching
- **`qdrant.advanced_search(query, vector_db)`**: Performs complex searches using detailed criteria.
  - **Example**: `qdrant.advanced_search("advanced NLP queries", vector_db)`
  - **Returns**: A list of results matching the query.

### Insertion
- **`qdrant.insert_advanced(vector, vector_db)`**: Inserts a vector with additional metadata for advanced usage.
  - **Example**: `qdrant.insert_advanced([0.1, 0.5, 0.3], vector_db)`
  - **Returns**: The ID of the inserted vector.

### Update
- **`qdrant.update_vector(vector_id, new_data, vector_db)`**: Updates an existing vector in the database.
  - **Example**: `qdrant.update_vector(123, [0.2, 0.6, 0.4], vector_db)`
  - **Returns**: The ID of the updated vector.

### Deletion
- **`qdrant.delete_vector(vector_id, vector_db)`**: Deletes a vector from the database.
  - **Example**: `qdrant.delete_vector(123, vector_db)`
  - **Returns**: Confirmation of deletion.

## Contribution and Feedback

We welcome contributions to enhance these advanced test scenarios. Please refer to our Contribution Guidelines for more information. If you encounter any issues or have suggestions, please use the issue tracker.

## License

This content is licensed under the MIT License. See the LICENSE file for more details.
