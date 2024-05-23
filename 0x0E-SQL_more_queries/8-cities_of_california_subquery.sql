-- lists all the cities of California found in db hbtn_0d_usa
-- states contain one record name=California, Result ASC no JOIN.
SELECT `id`, `name` FROM `cities`
 WHERE `state_id` IN
       (SELECT `id` FROM `states` WHERE `name` = "California")
 ORDER BY `id`;
