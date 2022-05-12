create schema DHA_system;
use DHA_system;
create table ADHA( 
ADHA_ID int, 
login_password varchar(20), 
username varchar(20), 
starting_date date, 
ending_date date, 
ADHA_rank varchar(20),
primary key (ADHA_ID) );

create table clients(
 client_ID int,
 login_password varchar(20),
 username varchar(20),
 user_rank varchar(20),
 previous_employ bool,
 primary key(client_ID),
 ADHA_ID int,
foreign key (ADHA_ID) REFERENCES ADHA(ADHA_ID)
on DELETE SET NULL ON UPDATE CASCADE);

create table Director
(branch varchar(20),
director_rank varchar(20),
ADHA_ID int,
dir_ID int,
primary key(dir_ID),
foreign key (ADHA_ID) REFERENCES ADHA(ADHA_ID)
on DELETE SET NULL ON UPDATE CASCADE);

create table employees(
emp_ID int,
branch varchar(20),
typeemp varchar(20),
position varchar(20),
duration numeric(5),
alloted_plot_no numeric (5), 
dir_ID int,
client_ID int,
primary key(emp_ID),
foreign key (dir_ID) references Director(dir_ID)
on DELETE SET NULL ON UPDATE CASCADE,
foreign key (client_ID) references clients(client_ID)
on DELETE SET NULL ON UPDATE CASCADE);

create table plots(
phase_no varchar(20) not null,
sector varchar(20) not null,
street varchar(20) not null,
size varchar(20),
client_ID int,
primary key(phase_no, sector,street),
foreign key (client_ID) references clients(client_ID)
ON DELETE SET NULL ON UPDATE CASCADE);


