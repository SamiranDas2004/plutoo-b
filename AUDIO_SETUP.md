# Audio Recording Feature Setup

## Overview
Users can record or upload audio files. The system transcribes them using OpenAI Whisper, stores audio in Cloudinary, saves metadata in MySQL, and creates embeddings in Pinecone.

## Backend Setup

### 1. Install Dependencies
```bash
cd pluto.chat
pip install openai cloudinary
```

### 2. Create Database Table
Run the SQL script:
```bash
mysql -u root -p plutochat < create_audio_table.sql
```

Or manually execute:
```sql
CREATE TABLE IF NOT EXISTS audio_recordings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    filename VARCHAR(255) NOT NULL,
    file_size INT NOT NULL,
    file_type VARCHAR(100) NOT NULL,
    audio_url VARCHAR(500) NOT NULL,
    transcribed_text TEXT NOT NULL,
    duration INT DEFAULT 0,
    chunks_count INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id)
);
```

### 3. Configure Environment Variables
Add to `pluto.chat/.env`:
```env
# OpenAI for Whisper transcription
OPENAI_API_KEY=sk-...

# Cloudinary for audio storage
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Get API Keys

**OpenAI (Whisper):**
- Sign up at https://platform.openai.com/
- Create API key at https://platform.openai.com/api-keys
- Free tier: $5 credit for new accounts
- Pricing: ~$0.006 per minute of audio

**Cloudinary (Audio Storage):**
- Sign up at https://cloudinary.com/
- Free tier: 25GB storage, 25GB bandwidth/month
- Get credentials from Dashboard > Settings > Access Keys

## Frontend Setup

No additional setup needed. The audio page is already integrated at `/dashboard/audio`.

## Features

### Recording
- Click "Start Recording" to record audio from microphone
- Click "Stop Recording" to finish and auto-upload
- Browser will request microphone permission

### Upload
- Click "Upload Audio" to select audio file
- Supports: MP3, WAV, M4A, WebM
- Max size: 50MB

### Processing Flow
1. Audio uploaded to backend
2. Whisper transcribes audio to text
3. Audio file stored in Cloudinary
4. Text chunked (500 chars, 100 overlap)
5. Embeddings created and stored in Pinecone
6. Metadata saved in MySQL

### Playback
- Click play button to listen to recordings
- View transcribed text
- See file size, duration, and chunk count

## API Endpoints

- `POST /audio` - Upload audio file
- `GET /audio` - List all recordings
- `DELETE /audio/{id}` - Delete recording

## Testing

1. Start backend: `cd pluto.chat && uvicorn main:app --reload`
2. Start frontend: `cd plutodashbord && npm run dev`
3. Navigate to http://localhost:3000/dashboard/audio
4. Test recording or upload an audio file

## Troubleshooting

**"Microphone access denied"**
- Grant browser permission for microphone
- Check browser settings

**"Upload failed"**
- Verify OPENAI_API_KEY is set
- Check Cloudinary credentials
- Ensure file is under 50MB

**"Transcription failed"**
- Verify audio file is valid format
- Check OpenAI API quota/credits
