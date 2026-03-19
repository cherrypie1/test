## Pipeline

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