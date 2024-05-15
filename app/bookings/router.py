from fastapi import APIRouter, Depends
from bookings.dao import BookingDAO
from bookings.schemas import SBooking
from users.dependencies import get_current_user


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)

# response_model=list[SBooking]
@router.get("")
async def get_bookings(user=Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)


@router.get("/{id}", response_model=SBooking)
async def get_booking_info(id: int):
    return await BookingDAO.find_by_id(id)

@router.get("/filters")
async def get_booking_info_by_cost(filters):
    return await BookingDAO.find_one_or_none()