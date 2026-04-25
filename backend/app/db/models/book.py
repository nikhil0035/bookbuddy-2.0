import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    title = Column(String(500), nullable=False)
    author = Column(String(255))
    file_url = Column(String, nullable=False)
    file_hash = Column(String, nullable=False, index=True)
    total_pages = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="books")
    pages = relationship("BookPage", back_populates="book", cascade="all, delete")
    chapters = relationship("Chapter", back_populates="book", cascade="all, delete")
    reading_progress = relationship("ReadingProgress", back_populates="book", cascade="all, delete")
    highlights = relationship("Highlight", back_populates="book", cascade="all, delete")
    notes = relationship("Note", back_populates="book", cascade="all, delete")
    vocabulary_logs = relationship("VocabularyLog", back_populates="book", cascade="all, delete")
    ai_interactions = relationship("AIInteraction", back_populates="book", cascade="all, delete")