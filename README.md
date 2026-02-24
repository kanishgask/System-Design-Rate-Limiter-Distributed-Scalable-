# 🚦 Distributed Rate Limiter System Design

> Day 2 – High-Package Software Engineer Journey 🚀

---

## 📌 Problem Statement

Design a scalable Rate Limiter system that restricts the number of API requests a user can make within a specified time window.

Example:
- A user can make only 5 requests per minute.
- If exceeded → return HTTP 429 (Too Many Requests).

---

## 🎯 Functional Requirements

- Limit requests per user
- Support configurable limits
- Fast response time (<10ms overhead)
- Distributed system support
- Accurate request tracking

---

## ⚙️ Non-Functional Requirements

- Horizontally scalable
- Low latency
- High availability
- Fault tolerant
- Prevent abuse / DDOS

---

# 🧠 Rate Limiting Algorithms

## 1️⃣ Fixed Window
Simple counter per time window

## 2️⃣ Sliding Window (Better accuracy)

## 3️⃣ Token Bucket (Best for real systems)

✔ Selected: Token Bucket Algorithm

Why?
- Smooth traffic control
- Allows burst traffic
- Industry standard approach

---

# 🏗️ High-Level Architecture

Client  
   ↓  
API Gateway  
   ↓  
Rate Limiter (Redis)  
   ↓  
Application Server  

Redis used for distributed atomic counters.

---

# 🗄️ Database / Storage Choice

In-memory datastore (Redis) for:

- Fast increments
- Atomic operations
- Expiry support

---

# 📊 Capacity Estimation

Assume:
- 1M users
- 10 requests/min per user

Requests per minute:
= 10M operations

Redis easily handles 100k+ ops/sec.

---

# 🔐 Security Considerations

- Use IP + User ID combination
- Protection against replay attacks
- Rate limit login endpoint more strictly
- DDOS mitigation at load balancer

---

# ⚡ Scaling Strategy

- Redis Cluster
- Consistent hashing
- Multiple API servers
- CDN for static content

---

# 🧩 Trade-offs

| Algorithm | Pros | Cons |
|-----------|------|------|
| Fixed Window | Simple | Burst edge problem |
| Sliding Window | Accurate | Slightly complex |
| Token Bucket | Smooth traffic | Requires token refill logic |

---

# 🚀 Future Improvements

- Per API key limits
- Dynamic rate limits
- Machine-learning based anomaly detection
- Rate limit dashboard

---

# 🎯 Concepts Demonstrated

- Distributed systems
- Caching systems
- Traffic shaping
- Horizontal scaling
- Backend optimization

---

⭐ Part of 30-Day High Impact GitHub Engineering Series
