# Common HTTP Status Codes

HTTP status codes are grouped into 5 categories:

| Range | Category |
|---------|----------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirection |
| 4xx | Client Errors |
| 5xx | Server Errors |

---

## 1xx Informational

| Code | Name | Meaning |
|------|------|----------|
| 100 | Continue | Request received, continue sending data |
| 101 | Switching Protocols | Server is changing protocols |

---

## 2xx Success

| Code | Name | Meaning |
|------|------|----------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 202 | Accepted | Request accepted for processing |
| 204 | No Content | Request successful, no response body |

### Example
```http
HTTP/1.1 200 OK
```

---

## 3xx Redirection

| Code | Name | Meaning |
|------|------|----------|
| 301 | Moved Permanently | Resource moved permanently |
| 302 | Found | Temporary redirect |
| 304 | Not Modified | Cached version can be used |
| 307 | Temporary Redirect | Redirect while preserving method |

### Example
```http
HTTP/1.1 301 Moved Permanently
Location: /new-page
```

---

## 4xx Client Errors

| Code | Name | Meaning |
|------|------|----------|
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource not found |
| 405 | Method Not Allowed | HTTP method not supported |
| 408 | Request Timeout | Client took too long |
| 409 | Conflict | Resource conflict |
| 422 | Unprocessable Entity | Validation error (common in FastAPI) |
| 429 | Too Many Requests | Rate limit exceeded |

### Example
```http
HTTP/1.1 404 Not Found
```

---

## 5xx Server Errors

| Code | Name | Meaning |
|------|------|----------|
| 500 | Internal Server Error | Generic server error |
| 501 | Not Implemented | Functionality not supported |
| 502 | Bad Gateway | Invalid response from upstream server |
| 503 | Service Unavailable | Server temporarily unavailable |
| 504 | Gateway Timeout | Upstream server timed out |

### Example
```http
HTTP/1.1 500 Internal Server Error
```

---

# Most Important Codes for FastAPI Developers

| Code | When Used |
|------|-----------|
| 200 | Successful GET request |
| 201 | Resource created |
| 204 | Resource deleted successfully |
| 400 | Invalid request |
| 401 | User not authenticated |
| 403 | User authenticated but lacks permission |
| 404 | Resource not found |
| 422 | Pydantic validation failed |
| 500 | Server-side error |

---