# API Reference

## Base URL
```
http://localhost:3001/api
```

## Authentication
All requests should include the Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### Documents

#### List Documents
```
GET /documents
Response: Document[]
```

#### Upload Document
```
POST /documents/upload
Content-Type: multipart/form-data
Body: { file: File }
Response: Document
```

#### Delete Document
```
DELETE /documents/:id
Response: { success: boolean }
```

### Chat Sessions

#### List Sessions
```
GET /sessions
Response: ChatSession[]
```

#### Get Session
```
GET /sessions/:id
Response: ChatSession
```

#### Get Session Messages
```
GET /sessions/:id/messages
Response: ChatMessage[]
```

### Visitors

#### List Visitors
```
GET /visitors
Response: Visitor[]
```

#### Get Visitor
```
GET /visitors/:id
Response: Visitor
```

### Widget Settings

#### Get Settings
```
GET /widget/settings
Response: WidgetSettings
```

#### Update Settings
```
PUT /widget/settings
Body: {
  color?: string;
  position?: 'left' | 'right';
  welcomeMessage?: string;
}
Response: WidgetSettings
```

#### Regenerate Token
```
POST /widget/regenerate-token
Response: { botToken: string }
```

### Analytics

#### Dashboard Metrics
```
GET /analytics/dashboard
Response: {
  visitorsToday: number;
  totalMessages: number;
  totalSessions: number;
  documentsCount: number;
}
```

### Authentication

#### Login
```
POST /auth/login
Body: {
  email: string;
  password: string;
}
Response: {
  token: string;
  user: User;
}
```

#### Logout
```
POST /auth/logout
Response: { success: boolean }
```

#### Update Profile
```
PUT /auth/profile
Body: {
  name?: string;
  email?: string;
  password?: string;
}
Response: User
```

## Data Types

### Document
```typescript
{
  id: string;
  name: string;
  size: number;
  type: string;
  uploadedAt: string;
  url?: string;
}
```

### ChatSession
```typescript
{
  id: string;
  visitorId: string;
  visitorName: string;
  startedAt: string;
  lastMessageAt: string;
  messageCount: number;
}
```

### ChatMessage
```typescript
{
  id: string;
  sessionId: string;
  sender: 'user' | 'bot';
  content: string;
  timestamp: string;
}
```

### Visitor
```typescript
{
  id: string;
  name: string;
  email?: string;
  totalMessages: number;
  createdAt: string;
  lastActive: string;
}
```

### WidgetSettings
```typescript
{
  botToken: string;
  color: string;
  position: 'left' | 'right';
  welcomeMessage: string;
}
```

### User
```typescript
{
  id: string;
  name: string;
  email: string;
  avatar?: string;
}
```

## Error Handling

All errors follow this format:
```json
{
  "error": "Error message",
  "code": "ERROR_CODE",
  "status": 400
}
```

Common status codes:
- 200: Success
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Server Error

## Rate Limiting

- 100 requests per minute per IP
- 1000 requests per hour per user

## CORS

The API should allow requests from:
- http://localhost:3000 (development)
- https://yourdomain.com (production)
