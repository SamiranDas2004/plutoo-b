-- Add full_name and company_name fields to users table
ALTER TABLE users 
ADD COLUMN full_name VARCHAR(255) NULL AFTER id,
ADD COLUMN company_name VARCHAR(255) NULL AFTER email;
