```java
package com.yourcompany.librarymanagementsystem.repository;

import com.yourcompany.librarymanagementsystem.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ItemRepository extends JpaRepository<Item, Long> {
    // The JpaRepository interface already provides basic CRUD operations.
    // Additional custom database operations can be defined here if needed.
}
```