'use client';

import { useState, useRef, useEffect } from 'react';
import { Mic, Upload, Trash2, Play, Pause } from 'lucide-react';
import { audioAPI } from '@/lib/api';

interface AudioRecording {
  id: number;
  filename: string;
  file_size: number;
  audio_url: string;
  transcribed_text: string;
  duration: number;
  chunks_count: number;
  created_at: string;
}

export default function AudioPage() {
  const [recordings, setRecordings] = useState<AudioRecording[]>([]);
  const [loading, setLoading] = useState(false);
  const [uploading, setUploading] = useState(false);
  const [recording, setRecording] = useState(false);
  const [playingId, setPlayingId] = useState<number | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const audioRef = useRef<HTMLAudioElement>(null);

  useEffect(() => {
    fetchRecordings();
  }, []);

  const fetchRecordings = async () => {
    setLoading(true);
    try {
      const response = await audioAPI.list();
      setRecordings(response.data);
    } catch (error) {
      console.error('Failed to fetch recordings:', error);
    } finally {
      setLoading(false);
    }
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        const file = new File([audioBlob], `recording-${Date.now()}.webm`, { type: 'audio/webm' });
        await uploadAudio(file);
        stream.getTracks().forEach(track => track.stop());
      };

      mediaRecorder.start();
      setRecording(true);
    } catch (error) {
      console.error('Failed to start recording:', error);
      alert('Microphone access denied');
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && recording) {
      mediaRecorderRef.current.stop();
      setRecording(false);
    }
  };

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      uploadAudio(file);
    }
  };

  const uploadAudio = async (file: File) => {
    if (file.size > 50 * 1024 * 1024) {
      alert('File too large. Max size: 50MB');
      return;
    }

    setUploading(true);
    try {
      await audioAPI.upload(file);
      await fetchRecordings();
      alert('Audio processed successfully!');
    } catch (error: any) {
      console.error('Upload failed:', error);
      alert(error.response?.data?.detail || 'Upload failed');
    } finally {
      setUploading(false);
    }
  };

  const deleteRecording = async (id: number) => {
    if (!confirm('Delete this recording?')) return;
    try {
      await audioAPI.delete(id);
      setRecordings(recordings.filter(r => r.id !== id));
    } catch (error) {
      console.error('Delete failed:', error);
    }
  };

  const togglePlay = (id: number, url: string) => {
    if (playingId === id) {
      audioRef.current?.pause();
      setPlayingId(null);
    } else {
      if (audioRef.current) {
        audioRef.current.src = url;
        audioRef.current.play();
        setPlayingId(id);
      }
    }
  };

  const formatFileSize = (bytes: number) => {
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
  };

  const formatDuration = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">Audio Recordings</h1>
        <p className="text-slate-600 mt-1">Record or upload audio to transcribe and store</p>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex gap-4">
          <button
            onClick={recording ? stopRecording : startRecording}
            disabled={uploading}
            className={`flex items-center gap-2 px-6 py-3 rounded-lg font-medium transition ${
              recording
                ? 'bg-red-600 hover:bg-red-700 text-white'
                : 'bg-blue-600 hover:bg-blue-700 text-white'
            } disabled:opacity-50`}
          >
            <Mic className="w-5 h-5" />
            {recording ? 'Stop Recording' : 'Start Recording'}
          </button>

          <button
            onClick={() => fileInputRef.current?.click()}
            disabled={uploading || recording}
            className="flex items-center gap-2 px-6 py-3 bg-slate-600 hover:bg-slate-700 text-white rounded-lg font-medium transition disabled:opacity-50"
          >
            <Upload className="w-5 h-5" />
            Upload Audio
          </button>
          <input
            ref={fileInputRef}
            type="file"
            accept="audio/*"
            onChange={handleFileUpload}
            className="hidden"
          />
        </div>
        {uploading && <p className="mt-4 text-blue-600">Processing audio...</p>}
      </div>

      {loading ? (
        <div className="text-center py-12">Loading...</div>
      ) : (
        <div className="space-y-4">
          {recordings.map((rec) => (
            <div key={rec.id} className="bg-white rounded-lg shadow p-6">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <h3 className="font-semibold text-lg text-slate-900">{rec.filename}</h3>
                  <p className="text-sm text-slate-500 mt-1">
                    {formatFileSize(rec.file_size)} • {formatDuration(rec.duration)} • {rec.chunks_count} chunks
                  </p>
                  <p className="text-slate-700 mt-3 whitespace-pre-wrap">{rec.transcribed_text}</p>
                </div>
                <div className="flex gap-2 ml-4">
                  <button
                    onClick={() => togglePlay(rec.id, rec.audio_url)}
                    className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition"
                  >
                    {playingId === rec.id ? <Pause className="w-5 h-5" /> : <Play className="w-5 h-5" />}
                  </button>
                  <button
                    onClick={() => deleteRecording(rec.id)}
                    className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition"
                  >
                    <Trash2 className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      <audio ref={audioRef} onEnded={() => setPlayingId(null)} className="hidden" />
    </div>
  );
}
