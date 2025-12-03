'use client';

import { usePathname } from 'next/navigation';
import { ChevronRight } from 'lucide-react';

const breadcrumbMap: Record<string, string[]> = {
  '/dashboard': ['Dashboard'],
  '/dashboard/documents': ['Dashboard', 'Documents'],
  '/dashboard/sessions': ['Dashboard', 'Chat Sessions'],
  '/dashboard/visitors': ['Dashboard', 'Visitors'],
  '/dashboard/settings': ['Dashboard', 'Widget Settings'],
  '/dashboard/account': ['Dashboard', 'Account'],
};

export function Header() {
  const pathname = usePathname();
  const breadcrumbs = breadcrumbMap[pathname] || ['Dashboard'];

  return (
    <header className="fixed top-0 left-64 right-0 h-16 border-b border-slate-200 bg-white flex items-center px-6 z-40">
      <div className="flex items-center gap-2">
        {breadcrumbs.map((crumb, idx) => (
          <div key={idx} className="flex items-center gap-2">
            {idx > 0 && <ChevronRight className="h-4 w-4 text-slate-400" />}
            <span className={idx === breadcrumbs.length - 1 ? 'font-semibold text-slate-900' : 'text-slate-600'}>
              {crumb}
            </span>
          </div>
        ))}
      </div>
    </header>
  );
}
