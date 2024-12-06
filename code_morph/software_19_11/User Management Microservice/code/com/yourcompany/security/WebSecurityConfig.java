```java
package com.yourcompany.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    public void configureGlobal(AuthenticationManagerBuilder auth) throws Exception {
        // Here you define the way of authentication. For example, in-memory authentication:
        auth.inMemoryAuthentication()
            .withUser("user").password(passwordEncoder().encode("password")).roles("USER")
            .and()
            .withUser("admin").password(passwordEncoder().encode("admin")).roles("ADMIN");
        
        // For JDBC authentication, you would set the data source and query for user and authorities.
        // For LDAP authentication, you would set the userDnPatterns or groupSearchBase, etc.
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            // CSRF is enabled by default, with Java Config
            .csrf().disable()
            .authorizeRequests()
                // Define which paths are secured and which are not. For example:
                .antMatchers("/public/**").permitAll()
                .antMatchers("/users/**").hasRole("USER")
                .antMatchers("/admin/**").hasRole("ADMIN")
                // Any other request must be authenticated
                .anyRequest().authenticated()
            .and()
            .formLogin()
                // Define the login page, login processing url, and default success url
                .loginPage("/login")
                .permitAll()
            .and()
            .logout()
                // Enable logout
                .permitAll()
            .and()
            .httpBasic(); // Enable basic authentication
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```