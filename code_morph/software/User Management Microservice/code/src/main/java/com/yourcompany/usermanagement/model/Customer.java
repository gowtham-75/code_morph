```java
package com.yourcompany.usermanagement.model;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "customers")
public class Customer extends User {

    // Assuming CustomerDetails is a class that contains customer-specific attributes.
    // This attribute should be mapped to a column in the customers table or to another table depending on the schema.
    private CustomerDetails customerDetails;

    // Getters and setters for customerDetails
    public CustomerDetails getCustomerDetails() {
        return customerDetails;
    }

    public void setCustomerDetails(CustomerDetails customerDetails) {
        this.customerDetails = customerDetails;
    }

    // Additional methods and logic specific to the Customer class can be added here
}
```