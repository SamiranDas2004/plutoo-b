'use client';

import { useEffect, useState } from 'react';
import { ColumnDef } from '@tanstack/react-table';
import { Visitor } from '@/types';
import { DataTable } from '@/components/data-table';
import { visitorAPI } from '@/lib/api';
import { formatDateTime } from '@/lib/utils';
import { useDashboardStore } from '@/store';
import toast from 'react-hot-toast';

export default function VisitorsPage() {
  const [loading, setLoading] = useState(true);
  const { visitors, setVisitors } = useDashboardStore();

  useEffect(() => {
    fetchVisitors();
  }, []);

  const fetchVisitors = async () => {
    try {
      const response = await visitorAPI.list();
      setVisitors(response.data);
    } catch (error) {
      toast.error('Failed to load visitors');
    } finally {
      setLoading(false);
    }
  };

  const columns: ColumnDef<Visitor>[] = [
    {
      accessorKey: 'id',
      header: 'Visitor ID',
      cell: ({ row }) => (
        <code className="text-xs bg-slate-100 px-2 py-1 rounded">
          {row.original.id.substring(0, 8)}...
        </code>
      ),
    },
    {
      accessorKey: 'name',
      header: 'Name',
    },
    {
      accessorKey: 'email',
      header: 'Email',
      cell: ({ row }) => row.original.email || '—',
    },
    {
      accessorKey: 'totalMessages',
      header: 'Messages',
    },
    {
      accessorKey: 'createdAt',
      header: 'Joined',
      cell: ({ row }) => formatDateTime(row.original.createdAt),
    },
    {
      accessorKey: 'lastActive',
      header: 'Last Active',
      cell: ({ row }) => formatDateTime(row.original.lastActive),
    },
  ];

  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Visitors</h1>
        <p className="text-slate-600 mt-1">Track all visitors and their interactions.</p>
      </div>

      <DataTable columns={columns} data={visitors} />
    </div>
  );
}
