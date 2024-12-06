```java
package com.yourcompany.logging;

import org.springframework.http.HttpStatus;

public class ResponseLogDetails {
    private HttpStatus status;
    private String path;
    private long duration;

    public ResponseLogDetails(HttpStatus status, String path, long duration) {
        this.status = status;
        this.path = path;
        this.duration = duration;
    }

    public HttpStatus getStatus() {
        return status;
    }

    public void setStatus(HttpStatus status) {
        this.status = status;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public long getDuration() {
        return duration;
    }

    public void setDuration(long duration) {
        this.duration = duration;
    }

    @Override
    public String toString() {
        return "ResponseLogDetails{" +
                "status=" + status +
                ", path='" + path + '\'' +
                ", duration=" + duration +
                '}';
    }
}
```