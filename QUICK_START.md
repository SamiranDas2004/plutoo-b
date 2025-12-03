# Quick Start Guide

## 5-Minute Setup

### Step 1: Install Dependencies
```bash
npm install
```

### Step 2: Configure API
Create `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

### Step 3: Start Development Server
```bash
npm run dev
```

### Step 4: Open Dashboard
Visit `http://localhost:3000`

---

## What's Included

### 6 Dashboard Pages
- Dashboard (analytics overview)
- Documents (upload & manage)
- Chat Sessions (view conversations)
- Visitors (track users)
- Widget Settings (configure bot)
- Account (profile management)

### 15+ Components
- Sidebar navigation
- Data tables with sorting/pagination
- File uploader with drag-and-drop
- Chat viewer with message bubbles
- Color picker
- Copy button
- Analytics cards

### State Management
- Zustand store for global state
- Axios API client with auth
- TypeScript types for all data

---

## Backend Integration

### Required Endpoints

**Documents**
- `GET /documents` - List
- `POST /documents/upload` - Upload
- `DELETE /documents/:id` - Delete

**Sessions**
- `GET /sessions` - List
- `GET /sessions/:id/messages` - Get messages

**Visitors**
- `GET /visitors` - List

**Widget**
- `GET /widget/settings` - Get settings
- `PUT /widget/settings` - Update
- `POST /widget/regenerate-token` - New token

**Analytics**
- `GET /analytics/dashboard` - Metrics

**Auth**
- `PUT /auth/profile` - Update profile

See `API_REFERENCE.md` for full details.

---

## Customization

### Change Theme Color
Edit `src/app/globals.css`:
```css
:root {
  --primary: #your-color;
}
```

### Add New Page
1. Create `src/app/dashboard/[page]/page.tsx`
2. Update `src/components/sidebar.tsx`

### Modify API Endpoints
Edit `src/lib/api.ts`

---

## Common Tasks

### Add Loading State
```typescript
const [loading, setLoading] = useState(true);
// ... fetch data
setLoading(false);

if (loading) return <div>Loading...</div>;
```

### Show Toast Notification
```typescript
import toast from 'react-hot-toast';

toast.success('Success message');
toast.error('Error message');
```

### Access Global State
```typescript
import { useDashboardStore } from '@/store';

const { documents, setDocuments } = useDashboardStore();
```

### Make API Call
```typescript
import { documentAPI } from '@/lib/api';

const response = await documentAPI.list();
```

---

## Troubleshooting

**API Connection Error?**
- Check `NEXT_PUBLIC_API_URL` in `.env.local`
- Ensure backend is running
- Check CORS settings

**Build Error?**
```bash
rm -rf .next node_modules
npm install
npm run dev
```

**Styling Issues?**
- Restart dev server
- Clear browser cache
- Check Tailwind class names

---

## Production Build

```bash
npm run build
npm start
```

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Configure API URL
3. ✅ Start dev server
4. 🔄 Connect your backend
5. 🔐 Add authentication
6. 🎨 Customize theme
7. 📦 Deploy to production

---

**Need Help?**
- See `DASHBOARD_SETUP.md` for detailed setup
- See `API_REFERENCE.md` for API details
- See `IMPLEMENTATION_SUMMARY.md` for architecture overview
