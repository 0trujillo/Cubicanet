FROM python:3.11-alpine

WORKDIR /app

# Instala build dependencies para compilar psycopg2 y otras librerías nativas
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
