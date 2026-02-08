-- Add payment and subscription fields to users table
ALTER TABLE users 
ADD COLUMN user_type VARCHAR(20) DEFAULT 'free',
ADD COLUMN payment_id VARCHAR(255),
ADD COLUMN order_id VARCHAR(255);
