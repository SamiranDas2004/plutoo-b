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
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at)
);
