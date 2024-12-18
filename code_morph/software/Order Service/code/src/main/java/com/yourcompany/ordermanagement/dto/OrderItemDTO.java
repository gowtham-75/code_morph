```java
package com.yourcompany.ordermanagement.dto;

import java.math.BigDecimal;

public class OrderItemDTO {

    private Long productId;
    private int quantity;
    private BigDecimal price;

    public OrderItemDTO() {
    }

    public OrderItemDTO(Long productId, int quantity, BigDecimal price) {
        this.productId = productId;
        this.quantity = quantity;
        this.price = price;
    }

    public Long getProductId() {
        return productId;
    }

    public void setProductId(Long productId) {
        this.productId = productId;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }
}
```