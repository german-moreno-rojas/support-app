# backend/app/models/user.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="client")

    # relaciones
    tickets = relationship("Ticket", back_populates="client", foreign_keys="Ticket.user_id")
    assigned_tickets = relationship("Ticket", back_populates="technician", foreign_keys="Ticket.assigned_technician_id")
    messages = relationship("Message", back_populates="author")