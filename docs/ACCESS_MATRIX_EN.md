# API Access Matrix - Restful Booker Platform

## 📋 Authentication and Access Overview

**Authentication Mechanism**: Token passed in HTTP Cookie named `token`  
**Obtaining a Token**: `POST /auth/login` with body `{"username": "admin", "password": "password"}`

---

## 📊 Access Matrix by Service

### 1. 🔑 Authentication Service (Auth Service:3004)

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| POST | `/auth/login` | ❌ Not required | Obtain authentication token |
| POST | `/auth/validate` | ✅ Required | Validate token (cookie: `token`) |
| POST | `/auth/logout` | ✅ Required | Clear token (cookie: `token`) |

### 2. 🏨 Booking Service (Booking Service:3000)

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| POST | `/booking/` | ❌ Not required | Create a new booking |
| GET | `/booking/unavailable` | ❌ Not required | Check room availability |
| GET | `/booking/summary` | ❌ Not required | Get booking summaries |
| GET | `/booking/{id}` | ⚠️ Optional | Get booking by ID |
| PUT | `/booking/{id}` | ⚠️ Optional | Update booking |
| DELETE | `/booking/{id}` | ⚠️ Optional | Delete booking |
| GET | `/booking/` | ⚠️ Optional | List all bookings |

### 3. 🛏️ Room Service (Room Service:3001)

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| GET | `/room/{id}` | ❌ Not required | Get room information |
| GET | `/room/` | ❌ Not required | List rooms (with filtering) |
| POST | `/room/` | ⚠️ Optional | Create a new room |
| PUT | `/room/{id}` | ⚠️ Optional | Update room |
| DELETE | `/room/{id}` | ⚠️ Optional | Delete room |

### 4. 📨 Message Service (Message Service:3006)

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| GET | `/message/` | ❌ Not required | List messages (summary format) |
| POST | `/message/` | ❌ Not required | Create a new message |
| GET | `/message/{id}` | ❌ Not required | Get full message by ID |
| GET | `/message/count` | ❌ Not required | Get message count |
| PUT | `/message/{id}/read` | ⚠️ Optional | Mark as read |
| DELETE | `/message/{id}` | ⚠️ Optional | Delete message |

### 5. 🏢 Branding Service (Branding Service:3002)

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| GET | `/branding/` | ❌ Not required | Get branding information |
| PUT | `/branding/` | ⚠️ Optional | Update branding information |

### 6. 📊 Report Service (Report Service:3005)

| Method | Endpoint | Authentication | Description |
|--------|----------|----------------|-------------|
| GET | `/report/room/{id}` | ❌ Not required | Report for a specific room |
| GET | `/report/` | ✅ Required | Full report for all rooms |

---

## 📝 Authentication Status Legend

| Status | Meaning |
|--------|---------|
| ❌ Not required | Method accessible without token |
| ✅ Required | Token mandatory (cookie: `token`) |
| ⚠️ Optional | Token enhances functionality or required for modifications |

---

**Version**: 1.0.0  
**Corresponds to**: Restful Booker Platform v2.1  
**Updated**: 2024-12-24