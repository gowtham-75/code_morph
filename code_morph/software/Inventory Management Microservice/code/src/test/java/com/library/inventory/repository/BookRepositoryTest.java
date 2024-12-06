```java
package com.library.inventory.repository;

import com.library.inventory.model.Book;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;

@DataJpaTest
public class BookRepositoryTest {
    
    @Autowired
    private TestEntityManager entityManager;
    
    @Autowired
    private BookRepository bookRepository;
    
    private Book book;
    
    @BeforeEach
    public void setUp() {
        book = new Book();
        book.setTitle("Effective Java");
        book.setAuthor("Joshua Bloch");
        book.setIsbn("978-0134685991");
        book.setLocationId("1");
        book.setBranchId("1");
        entityManager.persist(book);
        entityManager.flush();
    }
    
    @Test
    public void whenFindById_thenReturnBook() {
        // given
        Long id = book.getId();
        
        // when
        Optional<Book> found = bookRepository.findById(id);
        
        // then
        assertThat(found.isPresent()).isTrue();
        assertThat(found.get().getTitle()).isEqualTo(book.getTitle());
    }
    
    @Test
    public void whenSave_thenPersistBook() {
        // given
        Book newBook = new Book();
        newBook.setTitle("Clean Code");
        newBook.setAuthor("Robert C. Martin");
        newBook.setIsbn("978-0132350884");
        newBook.setLocationId("2");
        newBook.setBranchId("1");
        
        // when
        Book savedBook = bookRepository.save(newBook);
        
        // then
        assertThat(savedBook).isNotNull();
        assertThat(savedBook.getId()).isNotNull();
        assertThat(savedBook.getTitle()).isEqualTo(newBook.getTitle());
    }
    
    @Test
    public void whenDeleteById_thenRemoveBook() {
        // given
        Long id = book.getId();
        
        // when
        bookRepository.deleteById(id);
        
        // then
        Optional<Book> deleted = bookRepository.findById(id);
        assertThat(deleted.isPresent()).isFalse();
    }
}
```