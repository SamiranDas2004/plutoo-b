'use client';

import { useEffect, useState } from 'react';
import { ColumnDef } from '@tanstack/react-table';
import { Trash2, Download } from 'lucide-react';
import { Document } from '@/types';
import { DataTable } from '@/components/data-table';
import { FileUploader } from '@/components/file-uploader';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { documentAPI } from '@/lib/api';
import { formatBytes, formatDate } from '@/lib/utils';
import { useDashboardStore } from '@/store';
import toast from 'react-hot-toast';

export default function DocumentsPage() {
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const { documents, setDocuments, addDocument, removeDocument } = useDashboardStore();

  useEffect(() => {
    fetchDocuments();
  }, []);

  const fetchDocuments = async () => {
    try {
      const response = await documentAPI.list();
      setDocuments(response.data);
    } catch (error) {
      toast.error('Failed to load documents');
    } finally {
      setLoading(false);
    }
  };

  const handleFileSelect = async (file: File) => {
    setUploading(true);
    try {
      const response = await documentAPI.upload(file);
      addDocument(response.data);
      toast.success('Document uploaded successfully');
    } catch (error) {
      toast.error('Failed to upload document');
    } finally {
      setUploading(false);
    }
  };

  const handleDelete = async (id: string) => {
    try {
      await documentAPI.delete(id);
      removeDocument(id);
      toast.success('Document deleted');
    } catch (error) {
      toast.error('Failed to delete document');
    }
  };

  const columns: ColumnDef<Document>[] = [
    {
      accessorKey: 'name',
      header: 'Name',
      cell: ({ row }) => (
        <div className="flex items-center gap-2">
          <FileIcon type={row.original.type} />
          {row.original.name}
        </div>
      ),
    },
    {
      accessorKey: 'size',
      header: 'Size',
      cell: ({ row }) => formatBytes(row.original.size),
    },
    {
      accessorKey: 'type',
      header: 'Type',
      cell: ({ row }) => <Badge variant="secondary">{row.original.type}</Badge>,
    },
    {
      accessorKey: 'uploadedAt',
      header: 'Uploaded',
      cell: ({ row }) => formatDate(row.original.uploadedAt),
    },
    {
      id: 'actions',
      cell: ({ row }) => (
        <div className="flex gap-2">
          <Button variant="ghost" size="sm">
            <Download className="h-4 w-4" />
          </Button>
          <Button
            variant="ghost"
            size="sm"
            onClick={() => handleDelete(row.original.id)}
          >
            <Trash2 className="h-4 w-4 text-red-600" />
          </Button>
        </div>
      ),
    },
  ];

  if (loading) {
    return <div className="text-center py-12">Loading...</div>;
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Documents</h1>
        <p className="text-slate-600 mt-1">Upload and manage your knowledge base documents.</p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Upload Document</CardTitle>
        </CardHeader>
        <CardContent>
          <FileUploader onFileSelect={handleFileSelect} />
          {uploading && <p className="text-sm text-slate-600 mt-2">Uploading...</p>}
        </CardContent>
      </Card>

      <div>
        <h2 className="text-lg font-semibold text-slate-900 mb-4">
          Your Documents ({documents.length})
        </h2>
        <DataTable columns={columns} data={documents} />
      </div>
    </div>
  );
}

function FileIcon({ type }: { type: string }) {
  return (
    <div className="w-8 h-8 rounded bg-slate-100 flex items-center justify-center text-xs font-semibold text-slate-600">
      {type.split('/')[1]?.substring(0, 3).toUpperCase() || 'DOC'}
    </div>
  );
}
