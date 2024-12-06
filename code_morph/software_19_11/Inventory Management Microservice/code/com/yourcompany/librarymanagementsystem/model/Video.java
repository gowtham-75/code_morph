```java
package com.yourcompany.librarymanagementsystem.model;

public class Video extends Item {
    private String director;
    private String genre;

    public Video() {
    }

    public Video(String id, String title, Location location, Branch branch, String director, String genre) {
        super(id, title, location, branch);
        this.director = director;
        this.genre = genre;
    }

    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }
}
```