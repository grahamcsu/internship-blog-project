CREATE TABLE Author (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT
);

CREATE TABLE Article (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Content TEXT,
    AuthorId INT,
    FOREIGN KEY (AuthorId) REFERENCES Author(Id)
);




CREATE TABLE Tag (
    Id INT PRIMARY KEY,
    Name TEXT NOT NULL
);

CREATE TABLE ArticleTag (
    ArticleId INT NOT NULL,
    TagId INT NOT NULL,

    PRIMARY KEY (ArticleId, TagId),
    FOREIGN KEY (ArticleId) REFERENCES Article(Id),
    FOREIGN KEY (TagId) REFERENCES Tag(Id)
);