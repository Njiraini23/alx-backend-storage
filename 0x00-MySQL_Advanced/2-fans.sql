-- sql script  that ranks country origins of bands ordered 
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nrb_fans DESC;
