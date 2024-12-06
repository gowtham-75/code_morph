```java
package com.yourcompany.usermanagement.api;

import com.yourcompany.usermanagement.model.User;
import com.yourcompany.usermanagement.service.UserService;
import com.yourcompany.usermanagement.service.AuthenticationService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.mockito.BDDMockito.given;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@ExtendWith(MockitoExtension.class)
public class UserControllerTest {

    @Mock
    private UserService userService;

    @Mock
    private AuthenticationService authenticationService;

    @InjectMocks
    private UserController userController;

    private MockMvc mockMvc;

    @BeforeEach
    void setUp() {
        mockMvc = MockMvcBuilders.standaloneSetup(userController).build();
    }

    @Test
    void whenPostLogin_thenAuthenticateUser() throws Exception {
        String username = "johndoe";
        String password = "secret";
        String token = "jwt-token";

        given(authenticationService.authenticate(username, password)).willReturn(token);

        mockMvc.perform(post("/users/login")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\":\"" + username + "\", \"password\":\"" + password + "\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.token").value(token));
    }

    @Test
    void whenGetUser_thenReturnsUser() throws Exception {
        String userId = "1";
        User user = new User();
        user.setId(userId);
        user.setUsername("johndoe");
        user.setRole("customer");

        given(userService.getUserById(userId)).willReturn(user);

        mockMvc.perform(get("/users/{userId}", userId))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.userId").value(userId))
                .andExpect(jsonPath("$.username").value("johndoe"))
                .andExpect(jsonPath("$.role").value("customer"));
    }

    @Test
    void whenUpdateUser_thenUserUpdated() throws Exception {
        String userId = "1";
        User user = new User();
        user.setId(userId);
        user.setUsername("johndoe");
        user.setPassword("newsecret");

        given(userService.updateUser(userId, user)).willReturn(user);

        mockMvc.perform(put("/users/{userId}", userId)
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\":\"" + user.getUsername() + "\", \"password\":\"" + user.getPassword() + "\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("User updated successfully."));
    }

    @Test
    void whenCreateUser_thenUserCreated() throws Exception {
        User user = new User();
        user.setUsername("janedoe");
        user.setPassword("secret");
        user.setRole("customer");

        given(userService.createUser(user)).willReturn(user);

        mockMvc.perform(post("/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\":\"" + user.getUsername() + "\", \"password\":\"" + user.getPassword() + "\", \"role\":\"" + user.getRole() + "\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.username").value("janedoe"))
                .andExpect(jsonPath("$.role").value("customer"));
    }

    @Test
    void whenDeleteUser_thenUserDeleted() throws Exception {
        String userId = "1";

        mockMvc.perform(delete("/users/{userId}", userId))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("User deleted successfully."));
    }
}
```