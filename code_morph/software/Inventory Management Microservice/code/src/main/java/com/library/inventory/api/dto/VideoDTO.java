```java
package com.library.inventory.api.dto;

import java.io.Serializable;

public class VideoDTO implements Serializable {
    private String id;
    private String title;
    private String director;
    private String genre;
    private String locationId;
    private String branchId;

    public VideoDTO() {
    }

    public VideoDTO(String id, String title, String director, String genre, String locationId, String branchId) {
        this.id = id;
        this.title = title;
        this.director = director;
        this.genre = genre;
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