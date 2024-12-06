```java
package com.library.inventory.api.dto;

import java.io.Serializable;

public class BookDTO implements Serializable {
    private String id;
    private String title;
    private String author;
    private String isbn;
    private String locationId;
    private String branchId;

    public BookDTO() {
    }

    public BookDTO(String id, String title, String author, String isbn, String locationId, String branchId) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.locationId = locationId;
        this.branchId = branchId;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public String getLocationId() {
        return locationId;
    }

    public void setLocationId(String locationId) {
        this.locationId = locationId;
    }

    public String getBranchId() {
        return branchId;
    }

    public void setBranchId(String branchId) {
        this.branchId = branchId;
    }
}
```