```java
package com.yourcompany.librarymanagementsystem.controller;

import com.yourcompany.librarymanagementsystem.model.Book;
import com.yourcompany.librarymanagementsystem.model.Video;
import com.yourcompany.librarymanagementsystem.service.ItemService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

class ItemControllerTest {

    @InjectMocks
    private ItemController itemController;

    @Mock
    private ItemService itemService;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void getAllItems() {
        // Arrange
        Book book = new Book();
        book.setId("1");
        Video video = new Video();
        video.setId("2");
        List<Object> expectedItems = Arrays.asList(book, video);
        when(itemService.listItems()).thenReturn(expectedItems);

        // Act
        ResponseEntity<List<Object>> response = itemController.getAllItems();

        // Assert
        assertEquals(expectedItems, response.getBody());
        verify(itemService).listItems();
    }

    @Test
    void addItem() {
        // Arrange
        Book book = new Book();
        book.setId("1");
        when(itemService.createItem(any(Book.class))).thenReturn(book);

        // Act
        ResponseEntity<Object> response = itemController.addItem(book);

        // Assert
        assertEquals(book, response.getBody());
        verify(itemService).createItem(any(Book.class));
    }

    @Test
    void updateItem() {
        // Arrange
        Book book = new Book();
        book.setId("1");
        when(itemService.modifyItem(eq("1"), any(Book.class))).thenReturn(book);

        // Act
        ResponseEntity<Object> response = itemController.updateItem("1", book);

        // Assert
        assertEquals(book, response.getBody());
        verify(itemService).modifyItem(eq("1"), any(Book.class));
    }

    @Test
    void deleteItem() {
        // Arrange
        doNothing().when(itemService).removeItem("1");

        // Act
        ResponseEntity<Void> response = itemController.deleteItem("1");

        // Assert
        assertEquals(204, response.getStatusCodeValue());
        verify(itemService).removeItem("1");
    }

    @Test
    void getItemById() {
        // Arrange
        Book book = new Book();
        book.setId("1");
        when(itemService.fetchItemById("1")).thenReturn(book);

        // Act
        ResponseEntity<Object> response = itemController.getItemById("1");

        // Assert
        assertEquals(book, response.getBody());
        verify(itemService).fetchItemById("1");
    }
}
```