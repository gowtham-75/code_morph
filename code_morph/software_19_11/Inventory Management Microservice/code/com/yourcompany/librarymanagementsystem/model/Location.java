```java
package com.yourcompany.librarymanagementsystem.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "locations")
public class Location {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String shelf;
    private String aisle;

    public Location() {
    }

    public Location(String shelf, String aisle) {
        this.shelf = shelf;
        this.aisle = aisle;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getShelf() {
        return shelf;
    }

    public void setShelf(String shelf) {
        this.shelf = shelf;
    }

    public String getAisle() {
        return aisle;
    }

    public void setAisle(String aisle) {
        this.aisle = aisle;
    }

    @Override
    public String toString() {
        return "Location{" +
                "id=" + id +
                ", shelf='" + shelf + '\'' +
                ", aisle='" + aisle + '\'' +
                '}';
    }
}
```