--U1 Scenarios 
select dish_id,a.name as dish_name,d.name as menu_name,page_number,
menus_appeared,times_appeared,first_appeared,last_appeared,lowest_price,
highest_price,event_category,location,physical_description,notes,created_at
from dishcleaned as a
join menuitemcleaned as b on a.id=b.dish_id
join menupagecleaned as c on b.menu_page_id=c.id
join menucleaned as d on c.menu_id=d.id
where a.name = 'Chicken Gumbo' and first_appeared >= 1914 and last_appeared <= 1918
order by dish_id

--ICV
ALTER TABLE MenuPage
ADD FOREIGN KEY (menu_id) REFERENCES Menu(id)

ALTER TABLE MenuItem
ADD FOREIGN KEY (menu_page_id) REFERENCES MenuPage(id)

ALTER TABLE MenuItem
ADD FOREIGN KEY (dish_id) REFERENCES Dish(id)

SELECT a.menu_id as InvalidPageID, b.id as MenuPageID
FROM MenuPage a
LEFT JOIN Menu b ON a.menu_id = b.id
WHERE b.id IS NULL

SELECT a.menu_page_id as InvalidMenuPageID, b.id as MenuPageID
FROM MenuItem a
LEFT JOIN MenuPage b ON a.menu_page_id = b.id
WHERE b.id IS NULL

SELECT a.dish_id as InvalidDishID, b.id as DishID
FROM MenuItem a
LEFT JOIN Dish b ON a.dish_id = b.id
WHERE b.id IS NULL

ALTER TABLE MenuItemCleaned
ADD FOREIGN KEY (menu_page_id) REFERENCES MenuPageCleaned(id)
