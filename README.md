### Hexlet tests and linter status:
[![Actions Status](https://github.com/dima020/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dima020/python-project-49/actions)

Asciinema (github), это удобный опенсорсный инструмент для записи действий в терминале. Записи сохраняются в простом для чтения текстовом формате, поэтому весят совсем немного, а веб-плеер по сути воспроизводит текст из терминала вместо видео, так что любой кусок можно скопировать и использовать. Готовый материал можно загрузить в одно нажатие на asciinema.org или сначала отредактировать локально. Плеер можно встроить на сайт буквально в три строки, бонусом прилагаются всякие плюшки с оформлением и совместимостью, и вообще по совокупности всех фич (и отсутствия головной боли) asciinema давно перерос все аналоги. Вот только есть несостыковка: записи в проекте называют asciicasts, по аналогии со скринкастами — но возможности стримить сессию в реальном времени не было несколько лет, пока не вышел релиз 2.0, в котором с помощью нового формата файлов удалось реализовать на удивление стабильную и удобную раздачу на любой терминал в реал-тайме. О том, как это работает, о подводных камнях и перспективах — под катом.

asciinema rec
asciinema play
asciinema upload gsd.cast


 git add .
dim@User:~/dev/python-project-49$ git commit -m "7 проект"
[main 4604c7d] 7 проект
 2 files changed, 129 insertions(+)
 create mode 100644 gsd.cast
dim@User:~/dev/python-project-49$ git push origin main


## Демонстрация
[![asciicast](https://asciinema.org/a/HPpUKSEpccQ6gLDkHLtgBFL5X.png)](https://asciinema.org/a/HPpUKSEpccQ6gLDkHLtgBFL5X)

```sh
asciinema play demo.cast


Игра: «Калькулятор»
Необходимо реализовать игру «Калькулятор». Суть игры в следующем: пользователю показывается случайное математическое выражение, например, 35 + 16, которое нужно вычислить и записать правильный ответ.

## Демонстрация
[![asciicast](https://asciinema.org/a/HPpUKSEpccQ6gLDkHLtgBFL5X.png)](https://asciinema.org/a/R34hpQ1Zsf1Pd2l1O7f74gdYM)

Игра «НОД»
Необходимо реализовать игру «Наибольший общий делитель (НОД)». Суть игры в следующем: пользователю показывается два случайных числа, например, 25 50. Пользователь должен вычислить и ввести наибольший общий делитель этих чисел.

## Демонстрация
[![asciicast](https://asciinema.org/a/HPpUKSEpccQ6gLDkHLtgBFL5X.png)](https://asciinema.org/a/FdVJvu3RGY7n8CeBh7SF9Rbj8)
