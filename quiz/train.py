import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pydantic.type_adapter import TypeAdapter
from typing import List

from pydantic.json import pydantic_encoder

app = FastAPI() 

Quizes = [{ #этот список должен потом удалиться, чтобы его отличать пишу с большой буквы название
    "id": 1,
    "title": "Любимое животное",
    "answers": ["Кошка", "Собака", "Птеродактиль"],
    "multiplayer_choise": True,
    "have_right_answer": False
},
{
    "id": 2,
    "title": "Любишь прогу?",
    "answers": ["Да", "Нет"],
    "multiplayer_choise": False,
    "have_right_answer": False
}]

class DB(BaseModel): #класс опроса
    li_quiz: list
    def load_from_file(filename):
         python_data = json.loads(filename)
         adapter = TypeAdapter(List[DB])
         quizes = adapter.validate_python(python_data)
         print (quizes)
         for quiz in quizes:
              print (quiz)
    def load_to_file(filename):
         pass


json_data = '''
[
    {"li_quiz": ["хуй", "еще хуй"]},
    {"li_quiz": ["два хуя"]},
    {"li_quiz": ["хуй"]}
]
'''
quizes = [DB(li_quiz=['хуй', 'еще хуй']), DB(li_quiz=['два хуя']), DB(li_quiz=['хуй'])]
#DB.load_from_file(json_data)
bigger_data = json.dumps(quizes, default=pydantic_encoder, ensure_ascii=False)
print(bigger_data)


@app.get("/quizes", tags=["Пример"], summary=["Получить все опросы"]) #получаем данные с сервера - больше как пример
def read_quizes():
    return Quizes
    #return HTMLResponse(content=text)


#with open("quizes.json", 'w', encoding='utf-8',) as f: #пишем список в файл - тоже пример
#    json.dump(Quizes, f, ensure_ascii=False)
#
#with open('quizes.json', 'r', encoding='utf-8',) as f: #получаем данные с файла - пример
#        data = json.load(f)
#
#print(data)

@app.get("/quizes", tags=["Опросы"], summary=["Получить все опросы"]) #получаем все данные с сервера
def read_quizes():
    with open('quizes.json', 'r', encoding='utf-8',) as f:
        quizes = json.load(f)
    return quizes

@app.get("/quizes/{quiz_id}", tags=["Опросы"], summary=["Получить конкретный опрос"]) #достаем конкретный опрос из файла 
def get_quiz(quiz_id: int):
    with open('quizes.json', 'r', encoding='utf-8',) as f:
        quizes = json.load(f)
    for quiz in quizes:
        if quiz["id"] == quiz_id:
            return quiz
    raise HTTPException(status_code=404)


@app.post("/quizes", tags=["Опросы"], summary=["Создать опрос"])
def create_quiz(new_quiz: Quiz):
    with open('quizes.json', 'r', encoding='utf-8',) as f:
        quizes = json.load(f)
    quizes.append(
        {
            "id": len(quizes) + 1,
            "title": new_quiz.title,
            "answers": str_to_dict(new_quiz.answers),
            "multiplayer_choise": new_quiz.multiplayer_choise,
            "have_right_answer": new_quiz.have_right_answer
            #можно добавить что-то еще
        }
    )
    with open("quizes.json", 'w', encoding='utf-8',) as f:
        json.dump(quizes, f, ensure_ascii=False)
    return len(quizes) #возвращаю id

@app.put("/edit/{edit_id}", tags=["Опросы"], summary=["Редактировать опрос"])
def edit(new_quiz: Quiz, edit_id: int):
    with open('quizes.json', 'r', encoding='utf-8',) as f:
        quizes = json.load(f)
    edit_quiz = {
            "id": edit_id,
            "title": new_quiz.title,
            "answers": str_to_dict(new_quiz.answers),
            "multiplayer_choise": new_quiz.multiplayer_choise,
            "have_right_answer": new_quiz.have_right_answer
            #можно добавить что-то еще
        }
    for i, quiz in enumerate(quizes):
        if quiz["id"] == edit_id:
            quizes[i] = edit_quiz #переделать так, чтобы не стиралось число голосов
    
    with open("quizes.json", 'w', encoding='utf-8',) as f:
        json.dump(quizes, f, ensure_ascii=False)
    return edit_id #возвращаю id

@app.post("/plus", tags=["Опросы"], summary=["Добавить балл"]) #функция Артура
def vote_quiz(vote_id: int, vote_answer: str):
    with open('quizes.json', 'r', encoding='utf-8', ) as f:
        quizes = json.load(f)
    for i in range(len(quizes)):
        if quizes[i].id == vote_id:
            quizes[i].answer[vote_answer] += 1
            break
    with open("quizes.json", 'w', encoding='utf-8', ) as f:
        json.dump(quizes, f, ensure_ascii=False)
    return vote_id

@app.post("/delete/{del_id}", tags=["Опросы"], summary=["Удалить опрос"])
def delete_quiz(del_id: int):
    with open('quizes.json','r', encoding='utf-8',) as f:
        quizes = json.load(f)
    initial_length = len(quizes)
    for i in range(initial_length):  # Проходим по списку с индексами
            if quizes[i]['id'] == del_id:
                index_to_remove = i
                quizes.pop(index_to_remove)
                break
    with open("quizes.json", 'w', encoding='utf-8', ) as f:  # пишем список в файл - тоже пример
        json.dump(quizes, f, ensure_ascii=False)
    return "ок"