use librarysystem;
create table total(
	name varchar(20) COLLATE utf8mb4_unicode_ci not null,
	num int not null,
	primary key(name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
