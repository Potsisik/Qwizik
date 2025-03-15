from pydantic.type_adapter import TypeAdapter
from typing import List
import json
from typing import Optional
from pydantic.json import pydantic_encoder
from pydantic import BaseModel
from fastapi import HTTPException

class Vote(BaseModel): #костыли
    answer: str

class Quiz(BaseModel): #класс опроса
    id: Optional[int] = None
    title: str
    answers: list 
    multiplayer_choise: bool # не успели реализовать эти параметры
    have_right_answer: bool
    #добавить правильный ответ в режиме викторины

    #конструктор я не пишу потому что он наследуется от BaseModel
    # типо q1 = Q1(title = "first quiz", answers = ["one"], ...)

class DB: #класс базы данных
    li_quiz: List[Quiz]
    def __init__(self, filename):
        #python_data = json.loads(filename)
        with open(filename, 'r', encoding='utf-8') as j:
            python_data = json.loads(j.read())
        adapter = TypeAdapter(List[Quiz])
        quizes = adapter.validate_python(python_data)
        self.li_quiz =  quizes

    def get_quiz_by_id(self, quiz_id):
        quizes = self.li_quiz
        for quiz in quizes:
            if quiz.id == quiz_id:
                return quiz
        raise HTTPException(status_code=404)
    
    def get_max_id(self):
        i = 0
        for quiz in self.li_quiz:
            if quiz.id > i:
                i = quiz.id
        return i

    def append_quiz(self, quiz: Quiz):
        quiz.id = self.get_max_id() + 1
        quiz.answers = str_to_dict(quiz.answers)
        self.li_quiz.append(quiz)
        with open("quizes.json", 'w', encoding='utf-8',) as f:
            json.dump(self.li_quiz, f, default=pydantic_encoder, ensure_ascii=False)
        return quiz.id
    
    def edit_quiz(self, new_quiz: Quiz, edit_id):
        quizes = self.li_quiz
        for quiz in quizes:
            if quiz.id == edit_id:
                quiz.title = new_quiz.title
                quiz.answers = str_to_dict(new_quiz.answers) #переделать на нормально позже
                quiz.multiplayer_choise = new_quiz.multiplayer_choise
                quiz.have_right_answer = new_quiz.have_right_answer
        with open("quizes.json", 'w', encoding='utf-8',) as f:
            json.dump(self.li_quiz, f, default=pydantic_encoder, ensure_ascii=False)
        return edit_id
    
    def vote_quiz(self, vote_id: int, vote_answer: str): #функция Артура
        quizes = self.li_quiz
        for quiz in quizes:
            if quiz.id == vote_id:
                for answer in quiz.answers:
                    key = list(answer.keys())[0]
                    if key == vote_answer:
                        answer[key] += 1
                        with open("quizes.json", 'w', encoding='utf-8',) as f:
                            json.dump(self.li_quiz, f, default=pydantic_encoder, ensure_ascii=False)
                        return quiz.answers
        raise HTTPException(status_code=404)
    
    def delete_quiz(self, del_id): #функция Тимура
        quizes = self.li_quiz
        initial_length = len(quizes)
        for i in range(initial_length):  # Проходим по списку с индексами
            if quizes[i].id == del_id:
                index_to_remove = i
                quizes.pop(index_to_remove)
                break
        with open("quizes.json", 'w', encoding='utf-8',) as f:
            json.dump(self.li_quiz, f, default=pydantic_encoder, ensure_ascii=False)
        return("ok")
    
def str_to_dict(old_list: list): #функция делает из списка со строками список словарей
    new_list = []
    for el in old_list:
        new_list.append({el: 0})
    return new_list

class User(BaseModel):
    name: str
    password: str

class User_DB(BaseModel):
    li_user: List[User]
    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as j:
            python_data = json.loads(j.read())
        adapter = TypeAdapter(List[User])
        users = adapter.validate_python(python_data)
        self.li_user =  users
    
    def login(self, user: User):
        pass