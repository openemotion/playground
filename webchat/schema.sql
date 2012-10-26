drop table if exists messages;
create table messages (
  id integer primary key autoincrement,
  author string not null,
  text string not null
);

.quit