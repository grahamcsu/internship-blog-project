-- Seed Authors
INSERT INTO Author (Id, FirstName, LastName) VALUES
(1, 'George', 'Orwell'),
(2, 'Jane', 'Austen'),
(3, 'Mark', 'Twain'),
(4, 'Mary', 'Shelley'),
(5, 'James', 'Baldwin');

-- Seed Articles
INSERT INTO Article (Id, Title, Content, AuthorId) VALUES
(1, 'Politics and Language', 'An article about the relationship between language and political thought.', 1),
(2, 'Life in the Countryside', 'A short reflection on manners, class, and rural society.', 2),
(3, 'The River Journey', 'A story about travel, humor, and life along the river.', 3),
(4, 'The Modern Monster', 'An essay about science, ambition, and unintended consequences.', 4),
(5, 'Identity and Society', 'A thoughtful piece about identity, justice, and American culture.', 5),
(6, 'Fiction and Truth', 'An article about how fiction can reveal uncomfortable truths.', 1),
(7, 'Satire as Criticism', 'A short article on using humor to expose hypocrisy.', 3),
(8, 'The Shape of Fear', 'An article exploring fear in gothic literature.', 4);

INSERT INTO Tag (Id, Name) VALUES
(1, 'Politics'),
(2, 'Literature'),
(3, 'Satire'),
(4, 'Society'),
(5, 'Science'),
(6, 'Gothic'),
(7, 'Travel');

INSERT INTO ArticleTag (ArticleId, TagId) VALUES
(1, 1), -- Politics and Language -> Politics
(1, 4), -- Politics and Language -> Society

(2, 2), -- Life in the Countryside -> Literature
(2, 4), -- Life in the Countryside -> Society

(3, 3), -- The River Journey -> Satire
(3, 7), -- The River Journey -> Travel

(4, 5), -- The Modern Monster -> Science
(4, 6), -- The Modern Monster -> Gothic

(5, 4), -- Identity and Society -> Society
(5, 1), -- Identity and Society -> Politics

(6, 2), -- Fiction and Truth -> Literature
(6, 4), -- Fiction and Truth -> Society

(7, 3), -- Satire as Criticism -> Satire
(7, 1), -- Satire as Criticism -> Politics

(8, 6), -- The Shape of Fear -> Gothic
(8, 2); -- The Shape of Fear -> Literature