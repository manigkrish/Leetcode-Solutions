WITH ProductFirstYear AS (
  SELECT 
    product_id, 
    MIN(year) AS first_year
  FROM Sales
  GROUP BY product_id
)
SELECT
  s.product_id,
  pf.first_year,
  s.quantity,
  s.price
FROM Sales s
JOIN ProductFirstYear pf
  ON s.product_id = pf.product_id
  AND s.year = pf.first_year;
