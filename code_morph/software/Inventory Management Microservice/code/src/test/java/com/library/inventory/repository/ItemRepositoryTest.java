```java
package com.library.inventory.repository;

import com.library.inventory.model.Book;
import com.library.inventory.model.Video;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@DataJpaTest
public class ItemRepositoryTest {

    @Mock
    private BookRepository bookRepository;

    @Mock
    private VideoRepository videoRepository;

    @InjectMocks
    private ItemRepository itemRepository;

    private Book testBook;
    private Video testVideo;

    @BeforeEach
    public void setUp() {
        testBook = new Book();
        testBook.setId("1");
        testBook.setTitle("Effective Java");
        testBook.setAuthor("Joshua Bloch");
        testBook.setIsbn("0134685997");
        testBook.setLocationId("L1");
        testBook.setBranchId("B1");

        testVideo = new Video();
        testVideo.setId("2");
        testVideo.setTitle("The Matrix");
        testVideo.setDirector("Lana Wachowski, Lilly Wachowski");
        testVideo.setGenre("Sci-Fi");
        testVideo.setLocationId("L2");
        testVideo.setBranchId("B2");
    }

    @Test
    public void whenFindById_thenReturnBook() {
        when(bookRepository.findById(testBook.getId())).thenReturn(Optional.of(testBook));
        Optional<Book> foundBook = bookRepository.findById(testBook.getId());
        verify(bookRepository).findById(testBook.getId());
        assertEquals(testBook, foundBook.orElse(null));
    }

    @Test
    public void whenFindById_thenReturnVideo() {
        when(videoRepository.findById(testVideo.getId())).thenReturn(Optional.of(testVideo));
        Optional<Video> foundVideo = videoRepository.findById(testVideo.getId());
        verify(videoRepository).findById(testVideo.getId());
        assertEquals(testVideo, foundVideo.orElse(null));
    }

    @Test
    public void whenSaveBook_thenBookShouldBeSaved() {
        when(bookRepository.save(any(Book.class))).thenReturn(testBook);
        Book savedBook = bookRepository.save(testBook);
        verify(bookRepository).save(testBook);
        assertEquals(testBook, savedBook);
    }

    @Test
    public void whenSaveVideo_thenVideoShouldBeSaved() {
        when(videoRepository.save(any(Video.class))).thenReturn(testVideo);
        Video savedVideo = videoRepository.save(testVideo);
        verify(videoRepository).save(testVideo);
        assertEquals(testVideo, savedVideo);
    }

    @Test
    public void whenDeleteById_thenBookShouldBeDeleted() {
        doNothing().when(bookRepository).deleteById(testBook.getId());
        bookRepository.deleteById(testBook.getId());
        verify(bookRepository).deleteById(testBook.getId());
    }

    @Test
    public void whenDeleteById_thenVideoShouldBeDeleted() {
        doNothing().when(videoRepository).deleteById(testVideo.getId());
        videoRepository.deleteById(testVideo.getId());
        verify(videoRepository).deleteById(testVideo.getId());
    }
}
```