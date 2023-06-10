DROP TABLE IF EXISTS db_docbot.log_botmessages;

DROP TABLE IF EXISTS db_docbot.users;

CREATE TABLE users (
  id        int(11)                       NOT NULL AUTO_INCREMENT,
  email     varchar(80)                   NOT NULL,
  full_name varchar(100)                  NOT NULL,
  gender    enum('laki-laki','perempuan') DEFAULT 'laki-laki',
  username  varchar(64)                   NOT NULL,
  password  varchar(500)                  NOT NULL,
  created   timestamp                     DEFAULT current_timestamp(),
  updated   timestamp                     DEFAULT current_timestamp(),
  PRIMARY KEY (id)
);

CREATE TABLE log_botmessages (
  id        bigint                        NOT NULL AUTO_INCREMENT,
  userId    int(11)                       NOT NULL,
  question  varchar(500)                  NOT NULL,
  answer    text                          NOT NULL,
  created   timestamp                     DEFAULT current_timestamp(),
  PRIMARY KEY (id),
  CONSTRAINT  fk_log_botmessages_users FOREIGN KEY (userId) REFERENCES users (id) ON DELETE CASCADE ON UPDATE CASCADE
);