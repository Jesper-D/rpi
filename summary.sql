DROP TABLE recommendationsBasedOnSummaryField;

UPDATE movies
SET rank = ts_rank(lexemesSummary,plainto_tsquery(
(
SELECT Summary FROM movies WHERE url='inception'
)
));

CREATE TABLE recommendationsBasedOnSummaryField AS 
SELECT url, rank FROM movies WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;

\copy (SELECT * FROM recommendationsBasedOnSummaryField) to '/home/pi/RSL/top50summary.csv' WITH csv;
