-- Add company_name column to users table
ALTER TABLE users ADD COLUMN company_name VARCHAR(255);

-- Optional: Add index for faster queries
CREATE INDEX idx_users_company_name ON users(company_name);

-- Optional: Update existing users with a default value
-- UPDATE users SET company_name = 'Unknown' WHERE company_name IS NULL;
