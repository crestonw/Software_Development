FROM python:latest
MAINTAINER Creston Wilson "crestonw@uoregon.edu"
COPY . /flask_vocab
WORKDIR /flask_vocab
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["flask_vocab.py"]
