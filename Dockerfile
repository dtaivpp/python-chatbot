FROM python:3.6 as build
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN pip install pip==9.0.3
RUN python -m spacy link en_core_web_sm en -f
COPY . .
EXPOSE 5004
CMD . ./init.sh
