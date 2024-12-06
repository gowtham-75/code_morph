```java
package com.library.inventory.integration;

import com.library.inventory.api.dto.BookDTO;
import com.library.inventory.api.dto.VideoDTO;
import com.library.inventory.model.Book;
import com.library.inventory.model.Video;
import com.library.inventory.service.InventoryService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
public class InventoryIntegrationTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private InventoryService inventoryService;

    @Autowired
    private WebApplicationContext webApplicationContext;

    @BeforeEach
    public void setup() {
        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
    }

    @Test
    public void testAddBook() throws Exception {
        BookDTO bookDTO = new BookDTO();
        bookDTO.setTitle("The Hobbit");
        bookDTO.setAuthor("J.R.R. Tolkien");
        bookDTO.setIsbn("978-0-395-19395-8");
        bookDTO.setLocationId("1");
        bookDTO.setBranchId("1");

        mockMvc.perform(post("/items/books")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"title\":\"The Hobbit\",\"author\":\"J.R.R. Tolkien\",\"isbn\":\"978-0-395-19395-8\",\"locationId\":\"1\",\"branchId\":\"1\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("The Hobbit"))
                .andExpect(jsonPath("$.author").value("J.R.R. Tolkien"))
                .andExpect(jsonPath("$.isbn").value("978-0-395-19395-8"))
                .andExpect(jsonPath("$.locationId").value("1"))
                .andExpect(jsonPath("$.branchId").value("1"));
    }

    @Test
    public void testAddVideo() throws Exception {
        VideoDTO videoDTO = new VideoDTO();
        videoDTO.setTitle("The Lord of the Rings");
        videoDTO.setDirector("Peter Jackson");
        videoDTO.setGenre("Fantasy");
        videoDTO.setLocationId("2");
        videoDTO.setBranchId("2");

        mockMvc.perform(post("/items/videos")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"title\":\"The Lord of the Rings\",\"director\":\"Peter Jackson\",\"genre\":\"Fantasy\",\"locationId\":\"2\",\"branchId\":\"2\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("The Lord of the Rings"))
                .andExpect(jsonPath("$.director").value("Peter Jackson"))
                .andExpect(jsonPath("$.genre").value("Fantasy"))
                .andExpect(jsonPath("$.locationId").value("2"))
                .andExpect(jsonPath("$.branchId").value("2"));
    }

    @Test
    public void testGetItem() throws Exception {
        Book book = new Book();
        book.setTitle("1984");
        book.setAuthor("George Orwell");
        book.setIsbn("978-0-452-28423-4");
        book.setLocationId("1");
        book.setBranchId("1");
        Book savedBook = inventoryService.addItem(book);

        mockMvc.perform(get("/items/" + savedBook.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("1984"))
                .andExpect(jsonPath("$.author").value("George Orwell"))
                .andExpect(jsonPath("$.isbn").value("978-0-452-28423-4"));
    }

    @Test
    public void testUpdateItem() throws Exception {
        Book book = new Book();
        book.setTitle("1984");
        book.setAuthor("George Orwell");
        book.setIsbn("978-0-452-28423-4");
        book.setLocationId("1");
        book.setBranchId("1");
        Book savedBook = inventoryService.addItem(book);

        savedBook.setTitle("Nineteen Eighty-Four");
        inventoryService.updateItem(savedBook.getId(), savedBook);

        mockMvc.perform(put("/items/" + savedBook.getId())
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"title\":\"Nineteen Eighty-Four\",\"author\":\"George Orwell\",\"isbn\":\"978-0-452-28423-4\",\"locationId\":\"1\",\"branchId\":\"1\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value("Nineteen Eighty-Four"));
    }

    @Test
    public void testDeleteItem() throws Exception {
        Book book = new Book();
        book.setTitle("1984");
        book.setAuthor("George Orwell");
        book.setIsbn("978-0-452-28423-4");
        book.setLocationId("1");
        book.setBranchId("1");
        Book savedBook = inventoryService.addItem(book);

        mockMvc.perform(delete("/items/" + savedBook.getId()))
                .andExpect(status().isOk())
                .andExpect(content().string("Item deleted successfully"));
    }
}
```