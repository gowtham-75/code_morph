```java
package com.yourcompany.logging;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ApplicationLogger {

    private static final Logger logger = LoggerFactory.getLogger(ApplicationLogger.class);

    public void logRequest(RequestLogDetails details) {
        logger.info("Request: method={}, uri={}, headers={}, body={}",
                details.getMethod(), details.getUri(), details.getHeaders(), details.getBody());
    }

    public void logResponse(ResponseLogDetails details) {
        logger.info("Response: status={}, headers={}, body={}",
                details.getStatus(), details.getHeaders(), details.getBody());
    }
}
```