```java
package com.library.inventory.repository;

import com.library.inventory.model.Video;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface VideoRepository extends JpaRepository<Video, String> {
    // Custom repository methods can be added here if necessary
}
```