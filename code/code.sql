create table user (
  user_id int primary key auto_increment,
  staff_id int not null,
  suer_name varchar(32) not null,
  user_pwd VARCHAR(16) not null
);
insert into user values(1000,1000,"administrator","123456");
