-- search bands by glam rock

SELECT band_name, IFNULL(split, YEAR(CURRENT_DATE())) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'