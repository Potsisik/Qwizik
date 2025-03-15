#from .main import app
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path

from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Страница"], summary=["Получить главную страницу"]) #получаем главную страницу - перенести в другой файл
def get_html():
    html_content = Path('quizes.html').read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/create", tags=["Страница"], summary=["Получить страницу создания"]) #получаем cтраницу создания
def get_html():
    html_content = Path('create_quiz.html').read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/quizes.html/{quiz_id}", tags=["Страница"], summary=["Получить страницу одного опроса"]) #получаем страницу где есть только 1 опрос
def get_html(quiz_id):
    html_content = Path('one_quiz.html').read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/edit/{quiz_id}", tags=["Страница"], summary=["Редактировать опрос"]) #получаем страницу где можно редактировать опрос
def get_html(quiz_id):
    html_content = Path('edit.html').read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)

@router.get("/login", tags=["Челики"], summary=["Страничка авторизации"]) 
def get_html():
    html_content = Path('login.html').read_text(encoding="utf-8")
    return HTMLResponse(content=html_content, status_code=200)