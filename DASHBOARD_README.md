# PlutoChat Dashboard - Production-Ready SaaS Dashboard

A beautiful, modern SaaS dashboard for managing a chatbot platform. Built with Next.js 14, TypeScript, ShadCN UI, and Tailwind CSS.

## 🎯 Features

### Dashboard Pages
- **Dashboard Home** - Real-time analytics and metrics
- **Documents** - Upload, manage, and organize knowledge base documents
- **Chat Sessions** - View and manage all chat conversations
- **Visitors** - Track visitor information and activity
- **Widget Settings** - Configure and customize the chatbot widget
- **Account Settings** - Manage user profile and security

### Key Capabilities
- 📊 Real-time analytics with trend indicators
- 📁 Drag-and-drop file upload with validation
- 💬 Full chat conversation viewer with message bubbles
- 👥 Visitor tracking and metadata
- 🎨 Widget customization (color, position, welcome message)
- 🔐 Secure authentication and profile management
- 📱 Responsive design for all devices
- ⚡ Fast performance with Next.js 14

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Configure environment**
   ```bash
   cp .env.local.example .env.local
   # Edit .env.local with your API URL
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open dashboard**
   Visit `http://localhost:3000`

## 📚 Documentation

- **[QUICK_START.md](./QUICK_START.md)** - 5-minute setup guide
- **[DASHBOARD_SETUP.md](./DASHBOARD_SETUP.md)** - Detailed setup and customization
- **[API_REFERENCE.md](./API_REFERENCE.md)** - Complete API documentation
- **[IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md)** - Architecture overview

## 🏗️ Architecture

### Tech Stack
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **UI Components**: ShadCN UI
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Icons**: Lucide React
- **Notifications**: React Hot Toast
- **Tables**: TanStack React Table

### Project Structure
```
src/
├── app/                    # Next.js app directory
│   ├── dashboard/         # Dashboard pages
│   ├── layout.tsx         # Root layout
│   ├── globals.css        # Global styles
│   └── page.tsx           # Home redirect
├── components/            # React components
│   ├── ui/               # ShadCN UI components
│   ├── sidebar.tsx       # Navigation sidebar
│   ├── header.tsx        # Page header
│   ├── data-table.tsx    # Reusable table
│   └── ...               # Other components
├── lib/                   # Utilities
│   ├── api.ts            # API client
│   └── utils.ts          # Helper functions
├── store/                # State management
│   └── index.ts          # Zustand store
└── types/                # TypeScript types
    └── index.ts          # Data models
```

## 🔌 API Integration

### Environment Configuration
```env
NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

### Required Backend Endpoints

**Documents**
```
GET    /documents
POST   /documents/upload
DELETE /documents/:id
```

**Chat Sessions**
```
GET /sessions
GET /sessions/:id
GET /sessions/:id/messages
```

**Visitors**
```
GET /visitors
GET /visitors/:id
```

**Widget Settings**
```
GET    /widget/settings
PUT    /widget/settings
POST   /widget/regenerate-token
```

**Analytics**
```
GET /analytics/dashboard
```

**Authentication**
```
PUT /auth/profile
```

See [API_REFERENCE.md](./API_REFERENCE.md) for complete details.

## 🎨 Customization

### Theme Colors
Edit `src/app/globals.css`:
```css
:root {
  --primary: #000000;
  --secondary: #f1f5f9;
  --destructive: #ef4444;
  /* ... */
}
```

### Add New Page
1. Create folder: `src/app/dashboard/[page-name]/`
2. Add `page.tsx` file
3. Update sidebar in `src/components/sidebar.tsx`

### Modify Components
All components are in `src/components/` and fully customizable.

## 📦 Components

### UI Components (ShadCN)
- Button
- Card
- Dialog
- Badge
- Input
- Tabs
- Popover
- DropdownMenu

### Custom Components
- **Sidebar** - Navigation with active state
- **Header** - Breadcrumb navigation
- **DataTable** - Sortable, paginated table
- **FileUploader** - Drag-and-drop upload
- **ChatViewer** - Full conversation view
- **ChatMessageBubble** - Message display
- **AnalyticsCard** - Metric cards
- **CopyButton** - Copy to clipboard
- **ColorPicker** - Color selection

## 🔐 Security

### Authentication
- Token-based API authentication
- Secure token storage (implement httpOnly cookies)
- Protected routes (implement middleware)

### Best Practices
- Validate all inputs on backend
- Implement CORS properly
- Use HTTPS in production
- Implement rate limiting
- Sanitize user data

## 📊 State Management

### Zustand Store
```typescript
const { 
  user, 
  documents, 
  sessions, 
  messages, 
  visitors, 
  widgetSettings,
  selectedSession 
} = useDashboardStore();
```

### API Client
```typescript
import { documentAPI, sessionAPI, visitorAPI } from '@/lib/api';

// Usage
const docs = await documentAPI.list();
const sessions = await sessionAPI.list();
```

## 🚀 Production Build

```bash
npm run build
npm start
```

## 📱 Responsive Design

- Mobile-first approach
- Tailwind CSS responsive utilities
- Sidebar collapses on mobile
- Touch-friendly components

## ⚡ Performance

- Server-side rendering with Next.js
- Optimized images
- Code splitting
- Efficient state management
- Minimal bundle size

## 🐛 Troubleshooting

### API Connection Issues
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check backend is running
- Verify CORS settings

### Build Errors
```bash
rm -rf .next node_modules
npm install
npm run dev
```

### Styling Issues
- Restart dev server
- Clear browser cache
- Check Tailwind class names

## 📝 Development

### Available Scripts
```bash
npm run dev      # Start development server
npm run build    # Build for production
npm start        # Start production server
npm run lint     # Run ESLint
```

### Code Style
- TypeScript for type safety
- ESLint for code quality
- Tailwind CSS for styling
- Component-based architecture

## 🔄 Workflow

1. **Setup** - Install dependencies and configure API
2. **Development** - Run dev server and build features
3. **Testing** - Test with your backend API
4. **Customization** - Adjust theme and components
5. **Deployment** - Build and deploy to production

## 📞 Support

### Documentation
- [QUICK_START.md](./QUICK_START.md) - Quick setup
- [DASHBOARD_SETUP.md](./DASHBOARD_SETUP.md) - Detailed guide
- [API_REFERENCE.md](./API_REFERENCE.md) - API docs
- [IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md) - Architecture

### Common Issues
- Check documentation files
- Review error messages
- Check browser console
- Verify API configuration

## 📄 License

This dashboard is provided as-is for your SaaS platform.

## 🎯 Next Steps

1. ✅ Install and setup
2. ✅ Configure API URL
3. 🔄 Connect your backend
4. 🎨 Customize theme
5. 🔐 Implement authentication
6. 📦 Deploy to production

---

**Version**: 1.0.0  
**Status**: Production Ready  
**Last Updated**: 2024

Built with ❤️ for modern SaaS platforms
