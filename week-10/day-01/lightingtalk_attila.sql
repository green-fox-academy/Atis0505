use sakila;

select * from actor
limit 50;

select * from payment;

select sum(amount) as Amount_sum from payment;

select staff_id, sum(amount) from payment
group by staff_id;

select customer_id, staff_id, sum(amount) from payment
group by customer_id;

select * from payment
where payment_date > '2005-06-19 00:00:00';

select count(payment_id) from payment
where payment_date > '2005-06-19 00:00:00';