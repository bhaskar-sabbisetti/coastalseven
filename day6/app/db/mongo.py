from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_DB_NAME]
        print("✅ MongoDB connected!")

    def disconnect(self):
        if self.client:
            self.client.close()
            print("🛑 MongoDB disconnected.")

db = MongoDB()

async def get_mongo_db():
    """Dependency to get MongoDB database instance."""
    return db.db
