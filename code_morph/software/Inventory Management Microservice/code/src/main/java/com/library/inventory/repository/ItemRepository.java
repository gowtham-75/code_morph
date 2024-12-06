```java
package com.library.inventory.repository;

import com.library.inventory.model.Book;
import com.library.inventory.model.Video;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ItemRepository extends JpaRepository<Book, String> {
    Optional<Book> findBookById(String id);
    Optional<Video> findVideoById(String id);
    <S extends Book> S save(S entity);
    <S extends Video> S save(S entity);
    void deleteBookById(String id);
    void deleteVideoById(String id);
}
```