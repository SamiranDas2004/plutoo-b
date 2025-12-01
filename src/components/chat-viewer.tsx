'use client';

import { useEffect, useRef } from 'react';
import { ChatSession, ChatMessage, Visitor } from '@/types';
import { ChatMessageBubble } from './chat-message-bubble';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { formatDateTime } from '@/lib/utils';

interface ChatViewerProps {
  session: ChatSession;
  messages: ChatMessage[];
  visitor?: Visitor;
}

export function ChatViewer({ session, messages, visitor }: ChatViewerProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
      <div className="lg:col-span-3">
        <Card className="h-[600px] flex flex-col">
          <CardHeader className="border-b border-slate-200">
            <CardTitle className="text-lg">{session.visitorName}</CardTitle>
            <p className="text-xs text-slate-500 mt-1">
              Started {formatDateTime(session.startedAt)}
            </p>
          </CardHeader>
          <CardContent className="flex-1 overflow-y-auto p-4">
            {messages.length === 0 ? (
              <div className="flex items-center justify-center h-full text-slate-500">
                No messages yet
              </div>
            ) : (
              <>
                {messages.map((msg) => (
                  <ChatMessageBubble key={msg.id} message={msg} />
                ))}
                <div ref={messagesEndRef} />
              </>
            )}
          </CardContent>
        </Card>
      </div>

      <div>
        <Card>
          <CardHeader className="border-b border-slate-200">
            <CardTitle className="text-sm">Visitor Info</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4 pt-4">
            {visitor && (
              <>
                <div>
                  <p className="text-xs text-slate-500">Name</p>
                  <p className="text-sm font-medium text-slate-900">{visitor.name}</p>
                </div>
                <div>
                  <p className="text-xs text-slate-500">Email</p>
                  <p className="text-sm font-medium text-slate-900">{visitor.email || 'N/A'}</p>
                </div>
                <div>
                  <p className="text-xs text-slate-500">Total Messages</p>
                  <p className="text-sm font-medium text-slate-900">{visitor.totalMessages}</p>
                </div>
                <div>
                  <p className="text-xs text-slate-500">Last Active</p>
                  <p className="text-sm font-medium text-slate-900">{formatDateTime(visitor.lastActive)}</p>
                </div>
              </>
            )}
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
