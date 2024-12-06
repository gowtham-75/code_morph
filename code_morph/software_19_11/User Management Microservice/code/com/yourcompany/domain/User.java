```java
package com.yourcompany.domain;

public class User {
    private String username;
    private String password;
    private boolean isActive;

    public User() {
    }

    public User(String username, String password, boolean isActive) {
        this.username = username;
        this.password = password;
        this.isActive = isActive;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public boolean isActive() {
        return isActive;
    }

    public void setActive(boolean active) {
        isActive = active;
    }

    // Additional methods such as equals, hashCode, and toString may be implemented as needed.
}
```