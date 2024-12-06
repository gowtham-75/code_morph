```java
package com.yourcompany.service;

import com.yourcompany.domain.Customer;
import com.yourcompany.repository.CustomerRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import java.util.Optional;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.*;

class CustomerManagementServiceTest {

    @InjectMocks
    private CustomerManagementService customerManagementService;

    @Mock
    private CustomerRepository customerRepository;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    void createCustomer() {
        Customer customer = new Customer();
        customer.setId("C001");
        customer.setName("Jane Doe");
        customer.setEmail("jane.doe@example.com");

        when(customerRepository.save(customer)).thenReturn(customer);

        Customer createdCustomer = customerManagementService.createCustomer(customer);

        assertNotNull(createdCustomer);
        assertEquals("Jane Doe", createdCustomer.getName());
        assertEquals("jane.doe@example.com", createdCustomer.getEmail());
    }

    @Test
    void updateCustomer() {
        Customer existingCustomer = new Customer();
        existingCustomer.setId("C001");
        existingCustomer.setName("Jane Doe");
        existingCustomer.setEmail("jane.doe@example.com");

        Customer updatedCustomer = new Customer();
        updatedCustomer.setId("C001");
        updatedCustomer.setName("Jane Smith");
        updatedCustomer.setEmail("jane.smith@example.com");

        when(customerRepository.findByCustomerId("C001")).thenReturn(Optional.of(existingCustomer));
        when(customerRepository.save(updatedCustomer)).thenReturn(updatedCustomer);

        Customer result = customerManagementService.updateCustomer("C001", updatedCustomer);

        assertNotNull(result);
        assertEquals("C001", result.getId());
        assertEquals("Jane Smith", result.getName());
        assertEquals("jane.smith@example.com", result.getEmail());
    }

    @Test
    void deleteCustomer() {
        Customer customer = new Customer();
        customer.setId("C001");

        when(customerRepository.findByCustomerId(anyString())).thenReturn(Optional.of(customer));
        doNothing().when(customerRepository).delete(customer);

        assertDoesNotThrow(() -> customerManagementService.deleteCustomer("C001"));
        verify(customerRepository, times(1)).delete(customer);
    }

    @Test
    void getCustomer() {
        Customer customer = new Customer();
        customer.setId("C001");
        customer.setName("Jane Doe");
        customer.setEmail("jane.doe@example.com");

        when(customerRepository.findByCustomerId("C001")).thenReturn(Optional.of(customer));

        Customer foundCustomer = customerManagementService.getCustomer("C001");

        assertNotNull(foundCustomer);
        assertEquals("C001", foundCustomer.getId());
        assertEquals("Jane Doe", foundCustomer.getName());
        assertEquals("jane.doe@example.com", foundCustomer.getEmail());
    }
}
```