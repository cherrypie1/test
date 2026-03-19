<img width="750" height="444" alt="Снимок экрана 2026-03-19 в 15 45 13" src="https://github.com/user-attachments/assets/06416bd1-fe17-452a-97c3-f41792ef0a53" />## Pipeline

API → Python Loader → RAW_TABLE → Materialized View → PARSED_TABLE → dbt model

## Run project

1 Запустить Docker

docker compose up -d

2 Создать таблицы

clickhouse-client < sql/raw_table.sql
clickhouse-client < sql/parsed_table.sql
clickhouse-client < sql/mv_people.sql

3 Установить зависимости

pip install -r requirements.txt

4 Загрузка данных

python app/loader.py

5 DBT

dbt run

##RESULTS
<img width="750" height="444" alt="Снимок экрана 2026-03-19 в 15 45 13" src="https://github.com/user-attachments/assets/a56b6b72-53b1-4d74-b12c-b0e43ba3075d" />
<img width="792" height="353" alt="Снимок экрана 2026-03-19 в 15 46 05" src="https://github.com/user-attachments/assets/94697c69-e15d-4735-8776-9e8370efd6d0" />

