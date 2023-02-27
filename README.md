# ascom-ui

cd into /ascom-ui
then use the command: docker compose -f docker-compose.yml up --build

then command: docker build -t davidruddell/ascom-streamlit:latest .

now we run the streamlit app
use command: docker run --rm -e PYTHONUNBUFFERED=1 -p 8501:8501 davidruddell/ascom-streamlit:latest

to accesss streamlit app, on google go to localhost:8501