```java
package com.yourcompany.ordermanagement.api;

import com.yourcompany.ordermanagement.dto.OrderDTO;
import com.yourcompany.ordermanagement.service.OrderService;
import com.yourcompany.ordermanagement.exception.OrderNotFoundException;
import com.yourcompany.ordermanagement.model.Order;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/orders")
public class OrderController {

    private final OrderService orderService;

    @Autowired
    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping
    public ResponseEntity<OrderDTO> createOrder(@RequestBody Order order) {
        OrderDTO createdOrder = orderService.createOrder(order);
        return ResponseEntity.status(201).body(createdOrder);
    }

    @GetMapping("/{id}")
    public ResponseEntity<OrderDTO> getOrderById(@PathVariable Long id) {
        OrderDTO orderDTO = orderService.getOrderById(id)
                .orElseThrow(() -> new OrderNotFoundException("Order not found with id: " + id));
        return ResponseEntity.ok(orderDTO);
    }

    @PutMapping("/{id}/modify")
    public ResponseEntity<OrderDTO> modifyOrder(@PathVariable Long id, @RequestBody Order order) {
        OrderDTO updatedOrder = orderService.modifyOrder(id, order);
        return ResponseEntity.ok(updatedOrder);
    }
}
```