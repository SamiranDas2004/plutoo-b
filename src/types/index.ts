export interface Document {
  id: string;
  name: string;
  size: number;
  type: string;
  uploadedAt: string;
  url?: string;
}

export interface ChatSession {
  id: string;
  visitorId: string;
  visitorName: string;
  startedAt: string;
  lastMessageAt: string;
  messageCount: number;
}

export interface ChatMessage {
  id: string;
  sessionId: string;
  sender: 'user' | 'bot';
  content: string;
  timestamp: string;
}

export interface Visitor {
  id: string;
  name: string;
  email?: string;
  totalMessages: number;
  createdAt: string;
  lastActive: string;
}

export interface WidgetSettings {
  botToken: string;
  color: string;
  position: 'left' | 'right';
  welcomeMessage: string;
}

export interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
}
