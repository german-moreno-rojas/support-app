# backend/app/models/ticket.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String, default="open")
    priority = Column(String, default="medium")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_technician_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # relaciones
    client = relationship("User", back_populates="tickets", foreign_keys=[user_id])
    technician = relationship("User", back_populates="assigned_tickets", foreign_keys=[assigned_technician_id])
    messages = relationship("Message", back_populates="ticket", cascade="all, delete-orphan")