CREATE MATERIALIZED VIEW mv_people
TO people
AS
SELECT
    JSONExtractString(person, 'craft') AS craft,
    JSONExtractString(person, 'name') AS name,
    _inserted_at
FROM raw_astros
ARRAY JOIN JSONExtractArrayRaw(raw_json, 'people') AS person;