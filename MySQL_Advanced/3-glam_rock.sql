-- search bands by glam rock

SELECT band_name, IFNULL(split, 2024)) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';