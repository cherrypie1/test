
  
    
    
    
        
         


        insert into `default`.`craft_summary`
        ("craft", "people_count")SELECT
    craft,
    count(*) as people_count
FROM people
GROUP BY craft
  