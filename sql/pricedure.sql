# BRQuery
/*
use librarysystem;
DELIMITER $$
create procedure `proc_BRQuery`(
IN query varchar(100)
)
begin
select rn, reader.pid, b.isbn, bn, b_date, b_count from reader,b_r, b 
where reader.pid=b_r.pid and b.isbn=b_r.isbn and b_r.pid = query;
end;
DELIMITER;
*/



-- ----------------------------
-- Procedure structure for `proc_adder`
-- ----------------------------
/*
create procedure proc_BRQuery(
in query varchar(100)
)
begin
	select rn, reader.pid, b.isbn, bn, b_date, b_count from reader,b_r, b where reader.pid=b_r.pid and b.isbn=b_r.isbn and b_r.pid = query;
end;
*/
#查询读者的存储过程

use librarysystem;
#DELIMITER $$
create procedure proc_Reader() 
begin 
    select rn, pid,tele,rkn, max_day, max_b
	from reader, kind where reader.kno = kind.kno;
end$$
#DELIMITER;

/*
#修改图书类别的触发器
#当我修改一个图书的类别为一个不存在的类别时,
#会自动向图书类别中添加这个类别
#update b set bk = new.bk where bk = old.bk;

DELIMITER $
CREATE TRIGGER change_bk 
BEFORE UPDATE
ON b FOR EACH ROW

BEGIN
	if(new.bk not in (select bkn
         from bkind))
	then
		insert into bkind values(new.bk);
	end if;
END$


DELIMITER $
CREATE TRIGGER change_bk1
AFTER UPDATE
ON b FOR EACH ROW 
BEGIN
	if(old.bk not in (select bk
         from b))
	then
	delete from bkind where bkn = old.bk;
	end if;
END$
*/

/*
DELIMITER $
CREATE TRIGGER add_r AFTER INSERT
ON reader FOR EACH ROW 
BEGIN
	UPDATE total SET num=num+1 WHERE name='reader';
END$
*/