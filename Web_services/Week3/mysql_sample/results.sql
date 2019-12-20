use test
set names utf8;

-- 1. Выбрать все товары (все поля)
select * from product;

-- 2. Выбрать названия всех автоматизированных складов
select * from store;

-- 3. Посчитать общую сумму в деньгах всех продаж
select sum(total) from sale;

-- 4. Получить уникальные store_id всех складов, с которых была хоть одна продажа
select store_id from store natural  left join sale where not sale.total is null;

-- 5. Получить уникальные store_id всех складов, с которых не было ни одной продажи
select store_id from store natural  left join sale where sale.total is null;

-- 6. Получить для каждого товара название и среднюю стоимость единицы товара avg(total/quantity), если товар не продавался, он не попадает в отчет.
select name, avg(total/quantity) from sale natural join product group by product.product_id;

-- 7. Получить названия всех продуктов, которые продавались только с единственного склада
select name from product natural join sale group by product_id having count(distinct store_id) = 1;

-- 8. Получить названия всех складов, с которых продавался только один продукт
select any_value(name) from store natural join sale group by product_id having count(DISTINCT store_id)=1;

-- 9. Выберите все ряды (все поля) из продаж, в которых сумма продажи (total) максимальна (равна максимальной из всех встречающихся)
select *  from sale order by total desc limit 1;

-- 10. Выведите дату самых максимальных продаж, если таких дат несколько, то самую раннюю из них
select date from sale where total = (select max(total) from sale);
