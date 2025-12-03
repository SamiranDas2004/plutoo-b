'use client';

import { useEffect, useState } from 'react';
import { Plus, Trash2, Eye } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import axios from 'axios';
import toast from 'react-hot-toast';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface TextInfo {
  id: number;
  title: string;
  content: string;
  chunks_count: number;
  created_at: string;
}

export default function WriteInfoPage() {
  const [textInfos, setTextInfos] = useState<TextInfo[]>([]);
  const [loading, setLoading] = useState(true);
  const [showDialog, setShowDialog] = useState(false);
  const [viewDialog, setViewDialog] = useState(false);
  const [selectedText, setSelectedText] = useState<TextInfo | null>(null);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    fetchTextInfos();
  }, []);

  const fetchTextInfos = async () => {
    try {
      const token = localStorage.getItem('authToken');
      const response = await axios.get(`${API_BASE}/text-info/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setTextInfos(response.data);
    } catch (error) {
      toast.error('Failed to load text information');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) {
      toast.error('Title and content are required');
      return;
    }

    setSubmitting(true);
    try {
      const token = localStorage.getItem('authToken');
      await axios.post(
        `${API_BASE}/text-info/`,
        { title, content },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      toast.success('Text information saved successfully!');
      setTitle('');
      setContent('');
      setShowDialog(false);
      fetchTextInfos();
    } catch (error) {
      toast.error('Failed to save text information');
    } finally {
      setSubmitting(false);
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm('Are you sure you want to delete this?')) return;

    try {
      const token = localStorage.getItem('authToken');
      await axios.delete(`${API_BASE}/text-info/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      toast.success('Deleted successfully');
      fetchTextInfos();
    } catch (error) {
      toast.error('Failed to delete');
    }
  };

  const handleView = (text: TextInfo) => {
    setSelectedText(text);
    setViewDialog(true);
  };

  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-slate-900">Write Information</h1>
          <p className="text-slate-600 mt-1">
            Write custom text about your website/platform for AI training
          </p>
        </div>
        <Button onClick={() => setShowDialog(true)}>
          <Plus className="h-4 w-4 mr-2" />
          Add New
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {textInfos.map((text) => (
          <Card key={text.id}>
            <CardHeader>
              <CardTitle className="text-lg">{text.title}</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-slate-600 mb-4 line-clamp-3">
                {text.content}
              </p>
              <div className="flex justify-between items-center text-xs text-slate-500">
                <span>{text.chunks_count} chunks</span>
                <span>{new Date(text.created_at).toLocaleDateString()}</span>
              </div>
              <div className="flex gap-2 mt-4">
                <Button
                  variant="outline"
                  size="sm"
                  className="flex-1"
                  onClick={() => handleView(text)}
                >
                  <Eye className="h-4 w-4 mr-1" />
                  View
                </Button>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={() => handleDelete(text.id)}
                >
                  <Trash2 className="h-4 w-4 text-red-600" />
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {textInfos.length === 0 && (
        <Card>
          <CardContent className="text-center py-12">
            <p className="text-slate-600 mb-4">No text information yet</p>
            <Button onClick={() => setShowDialog(true)}>
              <Plus className="h-4 w-4 mr-2" />
              Add Your First Entry
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Add Dialog */}
      <Dialog open={showDialog} onOpenChange={setShowDialog}>
        <DialogContent className="max-w-2xl">
          <DialogHeader>
            <DialogTitle>Add Text Information</DialogTitle>
          </DialogHeader>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-2">Title</label>
              <Input
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="e.g., About Our Company"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Content</label>
              <textarea
                value={content}
                onChange={(e) => setContent(e.target.value)}
                placeholder="Write detailed information about your website/platform..."
                className="w-full min-h-[300px] p-3 border rounded-md"
                required
              />
            </div>
            <div className="flex justify-end gap-2">
              <Button
                type="button"
                variant="outline"
                onClick={() => setShowDialog(false)}
              >
                Cancel
              </Button>
              <Button type="submit" disabled={submitting}>
                {submitting ? 'Saving...' : 'Save'}
              </Button>
            </div>
          </form>
        </DialogContent>
      </Dialog>

      {/* View Dialog */}
      <Dialog open={viewDialog} onOpenChange={setViewDialog}>
        <DialogContent className="max-w-2xl">
          <DialogHeader>
            <DialogTitle>{selectedText?.title}</DialogTitle>
          </DialogHeader>
          <div className="space-y-4">
            <div className="prose max-w-none">
              <p className="whitespace-pre-wrap">{selectedText?.content}</p>
            </div>
            <div className="text-sm text-slate-500">
              <p>Chunks: {selectedText?.chunks_count}</p>
              <p>Created: {selectedText && new Date(selectedText.created_at).toLocaleString()}</p>
            </div>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
