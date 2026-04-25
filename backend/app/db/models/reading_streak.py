import uuid
from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class ReadingStreak(Base):
    __tablename__ = "reading_streaks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)

    streak_count = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_read_date = Column(Date)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="reading_streak")