-- top band

SELECT orgin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY orgin
ORDER BY nb_fans DESC;