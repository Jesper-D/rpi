DROP TABLE recommendationsBasedOnTitleField;

ALTER TABLE movies
ADD lexemesTitle tsvector;

UPDATE movies
SET lexemesTitle = to_tsvector(Title);

UPDATE movies
SET rank = ts_rank(lexemesTitle,plainto_tsquery(
(
SELECT Title FROM movies WHERE url='inception'
)
));

CREATE TABLE recommendationsBasedOnTitleField AS 
SELECT url, rank FROM movies ORDER BY rank DESC LIMIT 50;

\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/top50title.csv' WITH csv;
