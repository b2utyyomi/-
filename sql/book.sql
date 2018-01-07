create database LibrarySystem;
use LibrarySystem;
create table B(
	isbn varchar(20) COLLATE utf8mb4_unicode_ci not null,
	bn varchar(100) COLLATE utf8mb4_unicode_ci not null,
	bk varchar(20) COLLATE utf8mb4_unicode_ci,
	bs varchar(10) COLLATE utf8mb4_unicode_ci not null,
	maxstore int,
	rest int,
	author varchar(100) COLLATE utf8mb4_unicode_ci not null,
	publisher varchar(100) COLLATE utf8mb4_unicode_ci not null,
	publishdate varchar(20) COLLATE utf8mb4_unicode_ci not null,
	primary key(isbn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

