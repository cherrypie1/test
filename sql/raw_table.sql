CREATE TABLE raw_astros
(
    raw_json String,
    _inserted_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree
ORDER BY _inserted_at;