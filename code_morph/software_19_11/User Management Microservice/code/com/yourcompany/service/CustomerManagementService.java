```java
package com.yourcompany.service;

import com.yourcompany.domain.Customer;
import com.yourcompany.repository.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class CustomerManagementService {

    private final CustomerRepository customerRepository;

    @Autowired
    public CustomerManagementService(CustomerRepository customerRepository) {
        this.customerRepository = customerRepository;
    }

    public Customer createCustomer(Customer customer) {
        // Validate customer data
        // Logic to create a customer
        return customerRepository.save(customer);
    }

    public Customer updateCustomer(String customerId, Customer customer) {
        // Check if customer exists
        Optional<Customer> existingCustomer = customerRepository.findByCustomerId(customerId);
        if (!existingCustomer.isPresent()) {
            // Handle the case where the customer doesn't exist, e.g., throw an exception
        }
        // Update customer data
        return customerRepository.save(customer);
    }

    public void deleteCustomer(String customerId) {
        // Check if customer exists
        Optional<Customer> existingCustomer = customerRepository.findByCustomerId(customerId);
        if (!existingCustomer.isPresent()) {
            // Handle the case where the customer doesn't exist, e.g., throw an exception
        }
        // Delete the customer
        customerRepository.delete(existingCustomer.get());
    }

    public Customer getCustomer(String customerId) {
        // Retrieve customer by customerId
        Optional<Customer> customer = customerRepository.findByCustomerId(customerId);
        if (!customer.isPresent()) {
            // Handle the case where the customer doesn't exist, e.g., throw an exception
        }
        return customer.get();
    }
}
```