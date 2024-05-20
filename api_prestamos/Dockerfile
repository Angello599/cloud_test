FROM python:3-slim
WORKDIR /programas/api-prestamos
RUN pip3 install fastapi
RUN pip3 install pydantic
RUN pip3 install mysql-connector-python
COPY . .
CMD ["fastapi", "run", "./prestamos_main.py", "--port", "8002"]
