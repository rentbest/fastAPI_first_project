from fastapi import APIRouter
from bookings.dao import BookingDAO
from bookings.schemas import SBooking


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("", response_model=list[SBooking])
async def get_bookings():
    return await BookingDAO.find_all()


@router.get("/{id}", response_model=SBooking)
async def get_booking_info(id: int):
    return await BookingDAO.find_by_id(id)

@router.get("/filters")
async def get_booking_info_by_cost(filters):
    return await BookingDAO.find_one_or_none()