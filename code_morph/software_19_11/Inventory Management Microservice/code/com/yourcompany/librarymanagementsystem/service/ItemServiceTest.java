```java
package com.yourcompany.librarymanagementsystem.service;

import com.yourcompany.librarymanagementsystem.model.Book;
import com.yourcompany.librarymanagementsystem.model.Item;
import com.yourcompany.librarymanagementsystem.model.Video;
import com.yourcompany.librarymanagementsystem.repository.ItemRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.util.Optional;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

class ItemServiceTest {

    @Mock
    private ItemRepository itemRepository;

    @InjectMocks
    private ItemService itemService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void listItems_ShouldReturnAllItems() {
        when(itemRepository.findAll()).thenReturn(List.of(new Book(), new Video()));
        List<Item> items = itemService.listItems();
        assertEquals(2, items.size());
        verify(itemRepository, times(1)).findAll();
    }

    @Test
    void createItem_ShouldSaveBookItem() {
        Book book = new Book();
        when(itemRepository.save(book)).thenReturn(book);
        Item savedItem = itemService.createItem(book);
        assertEquals(book, savedItem);
        verify(itemRepository, times(1)).save(book);
    }

    @Test
    void createItem_ShouldSaveVideoItem() {
        Video video = new Video();
        when(itemRepository.save(video)).thenReturn(video);
        Item savedItem = itemService.createItem(video);
        assertEquals(video, savedItem);
        verify(itemRepository, times(1)).save(video);
    }

    @Test
    void modifyItem_ShouldUpdateItem() {
        String itemId = "1";
        Book book = new Book();
        book.setId(itemId);
        when(itemRepository.findById(itemId)).thenReturn(Optional.of(book));
        when(itemRepository.save(book)).thenReturn(book);
        Item updatedItem = itemService.modifyItem(itemId, book);
        assertEquals(book, updatedItem);
        verify(itemRepository, times(1)).save(book);
    }

    @Test
    void removeItem_ShouldDeleteItem() {
        String itemId = "1";
        doNothing().when(itemRepository).deleteById(itemId);
        itemService.removeItem(itemId);
        verify(itemRepository, times(1)).deleteById(itemId);
    }

    @Test
    void fetchItemById_ShouldReturnItem() {
        String itemId = "1";
        Book book = new Book();
        book.setId(itemId);
        when(itemRepository.findById(itemId)).thenReturn(Optional.of(book));
        Item item = itemService.fetchItemById(itemId);
        assertEquals(book, item);
        verify(itemRepository, times(1)).findById(itemId);
    }
}
```