```java
package com.yourcompany.librarymanagementsystem.service;

import com.yourcompany.librarymanagementsystem.model.Book;
import com.yourcompany.librarymanagementsystem.model.Item;
import com.yourcompany.librarymanagementsystem.model.Video;
import com.yourcompany.librarymanagementsystem.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ItemService {

    private final ItemRepository itemRepository;

    @Autowired
    public ItemService(ItemRepository itemRepository) {
        this.itemRepository = itemRepository;
    }

    public List<Item> listItems() {
        return itemRepository.findAll();
    }

    public Item createItem(Item item) {
        return itemRepository.save(item);
    }

    public Item modifyItem(String itemId, Item item) {
        return itemRepository.findById(itemId).map(existingItem -> {
            existingItem.setTitle(item.getTitle());
            existingItem.setLocation(item.getLocation());
            existingItem.setBranch(item.getBranch());
            if (item instanceof Book) {
                Book existingBook = (Book) existingItem;
                Book newBook = (Book) item;
                existingBook.setAuthor(newBook.getAuthor());
                existingBook.setIsbn(newBook.getIsbn());
                return itemRepository.save(existingBook);
            } else if (item instanceof Video) {
                Video existingVideo = (Video) existingItem;
                Video newVideo = (Video) item;
                existingVideo.setDirector(newVideo.getDirector());
                existingVideo.setGenre(newVideo.getGenre());
                return itemRepository.save(existingVideo);
            }
            return null;
        }).orElseGet(() -> {
            item.setId(itemId);
            return itemRepository.save(item);
        });
    }

    public void removeItem(String itemId) {
        itemRepository.deleteById(itemId);
    }

    public Optional<Item> fetchItemById(String itemId) {
        return itemRepository.findById(itemId);
    }
}
```