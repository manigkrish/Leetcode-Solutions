WITH Dates AS (
  SELECT DISTINCT visited_on
  FROM Customer
  WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
    FROM Customer
  )
)
SELECT
  d.visited_on,
  SUM(c.amount) AS amount,
  ROUND(SUM(c.amount) / 7, 2) AS average_amount
FROM Dates d
LEFT JOIN Customer c
  ON DATEDIFF(d.visited_on, c.visited_on) BETWEEN 0 AND 6
GROUP BY d.visited_on
ORDER BY d.visited_on;