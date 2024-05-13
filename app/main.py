from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel
from bookings.router import router as bookings_router


app = FastAPI()


app.include_router(bookings_router)


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: int | None = Query(None, ge=1, le=5),
        has_spa: bool | None = False,
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_spa = has_spa


@app.get("/hotels/")
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings/")
def add_booking(booking: SBooking):
    pass

