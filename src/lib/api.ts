import axios from 'axios';
import { Document, ChatSession, ChatMessage, Visitor, WidgetSettings } from '@/types';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Documents
export const documentAPI = {
  list: () => api.get<Document[]>('/documents'),
  upload: (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    return api.post<Document>('/documents/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
  delete: (id: string) => api.delete(`/documents/${id}`),
};

// Chat Sessions
export const sessionAPI = {
  list: () => api.get<ChatSession[]>('/sessions'),
  get: (id: string) => api.get<ChatSession>(`/sessions/${id}`),
  messages: (sessionId: string) => api.get<ChatMessage[]>(`/sessions/${sessionId}/messages`),
};

// Visitors
export const visitorAPI = {
  list: () => api.get<Visitor[]>('/visitors'),
  get: (id: string) => api.get<Visitor>(`/visitors/${id}`),
};

// Widget Settings
export const widgetAPI = {
  get: () => api.get<WidgetSettings>('/widget/settings'),
  update: (settings: Partial<WidgetSettings>) => api.put('/widget/settings', settings),
  regenerateToken: () => api.post<{ botToken: string }>('/widget/regenerate-token'),
};

// Analytics
export const analyticsAPI = {
  dashboard: () => api.get('/analytics/dashboard'),
};

// Auth
export const authAPI = {
  login: (email: string, password: string) => api.post('/auth/login', { email, password }),
  signup: (name: string, email: string, password: string) => api.post('/auth/signup', { name, email, password }),
  logout: () => api.post('/auth/logout'),
  updateProfile: (data: { name?: string; email?: string; password?: string }) =>
    api.put('/auth/profile', data),
};

// Audio
export const audioAPI = {
  list: () => api.get('/audio'),
  upload: (file: File) => {
    const formData = new FormData();
    formData.append('file', file);
    return api.post('/audio', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
  delete: (id: number) => api.delete(`/audio/${id}`),
};

// Website
export const websiteAPI = {
  list: () => api.get('/website'),
  load: (url: string) => api.post('/website', { url }),
  delete: (id: number) => api.delete(`/website/${id}`),
};

// Tickets
export const ticketAPI = {
  list: () => api.get('/tickets/list'),
};
