FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ban.py .
EXPOSE 5000
# Adicionamos o -u aqui embaixo:
CMD ["python", "-u", "ban.py"]