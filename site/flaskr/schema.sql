CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  salt TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE question (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  model TEXT NOT NULL,
  prompt TEXT NOT NULL,
  response TEXT NOT NULL,
  question TEXT NOT NULL,
  answer BOOLEAN NOT NULL,
  reference TEXT,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE test (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  duration_seconds INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE test_question (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  test_id INTEGER NOT NULL,
  question_id INTEGER NOT NULL,
  question_index INTEGER NOT NULL,
  FOREIGN KEY (test_id) REFERENCES test (id),
  FOREIGN KEY (question_id) REFERENCES question (id),
  UNIQUE(test_id, question_index)
);
CREATE INDEX idx_test_question_test_id ON test_question(test_id);

CREATE TABLE submission (
  test_question_id INTEGER PRIMARY KEY NOT NULL,
  answer BOOLEAN NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (test_question_id) REFERENCES test_question (id)
);
