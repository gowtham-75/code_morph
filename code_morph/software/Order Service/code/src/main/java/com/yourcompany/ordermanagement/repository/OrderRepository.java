```java
package com.yourcompany.ordermanagement.repository;

import com.yourcompany.ordermanagement.model.Order;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
    // Custom repository methods can be added here if needed
}
```