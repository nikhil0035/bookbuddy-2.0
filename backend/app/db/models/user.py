import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    is_premium = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    books = relationship("Book", back_populates="user", cascade="all, delete")
    reading_progress = relationship("ReadingProgress", back_populates="user", cascade="all, delete")
    highlights = relationship("Highlight", back_populates="user", cascade="all, delete")
    notes = relationship("Note", back_populates="user", cascade="all, delete")
    vocabulary_logs = relationship("VocabularyLog", back_populates="user", cascade="all, delete")
    ai_interactions = relationship("AIInteraction", back_populates="user", cascade="all, delete")
    reading_streak = relationship("ReadingStreak", back_populates="user", uselist=False, cascade="all, delete")
    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete")