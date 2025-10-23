use mydb2;
create table books(id int primary key,tittle varchar(50),author varchar(20),publication_year int,genere varchar(20),price float,stock int);
insert into books values (1,'To kill a Mocking Bird','harper lee',1960,'fiction',12.99,10),
(2,'1984','george orwell',1949,'science fiction',10.99,15),
(3,'pride and prejudice','jane Austen',1813,'Romance',9.99,5),
(4,'The Hobbit','J.R.R tolkien',1937,'fantasy',14.99,20),
(5,'The Catcher in The Rye','J.D salinger',1951,'fiction',11.99,8);

select* from books;

select sum(price * stock) as total_inventory_value from books;

select genere,count(*) as book_count from books group by genere;

select tittle,price as original_price,round(price*0.9,2)as discounted_price from books where publication_year<1950;

select tittle  as final_result from books where genere='fiction' or price<12;

select tittle, stock*2 as overstocked from books where stock>10;


