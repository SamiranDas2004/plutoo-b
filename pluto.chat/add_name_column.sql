-- Add name and company_name columns to users table
ALTER TABLE users ADD COLUMN name VARCHAR(255);
ALTER TABLE users ADD COLUMN company_name VARCHAR(255);

-- Optional: Add indexes for faster queries
CREATE INDEX idx_users_name ON users(name);
CREATE INDEX idx_users_company_name ON users(company_name);
