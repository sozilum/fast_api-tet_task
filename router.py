from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request


router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)
templates = Jinja2Templates(directory= 'templates')


@router.get('/')
async def get_chat_page(request: Request):
    return templates.TemplateResponse('chat.html', {'request':request})