DROP TABLE recommendationsBasedOnStarringField;

ALTER TABLE movies
ADD lexemesStarring tsvector;

UPDATE movies
SET lexemesStarring = to_tsvector(Starring);

UPDATE movies
SET rank = ts_rank(lexemesStarring,plainto_tsquery(
(
SELECT Starring FROM movies WHERE url='inception'
)
));

CREATE TABLE recommendationsBasedOnStarringField AS 
SELECT url, rank FROM movies ORDER BY rank DESC LIMIT 50;

\copy (SELECT * FROM recommendationsBasedOnStarringField) to '/home/pi/RSL/top50starring.csv' WITH csv;
