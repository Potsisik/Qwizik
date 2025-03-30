FROM python:3.8-alpine
RUN pip install fastapi[standard]
COPY . .
CMD ["fastapi", "run"]
