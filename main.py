from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from front import router
from base import DB, Quiz, Vote, User, User_DB

app = FastAPI()
app.include_router(router)
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
        

My_DB = DB('quizes.json') #создали базу данных, где подгружены все данные из файла
All_users = User_DB('admins.json')

@app.get("/quizes", tags=["Опросы"], summary=["Получить все опросы"]) #получаем все данные с сервера
def read_quizes():
    return My_DB.li_quiz

@app.get("/quizes/{quiz_id}", tags=["Опросы"], summary=["Получить конкретный опрос"]) #достаем конкретный опрос из файла 
def get_quiz(quiz_id: int):
    return My_DB.get_quiz_by_id(quiz_id)

@app.post("/quizes", tags=["Опросы"], summary=["Создать опрос"])
def create_quiz(new_quiz: Quiz):
    return My_DB.append_quiz(new_quiz)

@app.put("/edit/{edit_id}", tags=["Опросы"], summary=["Редактировать опрос"])
def edit(new_quiz: Quiz, edit_id: int):
    return My_DB.edit_quiz(new_quiz, edit_id)

@app.delete("/delete/{del_id}", tags=["Опросы"], summary=["Удалить опрос"]) #функция Тимура
def delete_quiz(del_id: int):
    return My_DB.delete_quiz(del_id)


@app.post("/plus/{vote_id}", tags=["Опросы"], summary=["Добавить балл"]) #функция Артура
def vote_quiz(vote_id: int, vote_answer: Vote):
    return My_DB.vote_quiz(vote_id, vote_answer.answer)

@app.post("/login", tags=["Челики"], summary=["Войти как админ"])
def login(user: User):
    return All_users.login(user)