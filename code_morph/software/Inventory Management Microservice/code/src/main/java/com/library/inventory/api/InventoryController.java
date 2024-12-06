```java
package com.library.inventory.api;

import com.library.inventory.api.dto.BookDTO;
import com.library.inventory.api.dto.VideoDTO;
import com.library.inventory.service.InventoryService;
import com.library.inventory.model.Book;
import com.library.inventory.model.Video;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/items")
public class InventoryController {

    private final InventoryService inventoryService;

    @Autowired
    public InventoryController(InventoryService inventoryService) {
        this.inventoryService = inventoryService;
    }

    @GetMapping
    public ResponseEntity<List<Object>> getAllItems() {
        List<Object> items = inventoryService.getAllItems();
        return ResponseEntity.ok(items);
    }

    @PostMapping("/books")
    public ResponseEntity<BookDTO> addBook(@RequestBody BookDTO bookDTO) {
        Book book = inventoryService.addItem(bookDTO.toEntity());
        return ResponseEntity.ok(new BookDTO(book));
    }

    @PostMapping("/videos")
    public ResponseEntity<VideoDTO> addVideo(@RequestBody VideoDTO videoDTO) {
        Video video = inventoryService.addItem(videoDTO.toEntity());
        return ResponseEntity.ok(new VideoDTO(video));
    }

    @PutMapping("/{itemId}")
    public ResponseEntity<Object> updateItem(@PathVariable String itemId, @RequestBody Object itemDTO) {
        Object updatedItem = inventoryService.updateItem(itemId, itemDTO);
        return ResponseEntity.ok(updatedItem);
    }

    @DeleteMapping("/{itemId}")
    public ResponseEntity<Void> removeItem(@PathVariable String itemId) {
        inventoryService.removeItem(itemId);
        return ResponseEntity.ok().build();
    }
}
```