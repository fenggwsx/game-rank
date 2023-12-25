CREATE TABLE rank(
    id integer primary key autoincrement,
    username varchar(64) not null,
    checkpoint varchar(64) not null,
    time double not null,
    update_time datetime not null,
    create_time datetime not null,
    unique (username, checkpoint)
);
