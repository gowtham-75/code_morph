```java
package com.library.inventory.repository;

import com.library.inventory.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookRepository extends JpaRepository<Book, String> {
    // This interface will automatically be implemented by Spring Data JPA with basic CRUD operations.
    // Additional custom queries can be defined here if needed.
}
```