# create_tables.py (run from project root)
from app.db.database import engine, Base
from app.db import models  # ensure models are imported

Base.metadata.create_all(bind=engine)
print("Tables created")
