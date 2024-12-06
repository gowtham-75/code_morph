```java
package com.yourcompany.librarymanagementsystem.repository;

import com.yourcompany.librarymanagementsystem.model.Book;
import com.yourcompany.librarymanagementsystem.model.Item;
import com.yourcompany.librarymanagementsystem.model.Video;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.dao.DataIntegrityViolationException;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertThrows;

@DataJpaTest
public class ItemRepositoryTest {

    @Autowired
    private ItemRepository itemRepository;

    private Book book;
    private Video video;

    @BeforeEach
    public void setUp() {
        book = new Book();
        book.setTitle("Effective Java");
        book.setAuthor("Joshua Bloch");
        book.setIsbn("978-0134685991");

        video = new Video();
        video.setTitle("The Matrix");
        video.setDirector("Lana Wachowski, Lilly Wachowski");
        video.setGenre("Action");
    }

    @Test
    public void whenSaveItem_thenItCanBeRetrieved() {
        itemRepository.save(book);
        Optional<Item> retrievedBook = itemRepository.findById(book.getId());
        assertThat(retrievedBook).isNotEmpty();
        assertThat(retrievedBook.get().getTitle()).isEqualTo(book.getTitle());

        itemRepository.save(video);
        Optional<Item> retrievedVideo = itemRepository.findById(video.getId());
        assertThat(retrievedVideo).isNotEmpty();
        assertThat(retrievedVideo.get().getTitle()).isEqualTo(video.getTitle());
    }

    @Test
    public void whenSaveItemWithDuplicateId_thenThrowException() {
        itemRepository.save(book);
        Book anotherBook = new Book();
        anotherBook.setId(book.getId());
        anotherBook.setTitle("Java Concurrency in Practice");
        anotherBook.setAuthor("Brian Goetz");

        assertThrows(DataIntegrityViolationException.class, () -> itemRepository.save(anotherBook));
    }

    @Test
    public void whenDeleteItem_thenItShouldBeRemoved() {
        itemRepository.save(book);
        assertThat(itemRepository.findById(book.getId())).isNotEmpty();
        itemRepository.deleteById(book.getId());
        assertThat(itemRepository.findById(book.getId())).isEmpty();
    }

    @Test
    public void whenUpdateItem_thenItShouldBeUpdated() {
        itemRepository.save(book);
        Optional<Item> retrievedBook = itemRepository.findById(book.getId());
        assertThat(retrievedBook).isNotEmpty();
        Book updatedBook = (Book) retrievedBook.get();
        updatedBook.setTitle("Effective Java 2nd Edition");
        itemRepository.save(updatedBook);

        Optional<Item> updatedRetrievedBook = itemRepository.findById(book.getId());
        assertThat(updatedRetrievedBook).isNotEmpty();
        assertThat(updatedRetrievedBook.get().getTitle()).isEqualTo("Effective Java 2nd Edition");
    }
}
```