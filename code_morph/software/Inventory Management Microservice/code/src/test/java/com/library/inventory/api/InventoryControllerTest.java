```java
package com.library.inventory.api;

import com.library.inventory.dto.BookDTO;
import com.library.inventory.dto.VideoDTO;
import com.library.inventory.service.InventoryService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class InventoryControllerTest {

    @Mock
    private InventoryService inventoryService;

    @InjectMocks
    private InventoryController inventoryController;

    private BookDTO bookDTO;
    private VideoDTO videoDTO;

    @BeforeEach
    void setUp() {
        bookDTO = new BookDTO();
        bookDTO.setId("1");
        bookDTO.setTitle("The Great Gatsby");
        bookDTO.setAuthor("F. Scott Fitzgerald");
        bookDTO.setIsbn("1234567890");
        bookDTO.setLocationId("1");
        bookDTO.setBranchId("1");

        videoDTO = new VideoDTO();
        videoDTO.setId("2");
        videoDTO.setTitle("Inception");
        videoDTO.setDirector("Christopher Nolan");
        videoDTO.setGenre("Sci-Fi");
        videoDTO.setLocationId("2");
        videoDTO.setBranchId("2");
    }

    @Test
    void testGetItems() {
        when(inventoryService.getItems()).thenReturn(Arrays.asList(bookDTO, videoDTO));
        ResponseEntity<List<Object>> response = inventoryController.getItems();
        assertEquals(2, response.getBody().size());
        verify(inventoryService, times(1)).getItems();
    }

    @Test
    void testAddBook() {
        when(inventoryService.addItem(bookDTO)).thenReturn(bookDTO);
        ResponseEntity<Object> response = inventoryController.addBook(bookDTO);
        assertEquals(bookDTO, response.getBody());
        verify(inventoryService, times(1)).addItem(bookDTO);
    }

    @Test
    void testAddVideo() {
        when(inventoryService.addItem(videoDTO)).thenReturn(videoDTO);
        ResponseEntity<Object> response = inventoryController.addVideo(videoDTO);
        assertEquals(videoDTO, response.getBody());
        verify(inventoryService, times(1)).addItem(videoDTO);
    }

    @Test
    void testUpdateItem() {
        when(inventoryService.updateItem("1", bookDTO)).thenReturn(bookDTO);
        ResponseEntity<Object> response = inventoryController.updateItem("1", bookDTO);
        assertEquals(bookDTO, response.getBody());
        verify(inventoryService, times(1)).updateItem("1", bookDTO);
    }

    @Test
    void testDeleteItem() {
        doNothing().when(inventoryService).removeItem("1");
        ResponseEntity<Object> response = inventoryController.deleteItem("1");
        assertEquals(ResponseEntity.ok().build(), response);
        verify(inventoryService, times(1)).removeItem("1");
    }
}
```