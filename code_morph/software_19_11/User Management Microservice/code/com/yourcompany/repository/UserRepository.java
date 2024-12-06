```java
package com.yourcompany.repository;

import com.yourcompany.domain.User;
import java.util.Optional;

public interface UserRepository {
    Optional<User> findById(String id);
    User save(User user);
    void delete(User user);
}
```