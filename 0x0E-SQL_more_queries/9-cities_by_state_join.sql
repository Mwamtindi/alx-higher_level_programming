-- list all cities in the db hbtn_0d_usa
-- records display: cities.id - cities.name - states.name sorted ASC.

SELECT ci.id, ci.name, st.name
FROM cities AS ci
INNER JOIN states AS st ON ci.states_id = st.id
ORDER BY ci.id;

