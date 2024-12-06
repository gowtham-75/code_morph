```java
package com.yourcompany.usermanagement.service;

import com.yourcompany.usermanagement.model.User;
import com.yourcompany.usermanagement.repository.UserRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

import java.util.Optional;

@ExtendWith(MockitoExtension.class)
public class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    private User user;

    @BeforeEach
    public void setUp() {
        user = new User();
        user.setId("1");
        user.setUsername("johndoe");
        user.setPassword("secret");
        user.setStatus("active");
        user.setRole("customer");
    }

    @Test
    public void testCreateUser() {
        when(userRepository.save(any(User.class))).thenReturn(user);
        User createdUser = userService.createUser(user);
        assertNotNull(createdUser);
        assertEquals(user.getId(), createdUser.getId());
    }

    @Test
    public void testUpdateUser() {
        when(userRepository.findById(anyString())).thenReturn(Optional.of(user));
        when(userRepository.save(any(User.class))).thenReturn(user);
        User updatedUser = userService.updateUser(user.getId(), user);
        assertNotNull(updatedUser);
        assertEquals(user.getUsername(), updatedUser.getUsername());
    }

    @Test
    public void testGetUserById() {
        when(userRepository.findById(anyString())).thenReturn(Optional.of(user));
        User foundUser = userService.getUserById(user.getId());
        assertNotNull(foundUser);
        assertEquals(user.getId(), foundUser.getId());
    }

    @Test
    public void testDeleteUser() {
        doNothing().when(userRepository).delete(any(User.class));
        userService.deleteUser(user.getId());
        verify(userRepository, times(1)).delete(any(User.class));
    }
}
```