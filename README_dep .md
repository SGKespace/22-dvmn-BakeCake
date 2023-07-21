# ssh
Путь к файлу конфигурации .ssh/config
Добавить записи
```
Host bakecake
    HostName 81.163.27.248
    User root
    ForwardAgent yes
```

Заходим на сервак и создаем ппользователя
useradd curator -m -s /bin/bash 
пепреходим в корень
cd ~


# GitHub

[Про руннер](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)





Затем выбираем docker image 
Breadcrumbs22-dvmn-BakeCake/.github/workflows / docker-image.yml     in master
# Исправляем 


name: Docker Image CI

on:
  push:
    branches: [ "master" ]
  pull_request:
    branches: [ "master" ]

jobs:

  build:

    runs-on: self-hosted

    
    steps:
    - uses: actions/checkout@v3
    - name: build and run
       env:
          DEBUG: True
          SECRET_KEY: 12345
          ALLOWED_HOSTS: localhost
       run: docker compose up -d --build



в соседней консоли от рута  пишем

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

[и далее ппо шагам](https://docs.docker.com/engine/install/debian/) устанавливаем докер


usermod -a -G docker curator



# [В ппомощь статья на Хабре](https://habr.com/ru/articles/711278/)
