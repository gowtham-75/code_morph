```java
package com.yourcompany.controller;

import com.yourcompany.domain.UserDTO;
import com.yourcompany.service.AuthenticationService;
import com.yourcompany.service.CustomerManagementService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.http.ResponseEntity;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.validation.BindingResult;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@ExtendWith(SpringExtension.class)
public class UserControllerTest {

    @Mock
    private AuthenticationService authenticationService;

    @Mock
    private CustomerManagementService customerManagementService;

    @Mock
    private BindingResult bindingResult;

    @InjectMocks
    private UserController userController;

    private UserDTO userDTO;

    @BeforeEach
    public void setUp() {
        userDTO = new UserDTO();
        userDTO.setUserId("U001");
        userDTO.setName("John Doe");
        userDTO.setEmail("john.doe@example.com");
    }

    @Test
    public void testLogin() {
        // Given
        String username = "john.doe";
        String password = "password123";
        // When
        when(authenticationService.authenticateUser(username, password)).thenReturn(userDTO);
        ResponseEntity<?> response = userController.login(username, password);
        // Then
        assertEquals(200, response.getStatusCodeValue());
        verify(authenticationService, times(1)).authenticateUser(username, password);
    }

    @Test
    public void testGetUser() {
        // Given
        String userId = "U001";
        // When
        when(customerManagementService.getCustomer(userId)).thenReturn(userDTO);
        ResponseEntity<UserDTO> response = userController.getUser(userId);
        // Then
        assertEquals(200, response.getStatusCodeValue());
        assertEquals(userDTO, response.getBody());
        verify(customerManagementService, times(1)).getCustomer(userId);
    }

    @Test
    public void testCreateUser() {
        // Given
        // When
        when(customerManagementService.createCustomer(any())).thenReturn(userDTO);
        ResponseEntity<UserDTO> response = userController.createUser(userDTO);
        // Then
        assertEquals(201, response.getStatusCodeValue());
        assertEquals(userDTO, response.getBody());
        verify(customerManagementService, times(1)).createCustomer(any());
    }

    @Test
    public void testUpdateUser() {
        // Given
        String userId = "U001";
        // When
        when(customerManagementService.updateCustomer(eq(userId), any())).thenReturn(userDTO);
        ResponseEntity<UserDTO> response = userController.updateUser(userId, userDTO);
        // Then
        assertEquals(200, response.getStatusCodeValue());
        assertEquals(userDTO, response.getBody());
        verify(customerManagementService, times(1)).updateCustomer(eq(userId), any());
    }

    @Test
    public void testDeleteUser() {
        // Given
        String userId = "U001";
        // When
        doNothing().when(customerManagementService).deleteCustomer(userId);
        ResponseEntity<Void> response = userController.deleteUser(userId);
        // Then
        assertEquals(204, response.getStatusCodeValue());
        verify(customerManagementService, times(1)).deleteCustomer(userId);
    }
}
```