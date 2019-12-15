# chat_limit_back

python3 with virtual environment is used to host this application
pip required packages are in the requirements.txt file

###### setup of database:

create database chat;
use chat;
create table chats(id int auto_increment not null primary key,name varchar(100),msg varchar(100),time timestamp default current_timestamp not null);
create table users(id int(11) auto_increment primary key,name varchar(100),password varchar(100));
insert into users(name,password) values("chethan","1234567890");
insert into users(name,password) values("thrishik","0987654321");
insert into users(name,password) values("test","test");

##### for server:
pip3 install flask
