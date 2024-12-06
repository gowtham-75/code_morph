```java
package com.yourcompany.librarymanagementsystem.model;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "books")
public class Book extends Item {

    private String author;
    private String isbn;

    public Book() {
        // Default constructor
    }

    // Getters and Setters
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
    
    // hashCode, equals, and toString methods can be overridden as needed
}
```