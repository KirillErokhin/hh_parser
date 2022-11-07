# Исследование вакансий HeadHunter.ru по запросу "data python"

Поиск вакансий и отклики на данный момент одна из самый сложных заданий для начинающих специалистов в области инженерии данных. Данное исследование должно помочь определить будущему специалисту узнать о рынке вакансий, в частности:
- количество вакансий по их типу/городу/грейду/опыту
- самые популярные вакансии
- проф. области компаний
- основные необходимые навыки (key skills)
- компенсации труда

## Основной стек:
- pandas
- numpy
- seaborn
- matplotlib

## Итог исследования 

Самые популярные вакансии:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/vacancies_count.jpg" title="Вакансии" alt="График" width="500" height="500"/>
</div>

В итоге самыми популярными будут:

- data scientist
- data engineer
- data analyst
- programmer
- analyst
- devops

Видно, что в сумме аналитики более востребованы, в отличии от инженеров данных и саентистов.

Топ-6 включает в себя и devops, хотя и идет с большим отрывом от популярных вакансий.

---

Количество вакансий по городам:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/vacancies_cities.jpg" title="Распределение по городам" alt="График" width="600" height="500"/>
</div>

Большинство вакансий в столице - Москва. В 4 раза меньше в Санкт-Петербурге.

И дальше идёт на убывание.

---

Самые популярные вакансии в городах:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/pies_types_cities.jpg" title="Вакансии в городах" alt="График" width="800" height="1000"/>
</div>

Как видно, в двух наиболее крупных городах лидерами по поиску разделяют четыре типа:

- data scientist
- data engineer
- data analyst
- programmer

Наиборлее популярные всё же data scientist'ы и инженеры данных.

В остальных городах, где вакансий значительно меньше вакансий - разброс по требованию выше. Статистика слишком мала (до 40 вакансий), чтобы делать конечные выводы. Тренд сейчас идет на увеличение количества вакансий в стране, после чего можно будет сделать конечные выводы.

---

Популярные по грейдам и опыту:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/grades_exp_count.jpg" title="По грейдам и опыту" alt="График" width="1000" height="500"/>
</div>

---

Популярные грейды в городах:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/grades_cities_count.jpg" title="Грейды в городах" alt="График" width="800" height="1000"/>
</div>

---

Количество отликов:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/responses_count.jpg" title="Отклики" alt="График" width="800" height="800"/>
</div>

---

Востребование навыки:

<div align="left">
  <img src="https://github.com/KirillErokhin/hh_parser/blob/main/img/ks_ru_en_count.jpg" title="Навыки" alt="График" width="1000" height="500"/>
</div>

---
