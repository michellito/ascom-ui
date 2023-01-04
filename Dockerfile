FROM python:3.9

# install requirements
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY entry.sh /bin
COPY . /app

EXPOSE 8501

ENTRYPOINT ["bash", "/bin/entry.sh"]