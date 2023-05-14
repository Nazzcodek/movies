-- Managers Details
select CONCAT(s.first_name, ' ', s.last_name) as manager, a.address, a.district, c.city, co.country
from staff s
inner join address a 
on s.address_id = a.address_id
inner join city c
on c.city_id = a.city_id
inner join country co
on c.country_id = co.country_id;

-- Inventory
select s.store_id, f.title, i.inventory_id, f.rating, f.rental_rate, f.replacement_cost
from store s
join inventory i
on s.store_id = i.store_id
join film f 
on f.film_id = i.film_id;

-- Inventory by ratings
select s.store_id, f.rating,
       count(*) as inventory_items
from store s
join inventory i
on s.store_id = i.store_id
join film f 
on f.film_id = i.film_id
group by s.store_id, f.rating;

-- Replacement cost
select s.store_id, fc.category_id,
       count(*) as number_of_films,
       avg(f.replacement_cost) as average_replacement_cost,
       sum(f.replacement_cost) as total_replacement_cost
from store s
join inventory i
on s.store_id = i.store_id
join film f 
on f.film_id = i.film_id
join film_category fc
on f.film_id = fc.film_id
group by s.store_id, fc.category_id;

-- customer details
select cu.store_id,
	CONCAT(cu.first_name, ' ', cu.last_name) as name,
	cu.active,
	CONCAT(a.address, ' ', ci.city, ' ', co.country) as full_address
from customer cu
join address a
on a.address_id = cu.address_id
join city ci
on ci.city_id = a.city_id
join country co
on co.country_id = ci.country_id;

-- Lifetime Value
SELECT
  customer_name,
  total_lifetime_rentals,
  sum_of_payments
FROM (
  SELECT
    CONCAT(cu.first_name, ' ', cu.last_name) AS customer_name,
    COUNT(*) AS total_lifetime_rentals,
    SUM(p.amount) AS sum_of_payments
  FROM
    customer cu
  JOIN rental r
    ON r.customer_id = cu.customer_id
  JOIN payment p
    ON r.rental_id = p.rental_id
  GROUP BY
    customer_name
) AS customer_lifetime_value
ORDER BY
  sum_of_payments DESC;

--   investor or advisor
select CONCAT(first_name, ' ', last_name) as name,
	'Advisor' as role,
	NULL as company  
from advisor
union all
select 
	CONCAT(first_name, ' ', last_name) as name,
	'Investor' as role,
	company_name 
from investor;