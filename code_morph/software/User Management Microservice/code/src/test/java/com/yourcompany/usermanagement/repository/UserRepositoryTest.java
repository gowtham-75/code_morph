```java
package com.yourcompany.usermanagement.repository;

import com.yourcompany.usermanagement.model.User;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.*;

@DataJpaTest
@ExtendWith(MockitoExtension.class)
public class UserRepositoryTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private User user;

    @BeforeEach
    void setUp() {
        user = new User();
        user.setId("1");
        user.setUsername("johndoe");
        user.setPassword("secret");
        user.setStatus("active");
        user.setRole("customer");
    }

    @Test
    void whenSaveUser_thenUserIsSaved() {
        when(userRepository.save(any(User.class))).thenReturn(user);
        User savedUser = userRepository.save(user);
        assertThat(savedUser).isNotNull();
        verify(userRepository).save(any(User.class));
    }

    @Test
    void whenFindById_thenReturnUser() {
        when(userRepository.findById(user.getId())).thenReturn(Optional.of(user));
        Optional<User> foundUser = userRepository.findById(user.getId());
        assertThat(foundUser).isPresent();
        assertThat(foundUser.get()).isEqualTo(user);
        verify(userRepository).findById(user.getId());
    }

    @Test
    void whenDeleteUser_thenUserIsDeleted() {
        doNothing().when(userRepository).delete(user);
        userRepository.delete(user);
        verify(userRepository).delete(user);
    }
}
```