FROM python:3.6-alpine3.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m spacy link en_core_web_sm en -f
COPY . .
CMD [ "python", "./slack_handler.py" ]