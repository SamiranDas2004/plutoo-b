'use client';

import { useEffect } from 'react';
import { getToken, getUser } from '@/lib/auth';
import { useDashboardStore } from '@/store';

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const { setUser } = useDashboardStore();

  useEffect(() => {
    const token = getToken();
    const user = getUser();
    
    if (token && user) {
      setUser(user);
    }
  }, [setUser]);

  return <>{children}</>;
}
