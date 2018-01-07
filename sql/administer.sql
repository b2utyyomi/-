use LibrarySystem;
create table allid(
	id varchar(20) COLLATE utf8mb4_unicode_ci not null,
	pw varchar(20) COLLATE utf8mb4_unicode_ci not null,
	primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

create table ad(
	id varchar(20) COLLATE utf8mb4_unicode_ci not null,
	pw varchar(20) COLLATE utf8mb4_unicode_ci not null,
	primary key(id)

)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;