FROM python:3-slim
WORKDIR /programas/api-usuarios
RUN pip3 install fastapi
RUN pip3 install pydantic
RUN pip3 install mysql-connector-python
COPY . .
CMD ["fastapi", "run", "./usuarios_main.py", "--port", "8001"]