CREATE TABLE people
(
    craft String,
    name String,
    _inserted_at DateTime
)
ENGINE = ReplacingMergeTree
ORDER BY (name, craft);