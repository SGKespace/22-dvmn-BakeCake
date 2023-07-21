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


# [Статья на Хабре](https://habr.com/ru/articles/711278/)


![img_1.png](img_1.png)

![img_3.png](img_3.png)

Выбираем docker image 
Breadcrumbs22-dvmn-BakeCake/.github/workflows / docker-image.yml     in master
Исправляем строчку  runs-on: self-hosted


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
    - name: Build the Docker image
      run: docker build . --file Dockerfile --tag my-image-name:$(date +%s)



в соседней консоли от рута  пишем

sudo apt-get update
sudo apt-get install ca-certificates curl gnupg

и далее ппо шагам https://docs.docker.com/engine/install/debian/


usermod -a -G docker curator

