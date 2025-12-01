# PlutoChat Dashboard - Setup Guide

## Overview
This is a production-ready SaaS dashboard for managing a chatbot platform. Built with Next.js 14, TypeScript, ShadCN UI, and Tailwind CSS.

## Features

### Pages Implemented
1. **Dashboard Home** - Analytics overview with key metrics
2. **Documents** - Upload, list, and manage knowledge base documents
3. **Chat Sessions** - View all chat conversations with detailed message viewer
4. **Visitors** - Track all visitors and their metadata
5. **Widget Settings** - Configure bot token, installation script, and widget appearance
6. **Account Settings** - Manage profile and password

### Components
- **Sidebar** - Persistent navigation with active state
- **Header** - Breadcrumb navigation
- **DataTable** - Reusable table with sorting and pagination
- **FileUploader** - Drag-and-drop file upload
- **ChatViewer** - Full chat conversation viewer with visitor info
- **AnalyticsCard** - Metric cards with trends
- **ColorPicker** - Widget theme customization
- **CopyButton** - Copy to clipboard utility

## Installation

### 1. Install Dependencies
```bash
npm install
```

### 2. Environment Setup
Create a `.env.local` file:
```bash
cp .env.example .env.local
```

Update the API URL to match your backend:
```
NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

### 3. Run Development Server
```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## API Integration

The dashboard expects the following backend endpoints:

### Documents
- `GET /api/documents` - List all documents
- `POST /api/documents/upload` - Upload a document
- `DELETE /api/documents/:id` - Delete a document

### Chat Sessions
- `GET /api/sessions` - List all sessions
- `GET /api/sessions/:id` - Get session details
- `GET /api/sessions/:id/messages` - Get session messages

### Visitors
- `GET /api/visitors` - List all visitors
- `GET /api/visitors/:id` - Get visitor details

### Widget Settings
- `GET /api/widget/settings` - Get widget settings
- `PUT /api/widget/settings` - Update widget settings
- `POST /api/widget/regenerate-token` - Regenerate bot token

### Analytics
- `GET /api/analytics/dashboard` - Get dashboard metrics

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `PUT /api/auth/profile` - Update user profile

## Project Structure

```
src/
├── app/
│   ├── dashboard/
│   │   ├── documents/
│   │   ├── sessions/
│   │   ├── visitors/
│   │   ├── settings/
│   │   ├── account/
│   │   └── layout.tsx
│   ├── globals.css
│   └── layout.tsx
├── components/
│   ├── ui/
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   ├── badge.tsx
│   │   ├── input.tsx
│   │   ├── tabs.tsx
│   │   └── popover.tsx
│   ├── sidebar.tsx
│   ├── header.tsx
│   ├── data-table.tsx
│   ├── file-uploader.tsx
│   ├── chat-viewer.tsx
│   ├── chat-message-bubble.tsx
│   ├── analytics-card.tsx
│   ├── copy-button.tsx
│   └── color-picker.tsx
├── lib/
│   ├── api.ts
│   └── utils.ts
├── store/
│   └── index.ts
└── types/
    └── index.ts
```

## State Management

Uses Zustand for global state management. Store includes:
- User data
- Documents list
- Chat sessions
- Messages
- Visitors
- Widget settings
- Selected session

Access store in components:
```typescript
import { useDashboardStore } from '@/store';

const { documents, setDocuments } = useDashboardStore();
```

## Styling

- **Tailwind CSS** for utility-first styling
- **ShadCN UI** components for consistent design
- **Lucide React** for icons
- Custom theme colors in `globals.css`

## Building for Production

```bash
npm run build
npm start
```

## Key Features

### Authentication
- Protected routes via middleware (to be implemented)
- Token-based API authentication
- Profile and password management

### Data Management
- Real-time data fetching with error handling
- Toast notifications for user feedback
- Pagination and sorting in tables

### File Handling
- Drag-and-drop file upload
- File size validation
- Multiple file format support (PDF, TXT, DOCX)

### Widget Configuration
- Bot token management with regeneration
- Installation script generation
- Customizable widget appearance (color, position, welcome message)

## Customization

### Adding New Pages
1. Create folder in `src/app/dashboard/[page-name]/`
2. Add `page.tsx` file
3. Update sidebar navigation in `src/components/sidebar.tsx`

### Modifying API Endpoints
Update endpoints in `src/lib/api.ts` to match your backend.

### Changing Theme Colors
Edit CSS variables in `src/app/globals.css`:
```css
:root {
  --primary: #000000;
  --secondary: #f1f5f9;
  /* ... */
}
```

## Troubleshooting

### API Connection Issues
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check CORS settings on backend
- Ensure backend is running

### Build Errors
- Clear `.next` folder: `rm -rf .next`
- Reinstall dependencies: `rm -rf node_modules && npm install`

### Styling Issues
- Rebuild Tailwind: `npm run dev` (auto-rebuilds)
- Check class names match Tailwind conventions

## Next Steps

1. Implement authentication middleware
2. Add error boundaries
3. Implement real-time updates with WebSocket
4. Add export/download functionality
5. Implement advanced filtering and search
6. Add user role-based access control
