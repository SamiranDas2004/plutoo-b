# Authentication Setup

## Overview
The dashboard includes complete authentication with JWT token storage and protected routes.

## Features
- ✅ Login with email/password
- ✅ Signup with name, email, password
- ✅ JWT token storage in localStorage
- ✅ Protected routes (redirect to login if not authenticated)
- ✅ Logout functionality
- ✅ Auto-login on page refresh

## Pages

### Login Page
**Route**: `/login`

```typescript
// Login with email and password
POST /auth/login
{
  "email": "user@example.com",
  "password": "password123"
}

// Response
{
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 5,
    "email": "user@example.com",
    "namespace": "5"
  }
}
```

### Signup Page
**Route**: `/signup`

```typescript
// Create new account
POST /auth/signup
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}

// Response (same as login)
{
  "message": "Account created",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 5,
    "email": "john@example.com",
    "namespace": "5"
  }
}
```

## Token Storage

### localStorage Keys
- `authToken` - JWT token
- `authUser` - User object (JSON)

### Token Usage
The token is automatically added to all API requests:
```
Authorization: Bearer <token>
```

## Auth Utilities

### `src/lib/auth.ts`

```typescript
// Get stored token
const token = getToken();

// Store token
setToken(token);

// Remove token
removeToken();

// Get stored user
const user = getUser();

// Store user
setUser(user);

// Remove user
removeUser();

// Check if authenticated
const isAuth = isAuthenticated();
```

## Protected Routes

### Middleware
**File**: `src/middleware.ts`

Routes that require authentication:
- `/dashboard/*` - All dashboard pages

Routes that redirect if authenticated:
- `/login` - Redirects to `/dashboard` if already logged in
- `/signup` - Redirects to `/dashboard` if already logged in

### Route Protection
```typescript
// Automatic redirect to login if not authenticated
// Automatic redirect to dashboard if already logged in
```

## Flow

### Login Flow
1. User enters email and password
2. Submit to `/auth/login`
3. Receive token and user data
4. Store token in localStorage
5. Store user in localStorage
6. Redirect to `/dashboard`

### Signup Flow
1. User enters name, email, password
2. Submit to `/auth/signup`
3. Receive token and user data
4. Store token in localStorage
5. Store user in localStorage
6. Redirect to `/dashboard`

### Logout Flow
1. Click logout button
2. Remove token from localStorage
3. Remove user from localStorage
4. Redirect to `/login`

### Auto-Login Flow
1. App loads
2. Check for token in localStorage
3. If token exists, restore user data
4. Redirect to `/dashboard`
5. If no token, redirect to `/login`

## Backend Requirements

### Login Endpoint
```
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response 200:
{
  "message": "Login successful",
  "token": "JWT_TOKEN",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "namespace": "namespace_id"
  }
}

Response 401:
{
  "message": "Invalid credentials"
}
```

### Signup Endpoint
```
POST /auth/signup
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}

Response 201:
{
  "message": "Account created",
  "token": "JWT_TOKEN",
  "user": {
    "id": "user_id",
    "email": "john@example.com",
    "namespace": "namespace_id"
  }
}

Response 400:
{
  "message": "Email already exists"
}
```

## Security Considerations

1. **Token Storage**: Currently using localStorage (consider httpOnly cookies for production)
2. **Token Expiration**: Implement token refresh logic
3. **HTTPS**: Always use HTTPS in production
4. **CORS**: Configure backend CORS properly
5. **Password**: Validate password strength on backend

## Implementation Checklist

- [x] Login page created
- [x] Signup page created
- [x] Token storage in localStorage
- [x] User data storage
- [x] Protected routes middleware
- [x] Logout functionality
- [x] Auto-login on page refresh
- [x] Auth provider for app initialization
- [ ] Token refresh logic (to implement)
- [ ] Password reset (to implement)
- [ ] Email verification (to implement)
- [ ] Two-factor authentication (to implement)

## Files Created

- `src/app/login/page.tsx` - Login page
- `src/app/signup/page.tsx` - Signup page
- `src/lib/auth.ts` - Auth utilities
- `src/middleware.ts` - Route protection
- `src/components/auth-provider.tsx` - Auth provider
- `AUTHENTICATION.md` - This file

## Testing

### Test Login
1. Go to `http://localhost:3000/login`
2. Enter email and password
3. Click Login
4. Should redirect to `/dashboard`

### Test Signup
1. Go to `http://localhost:3000/signup`
2. Enter name, email, password
3. Click Sign Up
4. Should redirect to `/dashboard`

### Test Logout
1. Click Logout button in sidebar
2. Should redirect to `/login`

### Test Protected Routes
1. Go to `http://localhost:3000/dashboard` without logging in
2. Should redirect to `/login`

### Test Auto-Login
1. Login successfully
2. Refresh the page
3. Should stay on `/dashboard` (not redirect to login)

## Troubleshooting

### Token not persisting
- Check browser localStorage
- Verify `setToken()` is called after login
- Check browser console for errors

### Redirect loops
- Check middleware configuration
- Verify token is being stored correctly
- Check browser cookies/localStorage

### API requests failing
- Verify token is being sent in Authorization header
- Check backend CORS settings
- Verify backend is running

## Next Steps

1. Test login/signup with your backend
2. Implement token refresh logic
3. Add password reset functionality
4. Add email verification
5. Implement two-factor authentication
6. Move to httpOnly cookies for token storage
