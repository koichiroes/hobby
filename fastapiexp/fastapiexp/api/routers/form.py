from typing import Optional

from fastapi import APIRouter, Cookie, Depends, Form, Response
from pydantic import BaseModel

COOKIE_MAX_AGE = 60 * 60
COOKIE_KEY = "session_id"

router = APIRouter()


class SendForm(BaseModel):
    name: str
    email: str
    company: str


async def create_send_form(
    name: str = Form("", description="user name"),
    email: str = Form("", description="user email"),
    company: str = Form("", description="company user belongs"),
):
    return SendForm(name=name, email=email, company=company)


@router.post("/send", status_code=204, tags=["send"])
async def send_personal_info(
    send_form: SendForm = Depends(create_send_form),
    session_id: Optional[str] = Cookie(None),
) -> Response:
    print(send_form, session_id)
    response = Response(status_code=204)
    response.set_cookie(
        key=COOKIE_KEY,
        value="1",
        max_age=COOKIE_MAX_AGE,
        path="/predict",
        secure=True,
        httponly=True,
    )
    return response
