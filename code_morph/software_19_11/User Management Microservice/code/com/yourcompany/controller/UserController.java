```java
package com.yourcompany.controller;

import com.yourcompany.domain.UserDTO;
import com.yourcompany.service.AuthenticationService;
import com.yourcompany.service.CustomerManagementService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/users")
public class UserController {

    private final AuthenticationService authenticationService;
    private final CustomerManagementService customerManagementService;

    @Autowired
    public UserController(AuthenticationService authenticationService, CustomerManagementService customerManagementService) {
        this.authenticationService = authenticationService;
        this.customerManagementService = customerManagementService;
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody UserDTO userLoginDTO) {
        // Logic to authenticate the user and create a token
        // This is a placeholder for the actual authentication logic
        return ResponseEntity.ok().body("Token generated for user");
    }

    @GetMapping("/{userId}")
    public ResponseEntity<UserDTO> getUser(@PathVariable String userId) {
        // Logic to get a user by id
        // This is a placeholder for the actual get user logic
        return ResponseEntity.ok(new UserDTO());
    }

    @PostMapping
    public ResponseEntity<UserDTO> createUser(@RequestBody UserDTO userDTO) {
        // Logic to create a new user
        // This is a placeholder for the actual create user logic
        return ResponseEntity.ok(new UserDTO());
    }

    @PutMapping("/{userId}")
    public ResponseEntity<UserDTO> updateUser(@PathVariable String userId, @RequestBody UserDTO userDTO) {
        // Logic to update an existing user
        // This is a placeholder for the actual update user logic
        return ResponseEntity.ok(new UserDTO());
    }

    @DeleteMapping("/{userId}")
    public ResponseEntity<Void> deleteUser(@PathVariable String userId) {
        // Logic to delete a user by id
        // This is a placeholder for the actual delete user logic
        return ResponseEntity.ok().build();
    }
}
```