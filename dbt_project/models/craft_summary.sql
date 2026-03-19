SELECT
    craft,
    count(*) as people_count
FROM people
GROUP BY craft