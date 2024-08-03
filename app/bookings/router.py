from fastapi import APIRouter, Depends
from bookings.dao import BookingDAO
from bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users
from datetime import date
from exceptions import RoomCannotBeBooked


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("", response_model=list[SBooking])
async def get_bookings(user=Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
    user_id: int,
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
    ):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked
    