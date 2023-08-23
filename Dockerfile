FROM python:3.8-alpine

ARG run_env=development
ENV env $run_env
LABEL "channel" = "Popravka"


WORKDIR ./test_project/popravka

VOLUME /allure_ss_com
RUN apk update && apk upgrade && apk add bash
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .


CMD pytest -m "$env" -s -v tests

#Эту команду мы запускаем чтобы собрать наш контейнер
#docker build --build-arg env=development -t automation-tests .

#Эта команда нужна чтобы запустить наш созданый контейнер
#docker run automation-tests

#Эти 2 команды нам нужны чтобы скопировать данные из контейнера и чтобы сгенерировать из результата репорт
#docker cp $(docker ps -a -q | head -1):/usr/lessons/allureResults .
#allure serve allureResults/
#Две команды ниже, помогут вам в эксперементах, чтобы после них почистить свой компьютер
#docker rm $(docker ps -a -q)
#docker kill $(docker ps -q)