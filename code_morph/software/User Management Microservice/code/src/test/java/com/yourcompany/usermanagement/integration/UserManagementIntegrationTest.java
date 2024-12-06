```java
package com.yourcompany.usermanagement.integration;

import com.yourcompany.usermanagement.api.UserController;
import com.yourcompany.usermanagement.model.User;
import com.yourcompany.usermanagement.service.AuthenticationService;
import com.yourcompany.usermanagement.service.UserService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@ExtendWith(SpringExtension.class)
@SpringBootTest
public class UserManagementIntegrationTest {

    @Autowired
    private WebApplicationContext webApplicationContext;

    private MockMvc mockMvc;

    @Autowired
    private UserService userService;

    @Autowired
    private AuthenticationService authenticationService;

    @BeforeEach
    public void setup() {
        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
    }

    @Test
    public void testUserLogin() throws Exception {
        String username = "johndoe";
        String password = "secret";

        mockMvc.perform(post("/users/login")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\":\"" + username + "\", \"password\":\"" + password + "\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.token").exists())
                .andExpect(jsonPath("$.userId").exists())
                .andExpect(jsonPath("$.role").value("customer"));
    }

    @Test
    public void testGetUserById() throws Exception {
        User user = new User();
        user.setUsername("johndoe");
        user.setPassword("secret");
        user.setRole("customer");
        user.setStatus("active");
        user = userService.createUser(user);

        mockMvc.perform(get("/users/{userId}", user.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.userId").value(user.getId()))
                .andExpect(jsonPath("$.username").value("johndoe"))
                .andExpect(jsonPath("$.role").value("customer"))
                .andExpect(jsonPath("$.status").value("active"));
    }

    @Test
    public void testCreateUser() throws Exception {
        mockMvc.perform(post("/users")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\":\"janedoe\", \"password\":\"secret\", \"role\":\"customer\"}"))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.userId").exists())
                .andExpect(jsonPath("$.username").value("janedoe"))
                .andExpect(jsonPath("$.role").value("customer"));
    }

    @Test
    public void testUpdateUser() throws Exception {
        User user = new User();
        user.setUsername("johndoe");
        user.setPassword("secret");
        user.setRole("customer");
        user.setStatus("active");
        user = userService.createUser(user);

        mockMvc.perform(put("/users/{userId}", user.getId())
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"username\":\"johndoe\", \"password\":\"newsecret\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("User updated successfully."));
    }

    @Test
    public void testDeleteUser() throws Exception {
        User user = new User();
        user.setUsername("johndoe");
        user.setPassword("secret");
        user.setRole("customer");
        user.setStatus("active");
        user = userService.createUser(user);

        mockMvc.perform(delete("/users/{userId}", user.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.message").value("User deleted successfully."));
    }
}
```