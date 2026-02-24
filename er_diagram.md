# 📊 ER Diagram - Rate Limiter System

## 🧱 Entities

### USERS
- user_id (Primary Key)
- api_key
- created_at

### RATE_LIMIT_RULES
- rule_id (Primary Key)
- max_requests
- window_size
- endpoint_name

### REQUEST_LOGS
- log_id (Primary Key)
- user_id (Foreign Key)
- timestamp
- endpoint

---

# 🔗 Relationships

One USER → Many REQUEST_LOGS  
One RATE_LIMIT_RULE → Applied to Many USERS  

---

# 📐 ER Diagram (ASCII)

```
+------------------+       1      N      +------------------+
|      USERS       |---------------------|  REQUEST_LOGS    |
+------------------+                      +------------------+
| user_id (PK)     |                      | log_id (PK)     |
| api_key          |                      | user_id (FK)    |
| created_at       |                      | timestamp       |
+------------------+                      | endpoint        |
                                          +------------------+

+----------------------+
| RATE_LIMIT_RULES     |
+----------------------+
| rule_id (PK)         |
| max_requests         |
| window_size          |
| endpoint_name        |
+----------------------+
```
