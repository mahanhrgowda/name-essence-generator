FROM python:3.10-slim

WORKDIR /app

COPY render/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "render/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
