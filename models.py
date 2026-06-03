from datetime import datetime, timezone
from sqlalchemy import String, Float, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class SearchHistory(Base):
    __tablename__ = "search_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    city: Mapped[String] = mapped_column(String(100), nullable=False, index=True)
    country: Mapped[String | None] = mapped_column(String(100), nullable=True)
    temperature_c: Mapped[float] = mapped_column(Float, nullable=False)
    windspeed_kmh: Mapped[float] =  mapped_column(Float, nullable=False)
    weather_code: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(50), nullable=False)
    searched_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
