```java
package com.yourcompany.repository;

import com.yourcompany.domain.Customer;
import java.util.Optional;

public interface CustomerRepository {
    Optional<Customer> findByCustomerId(String customerId);
    Customer save(Customer customer);
    void delete(Customer customer);
}
```