import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base
from sqlalchemy.orm import relationship

class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id", ondelete="CASCADE"), nullable=False)

    chapter_number = Column(Integer)
    title = Column(String(500))
    start_page = Column(Integer)
    end_page = Column(Integer)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    book = relationship("Book", back_populates="chapters")