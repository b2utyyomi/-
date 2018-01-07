use librarysystem;
create table kind(
	kno varchar(10) COLLATE utf8mb4_unicode_ci not null,
	rkn varchar(20) COLLATE utf8mb4_unicode_ci not null,
	max_day int not null,
	max_b int not null,
	primary key(kno)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

create table reader(
	rn varchar(20) COLLATE utf8mb4_unicode_ci not null,
	pid varchar(20) COLLATE utf8mb4_unicode_ci not null unique,
	tele varchar(20) COLLATE utf8mb4_unicode_ci not null unique,
	kno varchar(10) COLLATE utf8mb4_unicode_ci not null,
	primary key(pid)
	 
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

 alter table reader add constraint FK_1 foreign key(kno) references kind(kno);

