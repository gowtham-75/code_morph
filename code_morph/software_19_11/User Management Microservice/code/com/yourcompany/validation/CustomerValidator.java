```java
package com.yourcompany.validation;

import com.yourcompany.domain.Customer;
import com.yourcompany.exception.ValidationException;

public class CustomerValidator {

    public void validateCustomerData(Customer customer) throws ValidationException {
        if (customer == null) {
            throw new ValidationException("Customer object cannot be null");
        }

        if (customer.getId() == null || customer.getId().trim().isEmpty()) {
            throw new ValidationException("Customer ID cannot be empty");
        }

        if (customer.getName() == null || customer.getName().trim().isEmpty()) {
            throw new ValidationException("Customer name cannot be empty");
        }

        if (customer.getEmail() == null || !customer.getEmail().contains("@")) {
            throw new ValidationException("Customer email is invalid");
        }

        // You can add more validation logic as needed
    }
}
```