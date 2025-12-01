'use client';

import Link from 'next/link';
import { usePathname, useRouter } from 'next/navigation';
import {
  LayoutDashboard,
  FileText,
  MessageSquare,
  Users,
  Settings,
  User,
  LogOut,
  Mic,
  Globe,
  Upload,
  Ticket,
} from 'lucide-react';
import { cn } from '@/lib/utils';
import { Button } from './ui/button';
import { removeToken, removeUser } from '@/lib/auth';
import toast from 'react-hot-toast';

const navSections = [
  {
    title: null,
    items: [
      { href: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
    ],
  },
  {
    title: 'Upload Information',
    items: [
      { href: '/dashboard/documents', label: 'Documents', icon: FileText },
      { href: '/dashboard/audio', label: 'Audio Recordings', icon: Mic },
      { href: '/dashboard/website', label: 'Website Loader', icon: Globe },
      { href: '/dashboard/write-info', label: 'Write Information', icon: Upload },
    ],
  },
  {
    title: 'Analytics',
    items: [
      { href: '/dashboard/sessions', label: 'Chat Sessions', icon: MessageSquare },
      { href: '/dashboard/visitors', label: 'Visitors', icon: Users },
      { href: '/dashboard/tickets', label: 'Support Tickets', icon: Ticket },
    ],
  },
  {
    title: 'Settings',
    items: [
      { href: '/dashboard/settings', label: 'Widget Settings', icon: Settings },
      { href: '/dashboard/account', label: 'Account', icon: User },
    ],
  },
];

function LogoutButton() {
  const router = useRouter();

  const handleLogout = () => {
    removeToken();
    removeUser();
    toast.success('Logged out successfully');
    router.push('/login');
  };

  return (
    <Button variant="outline" className="w-full justify-start" onClick={handleLogout}>
      <LogOut className="h-4 w-4" />
      Logout
    </Button>
  );
}

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed left-0 top-0 h-screen w-64 border-r border-slate-200 bg-white">
      <div className="flex flex-col h-full">
        <div className="p-6 border-b border-slate-200">
          <h1 className="text-xl font-bold text-slate-900">PlutoChat</h1>
        </div>

        <nav className="flex-1 overflow-y-auto p-4 space-y-6">
          {navSections.map((section, idx) => (
            <div key={idx}>
              {section.title && (
                <h3 className="px-3 mb-2 text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  {section.title}
                </h3>
              )}
              <div className="space-y-1">
                {section.items.map((item) => {
                  const Icon = item.icon;
                  const isActive = pathname === item.href;
                  return (
                    <Link key={item.href} href={item.href}>
                      <Button
                        variant={isActive ? 'default' : 'ghost'}
                        className={cn(
                          'w-full justify-start',
                          isActive && 'bg-slate-900 text-white'
                        )}
                      >
                        <Icon className="h-4 w-4" />
                        {item.label}
                      </Button>
                    </Link>
                  );
                })}
              </div>
            </div>
          ))}
        </nav>

        <div className="p-4 border-t border-slate-200 space-y-2">
          <LogoutButton />
        </div>
      </div>
    </aside>
  );
}
