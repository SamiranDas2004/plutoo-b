import { create } from 'zustand';
import { Document, ChatSession, ChatMessage, Visitor, WidgetSettings, User } from '@/types';

interface DashboardStore {
  user: User | null;
  documents: Document[];
  sessions: ChatSession[];
  messages: ChatMessage[];
  visitors: Visitor[];
  widgetSettings: WidgetSettings | null;
  selectedSession: ChatSession | null;
  
  setUser: (user: User) => void;
  setDocuments: (docs: Document[]) => void;
  addDocument: (doc: Document) => void;
  removeDocument: (id: string) => void;
  setSessions: (sessions: ChatSession[]) => void;
  setMessages: (messages: ChatMessage[]) => void;
  setVisitors: (visitors: Visitor[]) => void;
  setWidgetSettings: (settings: WidgetSettings) => void;
  setSelectedSession: (session: ChatSession | null) => void;
}

export const useDashboardStore = create<DashboardStore>((set) => ({
  user: null,
  documents: [],
  sessions: [],
  messages: [],
  visitors: [],
  widgetSettings: null,
  selectedSession: null,
  
  setUser: (user) => set({ user }),
  setDocuments: (documents) => set({ documents }),
  addDocument: (doc) => set((state) => ({ documents: [...state.documents, doc] })),
  removeDocument: (id) => set((state) => ({ documents: state.documents.filter(d => d.id !== id) })),
  setSessions: (sessions) => set({ sessions }),
  setMessages: (messages) => set({ messages }),
  setVisitors: (visitors) => set({ visitors }),
  setWidgetSettings: (widgetSettings) => set({ widgetSettings }),
  setSelectedSession: (selectedSession) => set({ selectedSession }),
}));
