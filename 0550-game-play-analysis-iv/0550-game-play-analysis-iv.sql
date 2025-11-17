WITH FirstLogin AS (
  SELECT
    player_id,
    MIN(event_date) AS first_day
  FROM Activity
  GROUP BY player_id
),
SecondDayLogin AS (
  SELECT
    f.player_id
  FROM FirstLogin f
  JOIN Activity a
    ON f.player_id = a.player_id
    AND a.event_date = DATE_ADD(f.first_day, INTERVAL 1 DAY)
)
SELECT
  ROUND(
    COUNT(DISTINCT s.player_id) * 1.0
    / COUNT(DISTINCT f.player_id),
    2
  ) AS fraction
FROM FirstLogin f
LEFT JOIN SecondDayLogin s
  ON f.player_id = s.player_id;
