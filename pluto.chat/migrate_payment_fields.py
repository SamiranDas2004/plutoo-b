"""
Migration: Add payment and subscription fields to users table
Run this script to add user_type, payment_id, and order_id columns
"""
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Parse DATABASE_URL
db_url = os.getenv("DATABASE_URL")
# Format: mysql+pymysql://user:password@host:port/database
parts = db_url.replace("mysql+pymysql://", "").split("@")
user_pass = parts[0].split(":")
host_db = parts[1].split("/")
host_port = host_db[0].split(":")

DB_CONFIG = {
    'host': host_port[0],
    'port': int(host_port[1]) if len(host_port) > 1 else 3306,
    'user': user_pass[0],
    'password': user_pass[1],
    'database': host_db[1]
}

def run_migration():
    """Add payment fields to users table"""
    connection = None
    try:
        # Decode URL-encoded password
        import urllib.parse
        decoded_password = urllib.parse.unquote(DB_CONFIG['password'])
        
        config = DB_CONFIG.copy()
        config['password'] = decoded_password
        
        connection = pymysql.connect(**config)
        cursor = connection.cursor()
        
        print("Connected to database successfully!")
        
        # Check if columns already exist
        cursor.execute("""
            SELECT COLUMN_NAME 
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_SCHEMA = %s 
            AND TABLE_NAME = 'users' 
            AND COLUMN_NAME IN ('user_type', 'payment_id', 'order_id')
        """, (DB_CONFIG['database'],))
        
        existing_columns = [row[0] for row in cursor.fetchall()]
        
        # Add user_type column if not exists
        if 'user_type' not in existing_columns:
            print("Adding user_type column...")
            cursor.execute("""
                ALTER TABLE users 
                ADD COLUMN user_type VARCHAR(20) DEFAULT 'free'
            """)
            print("✓ user_type column added")
        else:
            print("✓ user_type column already exists")
        
        # Add payment_id column if not exists
        if 'payment_id' not in existing_columns:
            print("Adding payment_id column...")
            cursor.execute("""
                ALTER TABLE users 
                ADD COLUMN payment_id VARCHAR(255) NULL
            """)
            print("✓ payment_id column added")
        else:
            print("✓ payment_id column already exists")
        
        # Add order_id column if not exists
        if 'order_id' not in existing_columns:
            print("Adding order_id column...")
            cursor.execute("""
                ALTER TABLE users 
                ADD COLUMN order_id VARCHAR(255) NULL
            """)
            print("✓ order_id column added")
        else:
            print("✓ order_id column already exists")
        
        connection.commit()
        print("\n✅ Migration completed successfully!")
        
        # Show table structure
        cursor.execute("DESCRIBE users")
        print("\nUpdated users table structure:")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[1]}")
        
    except Exception as e:
        print(f"\n❌ Migration failed: {str(e)}")
        if connection:
            connection.rollback()
    finally:
        if connection:
            connection.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    print("=" * 60)
    print("Running Payment Fields Migration")
    print("=" * 60)
    run_migration()
