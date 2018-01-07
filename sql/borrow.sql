use LibrarySystem;
create table b_r(
	pid varchar(20) COLLATE utf8mb4_unicode_ci not null,
	isbn varchar(20) COLLATE utf8mb4_unicode_ci not null,
	b_date varchar(20) COLLATE utf8mb4_unicode_ci not null,
	b_count int,
	id int(10) not null,
	primary key(id),
	key pid(pid),
	constraint FK_2 foreign key(pid) references reader(pid),
	key isbn(isbn),
	constraint FK_3 foreign key(isbn) references b(isbn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
Alter table b_r change id id int(10) not null auto_increment;
#alter table b_r add constraint FK_2 foreign key(pid) references reader(pid);
#alter table b_r add constraint FK_3 foreign key(isbn) references b(isbn);
#alter table b modify isbn varchar(20) not null unique;
insert into b_r values('210123199712300000', '111', '2017-11-7', 1);
insert into b_r(pid, isbn, b_date, b_count) values('210123199712300000', '9787100022774', '2017-11-7', 1);