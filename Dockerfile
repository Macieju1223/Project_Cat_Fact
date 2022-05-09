FROM python:3.8.10

COPY . .
RUN pip install -r requirments.txt
CMD python3 main.py
EXPOSE 8080
