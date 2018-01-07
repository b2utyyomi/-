use librarysystem;
#图书部分信息的视图
create view V_book1
as
select isbn, bn, maxstore from b;
#在馆的书的视图
/*
create view V_book
as
select isbn, bn, bk, bs,author,publisher, publishdate,maxstore, rest 
from b where rest != 0;
*/
#读者视图
/*
create view V_reader
as 
select rn, pid,tele,rkn, max_day, max_b
from reader, kind where reader.kno = kind.kno;
*/
#借书的视图
/*
create view V_b_r
as
select rn, reader.pid, b.isbn, bn, b_date,b_count
from reader, b, b_r
where reader.pid = b_r.pid and b.isbn=b_r.isbn;
*/