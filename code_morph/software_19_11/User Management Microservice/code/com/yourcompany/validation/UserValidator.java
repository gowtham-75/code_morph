```java
package com.yourcompany.validation;

import com.yourcompany.domain.UserLoginDTO;
import org.springframework.util.StringUtils;
import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

public class UserValidator implements Validator {

    @Override
    public boolean supports(Class<?> clazz) {
        return UserLoginDTO.class.isAssignableFrom(clazz);
    }

    @Override
    public void validate(Object target, Errors errors) {
        UserLoginDTO userLoginDTO = (UserLoginDTO) target;
        
        if (!StringUtils.hasText(userLoginDTO.getUsername())) {
            errors.rejectValue("username", "username.empty", "Username must not be empty");
        }

        if (!StringUtils.hasText(userLoginDTO.getPassword())) {
            errors.rejectValue("password", "password.empty", "Password must not be empty");
        }

        // Additional validation logic can be added here
    }
}
```