```java
package com.yourcompany.usermanagement.service;

import com.yourcompany.usermanagement.model.User;
import com.yourcompany.usermanagement.repository.UserRepository;
import com.yourcompany.usermanagement.exception.CustomException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import java.util.Date;

@Service
public class AuthenticationService {

    private static final long EXPIRATION_TIME = 864_000_00; // 1 day in milliseconds
    private static final String SECRET_KEY = "SecretKeyToGenJWTs";
    
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Autowired
    public AuthenticationService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public String authenticate(String username, String password) {
        User user = userRepository.findByUsername(username)
            .orElseThrow(() -> new CustomException("User not found", 404));
        
        if (!passwordEncoder.matches(password, user.getPassword())) {
            throw new CustomException("Invalid password", 401);
        }
        
        return Jwts.builder()
                .setSubject(username)
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRATION_TIME))
                .signWith(SignatureAlgorithm.HS512, SECRET_KEY)
                .compact();
    }
}
```