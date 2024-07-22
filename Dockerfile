#   base image
FROM python:3.11

#   working directory
WORKDIR /app

#   code
COPY . .

#   required libraries]
RUN pip install -r requirements.txt

#   run
CMD ["python", "app.py"]
