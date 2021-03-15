FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "debug"]