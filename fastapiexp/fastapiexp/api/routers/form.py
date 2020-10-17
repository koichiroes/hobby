from fastapi import APIRouter, Depends, Form, Response
from pydantic import BaseModel

from fastapiexp.application.session import SessionApplication
from fastapiexp.infrastructure.di_container import di_container

COOKIE_MAX_AGE = 60 * 60
COOKIE_KEY = "session_id"

router = APIRouter()
application: SessionApplication = SessionApplication(di_container)


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
) -> Response:
    session_id = application.store_session(COOKIE_MAX_AGE)
    response = Response(status_code=204)
    response.set_cookie(
        key=COOKIE_KEY,
        value=session_id,
        max_age=COOKIE_MAX_AGE,
        path="/predict",
        secure=True,
        httponly=True,
    )
    return response
