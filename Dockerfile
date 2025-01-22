FROM python


RUN apt-get update
RUN pip install flask 
RUN pip install flask_session
RUN pip install mysql-connector-python

WORKDIR /app

EXPOSE 5000

CMD [ "python","web.py" ]