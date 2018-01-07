use librarysystem;
create table bkind(
	bkn varchar(20) COLLATE utf8mb4_unicode_ci not null,
	primary key(bkn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
insert into bkind values('教育');
insert into bkind values('军事');
insert into bkind values('健康');
insert into bkind values('经济');
insert into bkind values('科幻');
insert into bkind values('美食');
insert into bkind values('散文');
insert into bkind values('童话');
insert into bkind values('医药');
insert into bkind values('政治');
insert into bkind values('哲学');
insert into bkind values('小说');

alter table reader add constraint FK_4 foreign key(bk) references bkind(bkn);