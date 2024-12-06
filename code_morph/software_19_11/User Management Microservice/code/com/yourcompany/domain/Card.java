```java
package com.yourcompany.domain;

public class Card {
    private String cardId;
    private boolean active;
    private double fines;

    public Card(String cardId, boolean active, double fines) {
        this.cardId = cardId;
        this.active = active;
        this.fines = fines;
    }

    public String getCardId() {
        return cardId;
    }

    public void setCardId(String cardId) {
        this.cardId = cardId;
    }

    public boolean isActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public double getFines() {
        return fines;
    }

    public void setFines(double fines) {
        this.fines = fines;
    }
}
```