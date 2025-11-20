@ECHO OFF
git clone https://github.com/assafelovic/gpt-researcher.git
COPY .env gpt-researcher\
DEL gpt-researcher\requirements.txt
COPY requirements.txt gpt-researcher\
