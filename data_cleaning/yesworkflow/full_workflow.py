# @BEGIN main

# @IN csv_dish_dirty @URI file:NYPL-menus/Dish.csv
# @IN csv_menuitem_dirty @URI file:NYPL-menus/MenuItem.csv
# @IN csv_menupage_dirty @URI file:NYPL-menus/MenuPage.csv
# @IN csv_menu_dirty @URI file:NYPL-menus/Menu.csv

# @IN rules_dish @URI file:data_cleaning/datalog/DishRules.lp
# @IN rules_menuitem @URI file:data_cleaning/datalog/MenuItemRules.lp
# @IN rules_menupage @URI file:data_cleaning/datalog/MenuPageRules.lp
# @IN rules_menu @URI file:data_cleaning/datalog/MenuRules.lp

# @OUT csv_dish_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Dish_cleaned.csv
# @OUT csv_menupage_openrefine @URI file:data_cleaning/openrefine/OpenRefine_MenuPage_cleaned.csv
# @OUT csv_menu_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Menu_cleaned.csv

# @OUT history_dish_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Dish_history.csv
# @OUT history_menupage_openrefine @URI file:data_cleaning/openrefine/OpenRefine_MenuPage_history.csv
# @OUT history_menu_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Menu_history.csv

# @OUT csv_menuitem_python @URI file:Python_MenuItem_cleaned.csv

# @OUT oryw_dish @URI file:data_cleaning/yesworkflow/yw_openrefine_Dish.png
# @OUT oryw_menupage @URI file:data_cleaning/yesworkflow/yw_openrefine_MenuPage.png
# @OUT oryw_menu @URI file:data_cleaning/yesworkflow/yw_openrefine_Menu.png

# @OUT facts_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/Dish.lp
# @OUT facts_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItem.lp
# @OUT facts_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPage.lp
# @OUT facts_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/Menu.lp

# @OUT facts_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/Dish.lp
# @OUT facts_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItem.lp
# @OUT facts_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPage.lp
# @OUT facts_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/Menu.lp

# @OUT model_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/DishModel.txt
# @OUT model_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/DishModel.txt
# @OUT model_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItemModel.txt
# @OUT model_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItemModel.txt
# @OUT model_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPageModel.txt
# @OUT model_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPageModel.txt
# @OUT model_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuModel.txt
# @OUT model_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuModel.txt

# @OUT violations_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/DishViolations.txt
# @OUT violations_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/DishViolations.txt
# @OUT violations_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItemViolations.txt
# @OUT violations_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItemViolations.txt
# @OUT violations_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPageViolations.txt
# @OUT violations_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPageViolations.txt
# @OUT violations_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuViolations.txt
# @OUT violations_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuViolations.txt

def main():

    print("Define YW for OpenRefine")

    # @BEGIN openrefine_dish
    # @IN csv_in @AS csv_dish_dirty @URI file:NYPL-menus/Dish.csv
    # @OUT csv_out @AS csv_dish_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Dish_cleaned.csv
    # @OUT history @AS history_dish_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Dish_history.json
    x = 0
    # @END openrefine_dish

    # @BEGIN openrefine_menupage
    # @IN csv_in @AS csv_menupage_dirty @URI file:NYPL-menus/MenuPage.csv
    # @OUT csv_out @AS csv_menupage_openrefine @URI file:data_cleaning/openrefine/OpenRefine_MenuPage_cleaned.csv
    # @OUT history @AS history_menupage_openrefine @URI file:data_cleaning/openrefine/OpenRefine_MenuPage_history.json
    x = x + 1
    # @END openrefine_menupage

    # @BEGIN openrefine_menu
    # @IN csv_in @AS csv_menu_dirty @URI file:NYPL-menus/Menu.csv
    # @OUT csv_out @AS csv_menu_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Menu_cleaned.csv
    # @OUT history @AS history_menu_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Menu_history.json
    x = x + 1
    # @END openrefine_menu


    print("Define YW for OpenRefine history")


    # @BEGIN or2yw_dish
    # @IN history @AS history_dish_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Dish_history.json
    # @OUT png @AS oryw_dish @URI file:data_cleaning/yesworkflow/yw_openrefine_Dish.png
    x = x + 1
    # @END or2yw_dish

    # @BEGIN or2yw_menupage
    # @IN history @AS history_menupage_openrefine @URI file:data_cleaning/openrefine/OpenRefine_MenuPage_history.json
    # @OUT png @AS oryw_menupage @URI file:data_cleaning/yesworkflow/yw_openrefine_MenuPage.png
    x = x + 1
    # @END or2yw_menupage

    # @BEGIN or2yw_menu
    # @IN history @AS history_menu_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Menu_history.json
    # @OUT png @AS oryw_menu @URI file:data_cleaning/yesworkflow/yw_openrefine_Menu.png
    x = x + 1
    # @END or2yw_menu


    print("Define YW for MenuItem")

    # @BEGIN python_menuitem
    # @IN csv_menuitem_dirty @URI file:NYPL-menus/MenuItem.csv
    # @OUT csv_menuitem_python @URI file:Python_MenuItem_cleaned.csv
    x = x + 1
    # @END python_menuitem

    print("Define YW for Datalog fact, model, and violations")


    # @BEGIN datalog_facts_dish
    # @IN csv_cleaned @AS csv_dish_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Dish_cleaned.csv
    # @IN csv_dirty @AS csv_dish_dirty @URI file:NYPL-menus/Dish.csv
    # @IN rules @AS rules_dish @URI file:data_cleaning/datalog/DishRules.lp
    # @OUT facts_cleaned @AS facts_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/Dish.lp
    # @OUT facts_dirty @AS facts_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/Dish.lp
    x = x + 1
    # @END datalog_facts_dish

    # @BEGIN datalog_model_dish
    # @IN facts_cleaned @AS facts_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/Dish.lp
    # @IN facts_dirty @AS facts_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/Dish.lp
    # @OUT model_cleaned @AS model_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/DishModel.txt
    # @OUT model_dirty @AS model_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/DishModel.txt
    x = x + 1
    # @END datalog_model_dish

    # @BEGIN datalog_violations_dish
    # @IN model_cleaned @AS model_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/DishModel.txt
    # @IN model_dirty @AS model_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/DishModel.txt
    # @OUT violations_cleaned @AS violations_dish_cleaned @URI file:data_cleaning/datalog/generated/cleaned/DishViolations.txt
    # @OUT violations_dirty @AS violations_dish_dirty @URI file:data_cleaning/datalog/generated/dirty/DishViolations.txt
    x = x + 1
    # @END datalog_violations_dish


    # @BEGIN datalog_facts_menuitem
    # @IN csv_cleaned @AS csv_menuitem_python @URI file:Python_MenuItem_cleaned.csv
    # @IN csv_dirty @AS csv_menuitem_dirty @URI file:NYPL-menus/MenuItem.csv
    # @IN rules @AS rules_menuitem @URI file:data_cleaning/datalog/MenuItemRules.lp
    # @OUT facts_cleaned @AS facts_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItem.lp
    # @OUT facts_dirty @AS facts_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItem.lp
    x = x + 1
    # @END datalog_facts_menuitem

    # @BEGIN datalog_model_menuitem
    # @IN facts_cleaned @AS facts_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItem.lp
    # @IN facts_dirty @AS facts_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItem.lp
    # @OUT model_cleaned @AS model_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItemModel.txt
    # @OUT model_dirty @AS model_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItemModel.txt
    x = x + 1
    # @END datalog_model_menuitem

    # @BEGIN datalog_violations_menuitem
    # @IN model_cleaned @AS model_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItemModel.txt
    # @IN model_dirty @AS model_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItemModel.txt
    # @OUT violations_cleaned @AS violations_menuitem_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuItemViolations.txt
    # @OUT violations_dirty @AS violations_menuitem_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuItemViolations.txt
    x = x + 1
    # @END datalog_violations_menuitem


    # @BEGIN datalog_facts_menupage
    # @IN csv_cleaned @AS csv_menupage_openrefine @URI file:data_cleaning/openrefine/OpenRefine_MenuPage_cleaned.csv
    # @IN csv_dirty @AS csv_menupage_dirty @URI file:NYPL-menus/MenuPage.csv
    # @IN rules @AS rules_menupage @URI file:data_cleaning/datalog/MenuPageRules.lp
    # @OUT facts_cleaned @AS facts_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPage.lp
    # @OUT facts_dirty @AS facts_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPage.lp
    x = x + 1
    # @END datalog_facts_menupage

    # @BEGIN datalog_model_menupage
    # @IN facts_cleaned @AS facts_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPage.lp
    # @IN facts_dirty @AS facts_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPage.lp
    # @OUT model_cleaned @AS model_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPageModel.txt
    # @OUT model_dirty @AS model_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPageModel.txt
    x = x + 1
    # @END datalog_model_menupage

    # @BEGIN datalog_violations_menupage
    # @IN model_cleaned @AS model_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPageModel.txt
    # @IN model_dirty @AS model_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPageModel.txt
    # @OUT violations_cleaned @AS violations_menupage_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuPageViolations.txt
    # @OUT violations_dirty @AS violations_menupage_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuPageViolations.txt
    x = x + 1
    # @END datalog_violations_menupage


    # @BEGIN datalog_facts_menu
    # @IN csv_cleaned @AS csv_menu_openrefine @URI file:data_cleaning/openrefine/OpenRefine_Menu_cleaned.csv
    # @IN csv_dirty @AS csv_menu_dirty @URI file:NYPL-menus/Menu.csv
    # @IN rules @AS rules_menu @URI file:data_cleaning/datalog/MenuRules.lp
    # @OUT facts_cleaned @AS facts_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/Menu.lp
    # @OUT facts_dirty @AS facts_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/Menu.lp
    x = x + 1
    # @END datalog_facts_menu

    # @BEGIN datalog_model_menu
    # @IN facts_cleaned @AS facts_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/Menu.lp
    # @IN facts_dirty @AS facts_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/Menu.lp
    # @OUT model_cleaned @AS model_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuModel.txt
    # @OUT model_dirty @AS model_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuModel.txt
    x = x + 1
    # @END datalog_model_menu

    # @BEGIN datalog_violations_menu
    # @IN model_cleaned @AS model_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuModel.txt
    # @IN model_dirty @AS model_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuModel.txt
    # @OUT violations_cleaned @AS violations_menu_cleaned @URI file:data_cleaning/datalog/generated/cleaned/MenuViolations.txt
    # @OUT violations_dirty @AS violations_menu_dirty @URI file:data_cleaning/datalog/generated/dirty/MenuViolations.txt
    x = x + 1
    # @END datalog_violations_menu


    x = x + 1

# @END main