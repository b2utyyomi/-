use librarysystem;
create table bkind(
	bkn varchar(20) COLLATE utf8mb4_unicode_ci not null,
	primary key(bkn)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
insert into bkind values('����');
insert into bkind values('����');
insert into bkind values('����');
insert into bkind values('����');
insert into bkind values('�ƻ�');
insert into bkind values('��ʳ');
insert into bkind values('ɢ��');
insert into bkind values('ͯ��');
insert into bkind values('ҽҩ');
insert into bkind values('����');
insert into bkind values('��ѧ');
insert into bkind values('С˵');

alter table reader add constraint FK_4 foreign key(bk) references bkind(bkn);