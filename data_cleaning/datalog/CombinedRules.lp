% Not including all columns to help reduce data size
% dish(id)
% menu(id)
% menuitem(id, menu_page_id, dish_id)
% menupage(id, menu_id)

% the menu_id column from MenuPage is a foreign key for Menu
icv_menuid_is_fk_in_menu(ID) :- menupage(_, ID), not menu(ID).

% the menu_page_id column from MenuItem is a foreign key for MenuPage
icv_menupageid_is_fk_in_menupage(ID) :- menuitem(_, ID, _), not menupage(ID).

% the dish_id column from MenuItem is a foreign key for Dish
icv_dishid_is_fk_in_menuitem(ID) :- menuitem(_, _, ID), not dish(ID).

% every dish_id is referenced in MenuItem
icv_dishid_in_menuitem(ID) :- dish(ID), not menuitem(_, _, ID).

