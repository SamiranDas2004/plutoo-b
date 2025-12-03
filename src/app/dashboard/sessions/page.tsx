'use client';

import { useEffect, useState } from 'react';
import { ColumnDef } from '@tanstack/react-table';
import { ChevronRight } from 'lucide-react';
import { ChatSession } from '@/types';
import { DataTable } from '@/components/data-table';
import { ChatViewer } from '@/components/chat-viewer';
import { Button } from '@/components/ui/button';
import { sessionAPI } from '@/lib/api';
import { formatDateTime } from '@/lib/utils';
import { useDashboardStore } from '@/store';
import toast from 'react-hot-toast';

export default function SessionsPage() {
  const [loading, setLoading] = useState(true);
  const { sessions, setSessions, selectedSession, setSelectedSession, messages, setMessages } = useDashboardStore();

  useEffect(() => {
    fetchSessions();
  }, []);

  const fetchSessions = async () => {
    try {
      const response = await sessionAPI.list();
      setSessions(response.data);
    } catch (error) {
      toast.error('Failed to load sessions');
    } finally {
      setLoading(false);
    }
  };

  const handleSelectSession = async (session: ChatSession) => {
    setSelectedSession(session);
    try {
      const response = await sessionAPI.messages(session.id);
      setMessages(response.data);
    } catch (error) {
      toast.error('Failed to load messages');
    }
  };

  const columns: ColumnDef<ChatSession>[] = [
    {
      accessorKey: 'visitorName',
      header: 'Visitor',
    },
    {
      accessorKey: 'messageCount',
      header: 'Messages',
    },
    {
      accessorKey: 'startedAt',
      header: 'Started',
      cell: ({ row }) => formatDateTime(row.original.startedAt),
    },
    {
      accessorKey: 'lastMessageAt',
      header: 'Last Message',
      cell: ({ row }) => formatDateTime(row.original.lastMessageAt),
    },
    {
      id: 'actions',
      cell: ({ row }) => (
        <Button
          variant="ghost"
          size="sm"
          onClick={() => handleSelectSession(row.original)}
        >
          <ChevronRight className="h-4 w-4" />
        </Button>
      ),
    },
  ];

  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }

  if (selectedSession) {
    return (
      <div className="space-y-6">
        <Button variant="outline" onClick={() => setSelectedSession(null)}>
          ← Back to Sessions
        </Button>
        <ChatViewer session={selectedSession} messages={messages} />
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Chat Sessions</h1>
        <p className="text-slate-600 mt-1">View and manage all chat conversations.</p>
      </div>

      <DataTable columns={columns} data={sessions} />
    </div>
  );
}
