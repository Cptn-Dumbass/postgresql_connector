FROM python

WORKDIR /.

RUN pip install psycopg2

COPY . .

CMD [ "python", "connector.py" ]