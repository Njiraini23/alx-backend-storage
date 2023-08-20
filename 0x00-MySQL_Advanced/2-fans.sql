-- sql script  that ranks country origins of bands ordered
-- by number of unique fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nrb_fans DESC;
