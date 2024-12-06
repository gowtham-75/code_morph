```java
package com.yourcompany.librarymanagementsystem.controller;

import com.yourcompany.librarymanagementsystem.model.Book;
import com.yourcompany.librarymanagementsystem.model.Video;
import com.yourcompany.librarymanagementsystem.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/items")
public class ItemController {

    private final ItemService itemService;

    @Autowired
    public ItemController(ItemService itemService) {
        this.itemService = itemService;
    }

    @GetMapping
    public ResponseEntity<List<?>> getAllItems() {
        List<?> items = itemService.listItems();
        return ResponseEntity.ok(items);
    }

    @PostMapping("/books")
    public ResponseEntity<Book> addItem(@RequestBody Book book) {
        Book createdBook = itemService.createItem(book);
        return ResponseEntity.ok(createdBook);
    }

    @PostMapping("/videos")
    public ResponseEntity<Video> addItem(@RequestBody Video video) {
        Video createdVideo = itemService.createItem(video);
        return ResponseEntity.ok(createdVideo);
    }

    @PutMapping("/{itemId}")
    public ResponseEntity<?> updateItem(@PathVariable String itemId, @RequestBody Object item) {
        Object updatedItem = itemService.modifyItem(itemId, item);
        return ResponseEntity.ok(updatedItem);
    }

    @DeleteMapping("/{itemId}")
    public ResponseEntity<?> deleteItem(@PathVariable String itemId) {
        itemService.removeItem(itemId);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/{itemId}")
    public ResponseEntity<?> getItemById(@PathVariable String itemId) {
        Object item = itemService.fetchItemById(itemId);
        return ResponseEntity.ok(item);
    }
}
```