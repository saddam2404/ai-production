from app.database import engine

try:
    # Test the database connection
    with engine.connect() as connection:
        print("Database connection test passed.")
    
except Exception as e:
    print(f"Database connection test failed: {e}")