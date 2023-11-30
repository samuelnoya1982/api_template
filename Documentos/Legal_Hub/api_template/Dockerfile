FROM python:3.9-slim

WORKDIR /project

COPY . .

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD ["apprun:app", "-t 0", "-w 2", "-b 0.0.0.0:5000"]