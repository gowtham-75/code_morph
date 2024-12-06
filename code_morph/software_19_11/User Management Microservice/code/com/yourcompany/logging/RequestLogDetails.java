```java
package com.yourcompany.logging;

import java.util.Map;

public class RequestLogDetails {
    private String method;
    private String url;
    private Map<String, String> headers;
    private String body;

    public RequestLogDetails(String method, String url, Map<String, String> headers, String body) {
        this.method = method;
        this.url = url;
        this.headers = headers;
        this.body = body;
    }

    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public Map<String, String> getHeaders() {
        return headers;
    }

    public void setHeaders(Map<String, String> headers) {
        this.headers = headers;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    @Override
    public String toString() {
        return "RequestLogDetails{" +
               "method='" + method + '\'' +
               ", url='" + url + '\'' +
               ", headers=" + headers +
               ", body='" + body + '\'' +
               '}';
    }
}
```