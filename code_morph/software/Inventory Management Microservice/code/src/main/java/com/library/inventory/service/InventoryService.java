```java
package com.library.inventory.service;

import com.library.inventory.model.Book;
import com.library.inventory.model.Video;
import com.library.inventory.repository.BookRepository;
import com.library.inventory.repository.VideoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class InventoryService {

    private final BookRepository bookRepository;
    private final VideoRepository videoRepository;

    @Autowired
    public InventoryService(BookRepository bookRepository, VideoRepository videoRepository) {
        this.bookRepository = bookRepository;
        this.videoRepository = videoRepository;
    }

    public Book addItem(Book book) {
        return bookRepository.save(book);
    }

    public Video addItem(Video video) {
        return videoRepository.save(video);
    }

    public Book updateItem(String itemId, Book book) {
        book.setId(itemId);
        return bookRepository.save(book);
    }

    public Video updateItem(String itemId, Video video) {
        video.setId(itemId);
        return videoRepository.save(video);
    }

    public void removeItem(String itemId, Class<?> itemType) {
        if (itemType == Book.class) {
            bookRepository.deleteById(itemId);
        } else if (itemType == Video.class) {
            videoRepository.deleteById(itemId);
        }
    }

    public Optional<Book> getBook(String itemId) {
        return bookRepository.findById(itemId);
    }

    public Optional<Video> getVideo(String itemId) {
        return videoRepository.findById(itemId);
    }
}
```