```java
package com.yourcompany.ordermanagement.service;

import com.yourcompany.ordermanagement.model.Order;
import com.yourcompany.ordermanagement.repository.OrderRepository;
import com.yourcompany.ordermanagement.exception.OrderNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Service
public class OrderService {

    private final OrderRepository orderRepository;

    @Autowired
    public OrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    @Transactional
    public Order createOrder(Order order) {
        // Perform order validation and business logic here
        // For example, check for stock availability, customer credit limit, etc.
        // Assume validation is passed and business logic is handled
        
        return orderRepository.save(order);
    }

    @Transactional
    public Order modifyOrder(Long orderId, Order orderDetails) {
        Order existingOrder = orderRepository.findById(orderId)
                .orElseThrow(() -> new OrderNotFoundException("Order not found with id: " + orderId));
        
        // Update the existing order with new details
        // For simplicity, let's assume we are updating the entire order
        // In a real scenario, you would update only the changed fields and handle related business logic
        existingOrder.setItems(orderDetails.getItems());
        existingOrder.setCustomer(orderDetails.getCustomer());
        existingOrder.setTotalAmount(orderDetails.getTotalAmount());
        
        return orderRepository.save(existingOrder);
    }

    public Order getOrderById(Long orderId) {
        Optional<Order> order = orderRepository.findById(orderId);
        return order.orElseThrow(() -> new OrderNotFoundException("Order not found with id: " + orderId));
    }
}
```