(
  SELECT u.name AS results
  FROM MovieRating m
    JOIN Users u
      ON m.user_id = u.user_id
  GROUP BY u.user_id, u.name
  ORDER BY COUNT(*) DESC, u.name ASC
  LIMIT 1
)
UNION ALL
(
  SELECT mo.title AS results
  FROM MovieRating m
    JOIN Movies mo
      ON m.movie_id = mo.movie_id
  WHERE DATE_FORMAT(m.created_at, '%Y-%m') = '2020-02'
  GROUP BY mo.movie_id, mo.title
  ORDER BY AVG(m.rating) DESC, mo.title ASC
  LIMIT 1
);