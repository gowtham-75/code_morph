```java
package com.yourcompany.usermanagement.service;

import com.yourcompany.usermanagement.model.User;
import com.yourcompany.usermanagement.repository.UserRepository;
import com.yourcompany.usermanagement.exception.CustomException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.security.crypto.password.PasswordEncoder;
import java.util.Optional;
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

public class AuthenticationServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @InjectMocks
    private AuthenticationService authenticationService;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void authenticateSuccessTest() {
        String username = "johndoe";
        String password = "secret";
        User mockUser = new User();
        mockUser.setUsername(username);
        mockUser.setPassword(passwordEncoder.encode(password));

        when(userRepository.findByUsername(username)).thenReturn(Optional.of(mockUser));
        when(passwordEncoder.matches(anyString(), anyString())).thenReturn(true);

        String token = authenticationService.authenticate(username, password);

        assertNotNull(token);
        verify(userRepository, times(1)).findByUsername(username);
    }

    @Test
    public void authenticateFailureTest() {
        String username = "janedoe";
        String password = "wrongpassword";

        when(userRepository.findByUsername(username)).thenReturn(Optional.empty());

        assertThrows(CustomException.class, () -> {
            authenticationService.authenticate(username, password);
        });

        verify(userRepository, times(1)).findByUsername(username);
    }
}
```