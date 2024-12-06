```java
package com.yourcompany.service;

import com.yourcompany.domain.User;
import com.yourcompany.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

public class AuthenticationServiceTest {

    @InjectMocks
    private AuthenticationService authenticationService;

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void authenticateUser_ValidCredentials_ReturnsUser() {
        String username = "testUser";
        String password = "testPass";
        String encodedPassword = "encodedTestPass";

        User user = new User();
        user.setUsername(username);
        user.setPassword(encodedPassword);
        user.setActive(true);

        when(userRepository.findByUsername(username)).thenReturn(Optional.of(user));
        when(passwordEncoder.matches(password, encodedPassword)).thenReturn(true);

        User authenticatedUser = authenticationService.authenticateUser(username, password);

        assertNotNull(authenticatedUser);
        assertEquals(username, authenticatedUser.getUsername());
    }

    @Test
    public void authenticateUser_InvalidUsername_ThrowsException() {
        String username = "nonExistentUser";
        String password = "testPass";

        when(userRepository.findByUsername(username)).thenReturn(Optional.empty());

        Exception exception = assertThrows(RuntimeException.class, () ->
                authenticationService.authenticateUser(username, password));

        assertTrue(exception.getMessage().contains("User not found"));
    }

    @Test
    public void authenticateUser_InvalidPassword_ThrowsException() {
        String username = "testUser";
        String password = "wrongPass";
        String encodedPassword = "encodedTestPass";

        User user = new User();
        user.setUsername(username);
        user.setPassword(encodedPassword);
        user.setActive(true);

        when(userRepository.findByUsername(username)).thenReturn(Optional.of(user));
        when(passwordEncoder.matches(password, encodedPassword)).thenReturn(false);

        Exception exception = assertThrows(RuntimeException.class, () ->
                authenticationService.authenticateUser(username, password));

        assertTrue(exception.getMessage().contains("Invalid password"));
    }
}
```