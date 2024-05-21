-- import in hbtn_0c_0 db this table dum`p
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM temperatures
GROUP BY `city`
ORDER BY `avg_temp` DESC;
