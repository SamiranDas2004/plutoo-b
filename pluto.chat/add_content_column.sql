-- Add content column to documents table
ALTER TABLE documents 
ADD COLUMN content TEXT NULL AFTER file_type;
