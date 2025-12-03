'use client';

import { useState, useEffect } from 'react';
import { Globe, Trash2, Loader2 } from 'lucide-react';
import { websiteAPI } from '@/lib/api';

interface Website {
  id: number;
  url: string;
  summary: string;
  chunks_count: number;
  created_at: string;
}

export default function WebsitePage() {
  const [websites, setWebsites] = useState<Website[]>([]);
  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [url, setUrl] = useState('');

  useEffect(() => {
    fetchWebsites();
  }, []);

  const fetchWebsites = async () => {
    setLoading(true);
    try {
      const response = await websiteAPI.list();
      setWebsites(response.data);
    } catch (error) {
      console.error('Failed to fetch websites:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!url.trim()) return;

    setSubmitting(true);
    try {
      await websiteAPI.load(url);
      setUrl('');
      await fetchWebsites();
      alert('Website loaded successfully!');
    } catch (error: any) {
      console.error('Failed to load website:', error);
      alert(error.response?.data?.detail || 'Failed to load website');
    } finally {
      setSubmitting(false);
    }
  };

  const deleteWebsite = async (id: number) => {
    if (!confirm('Delete this website?')) return;
    try {
      await websiteAPI.delete(id);
      setWebsites(websites.filter(w => w.id !== id));
    } catch (error) {
      console.error('Delete failed:', error);
    }
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Website Loader</h1>
        <p className="text-slate-600 mt-1">Load and analyze website content</p>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <form onSubmit={handleSubmit} className="flex gap-4">
          <input
            type="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="https://example.com"
            required
            disabled={submitting}
            className="flex-1 px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={submitting}
            className="flex items-center gap-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition disabled:opacity-50"
          >
            {submitting ? (
              <>
                <Loader2 className="w-5 h-5 animate-spin" />
                Loading...
              </>
            ) : (
              <>
                <Globe className="w-5 h-5" />
                Load Website
              </>
            )}
          </button>
        </form>
      </div>

      {loading ? (
        <div className="text-center py-12">Loading...</div>
      ) : (
        <div className="space-y-4">
          {websites.map((site) => (
            <div key={site.id} className="bg-white rounded-lg shadow p-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <Globe className="w-5 h-5 text-blue-600" />
                    <a
                      href={site.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="font-semibold text-lg text-blue-600 hover:underline"
                    >
                      {site.url}
                    </a>
                  </div>
                  <p className="text-sm text-slate-500 mt-1">
                    {site.chunks_count} chunks • {new Date(site.created_at).toLocaleDateString()}
                  </p>
                  <div className="mt-4">
                    <h3 className="font-medium text-slate-900 mb-2">Summary:</h3>
                    <p className="text-slate-700 whitespace-pre-wrap">{site.summary}</p>
                  </div>
                </div>
                <button
                  onClick={() => deleteWebsite(site.id)}
                  className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition ml-4"
                >
                  <Trash2 className="w-5 h-5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
