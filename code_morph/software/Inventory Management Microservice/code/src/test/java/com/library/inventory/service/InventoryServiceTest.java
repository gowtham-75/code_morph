```java
package com.library.inventory.service;

import com.library.inventory.model.Book;
import com.library.inventory.model.Video;
import com.library.inventory.repository.BookRepository;
import com.library.inventory.repository.VideoRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.util.Optional;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

class InventoryServiceTest {

    @InjectMocks
    private InventoryService inventoryService;

    @Mock
    private BookRepository bookRepository;

    @Mock
    private VideoRepository videoRepository;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void addItem_Book() {
        Book book = new Book();
        book.setTitle("Test Book");
        book.setAuthor("Test Author");
        book.setIsbn("1234567890");
        book.setLocationId("1");
        book.setBranchId("1");

        when(bookRepository.save(any(Book.class))).thenReturn(book);

        Book savedBook = inventoryService.addItem(book);

        assertEquals(book.getTitle(), savedBook.getTitle());
        verify(bookRepository, times(1)).save(book);
    }

    @Test
    void addItem_Video() {
        Video video = new Video();
        video.setTitle("Test Video");
        video.setDirector("Test Director");
        video.setGenre("Test Genre");
        video.setLocationId("1");
        video.setBranchId("1");

        when(videoRepository.save(any(Video.class))).thenReturn(video);

        Video savedVideo = inventoryService.addItem(video);

        assertEquals(video.getTitle(), savedVideo.getTitle());
        verify(videoRepository, times(1)).save(video);
    }

    @Test
    void updateItem_Book() {
        Book book = new Book();
        book.setId("1");
        book.setTitle("Updated Book");
        book.setAuthor("Updated Author");
        book.setIsbn("0987654321");
        book.setLocationId("2");
        book.setBranchId("2");

        when(bookRepository.findById(any(String.class))).thenReturn(Optional.of(book));
        when(bookRepository.save(any(Book.class))).thenReturn(book);

        Book updatedBook = inventoryService.updateItem(book.getId(), book);

        assertEquals(book.getTitle(), updatedBook.getTitle());
        verify(bookRepository, times(1)).save(book);
    }

    @Test
    void updateItem_Video() {
        Video video = new Video();
        video.setId("1");
        video.setTitle("Updated Video");
        video.setDirector("Updated Director");
        video.setGenre("Updated Genre");
        video.setLocationId("2");
        video.setBranchId("2");

        when(videoRepository.findById(any(String.class))).thenReturn(Optional.of(video));
        when(videoRepository.save(any(Video.class))).thenReturn(video);

        Video updatedVideo = inventoryService.updateItem(video.getId(), video);

        assertEquals(video.getTitle(), updatedVideo.getTitle());
        verify(videoRepository, times(1)).save(video);
    }

    @Test
    void removeItem_Book() {
        String bookId = "1";
        doNothing().when(bookRepository).deleteById(bookId);
        inventoryService.removeItem(bookId);
        verify(bookRepository, times(1)).deleteById(bookId);
    }

    @Test
    void removeItem_Video() {
        String videoId = "1";
        doNothing().when(videoRepository).deleteById(videoId);
        inventoryService.removeItem(videoId);
        verify(videoRepository, times(1)).deleteById(videoId);
    }

    @Test
    void getItem_Book() {
        String bookId = "1";
        Book book = new Book();
        book.setId(bookId);
        book.setTitle("Test Book");
        book.setAuthor("Test Author");
        book.setIsbn("1234567890");
        book.setLocationId("1");
        book.setBranchId("1");

        when(bookRepository.findById(bookId)).thenReturn(Optional.of(book));

        Optional<Book> foundBook = inventoryService.getItem(bookId);

        assertEquals(book.getTitle(), foundBook.orElse(new Book()).getTitle());
        verify(bookRepository, times(1)).findById(bookId);
    }

    @Test
    void getItem_Video() {
        String videoId = "1";
        Video video = new Video();
        video.setId(videoId);
        video.setTitle("Test Video");
        video.setDirector("Test Director");
        video.setGenre("Test Genre");
        video.setLocationId("1");
        video.setBranchId("1");

        when(videoRepository.findById(videoId)).thenReturn(Optional.of(video));

        Optional<Video> foundVideo = inventoryService.getItem(videoId);

        assertEquals(video.getTitle(), foundVideo.orElse(new Video()).getTitle());
        verify(videoRepository, times(1)).findById(videoId);
    }
}
```