### Hexlet tests and linter status:
[![Actions Status](https://github.com/dima020/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dima020/python-project-49/actions)

Asciinema (github), это удобный опенсорсный инструмент для записи действий в терминале. Записи сохраняются в простом для чтения текстовом формате, поэтому весят совсем немного, а веб-плеер по сути воспроизводит текст из терминала вместо видео, так что любой кусок можно скопировать и использовать. Готовый материал можно загрузить в одно нажатие на asciinema.org или сначала отредактировать локально. Плеер можно встроить на сайт буквально в три строки, бонусом прилагаются всякие плюшки с оформлением и совместимостью, и вообще по совокупности всех фич (и отсутствия головной боли) asciinema давно перерос все аналоги. Вот только есть несостыковка: записи в проекте называют asciicasts, по аналогии со скринкастами — но возможности стримить сессию в реальном времени не было несколько лет, пока не вышел релиз 2.0, в котором с помощью нового формата файлов удалось реализовать на удивление стабильную и удобную раздачу на любой терминал в реал-тайме. О том, как это работает, о подводных камнях и перспективах — под катом.

```sh
asciinema play demo.cast
