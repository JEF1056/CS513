from DatalogGenerator import *
from DatalogValidator import *

# @BEGIN main
# @IN csv_dish_cleaned @URI file:InputDishCleaned.csv
# @IN csv_menuitem_cleaned @URI file:InputMenuItemCleaned.csv
# @IN csv_menupage_cleaned @URI file:InputMenuPageCleaned.csv
# @IN csv_menu_cleaned @URI file:InputMenuCleaned.csv
# @IN csv_dish_dirty @URI file:InputDishDirty.csv
# @IN csv_menuitem_dirty @URI file:InputMenuItemDirty.csv
# @IN csv_menupage_dirty @URI file:InputMenuPageDirty.csv
# @IN csv_menu_dirty @URI file:InputMenuDirty.csv
# @IN rules_dish @URI file:DishRules.lp
# @IN rules_menuitem @URI file:MenuItemRules.lp
# @IN rules_menupage @URI file:MenuPageRules.lp
# @IN rules_menu @URI file:MenuRules.lp
# @IN rules_combined @URI file:CombinedRules.lp
# @OUT facts_dish_cleaned @URI file:cleaned/Dish.lp
# @OUT facts_menuitem_cleaned @URI file:cleaned/MenuItem.lp
# @OUT facts_menupage_cleaned @URI file:cleaned/MenuPage.lp
# @OUT facts_menu_cleaned @URI file:cleaned/Menu.lp
# @OUT facts_combined_cleaned @URI file:cleaned/Combined.lp
# @OUT facts_dish_dirty @URI file:dirty/Dish.lp
# @OUT facts_menuitem_dirty @URI file:dirty/MenuItem.lp
# @OUT facts_menupage_dirty @URI file:dirty/MenuPage.lp
# @OUT facts_menu_dirty @URI file:dirty/Menu.lp
# @OUT facts_combined_dirty @URI file:dirty/Combined.lp
# @OUT model_dish_cleaned @URI file:cleaned/DishModel.txt
# @OUT model_dish_dirty @URI file:dirty/DishModel.txt
# @OUT model_menuitem_cleaned @URI file:/cleaned/MenuItemModel.txt
# @OUT model_menuitem_dirty @URI file:/dirty/MenuItemModel.txt
# @OUT model_menupage_cleaned @URI file:/cleaned/MenuPageModel.txt
# @OUT model_menupage_dirty @URI file:/dirty/MenuPageModel.txt
# @OUT model_menu_cleaned @URI file:/cleaned/MenuModel.txt
# @OUT model_menu_dirty @URI file:/dirty/MenuModel.txt
# @OUT model_combined_cleaned @URI file:cleaned/CombinedModel.txt
# @OUT model_combined_dirty @URI file:dirty/CombinedModel.txt
# @OUT violations_dish_cleaned @URI file:cleaned/DishViolations.txt
# @OUT violations_dish_dirty @URI file:dirty/DishViolations.txt
# @OUT violations_menuitem_cleaned @URI file:/cleaned/MenuItemViolations.txt
# @OUT violations_menuitem_dirty @URI file:/dirty/MenuItemViolations.txt
# @OUT violations_menupage_cleaned @URI file:/cleaned/MenuPageViolations.txt
# @OUT violations_menupage_dirty @URI file:/dirty/MenuPageViolations.txt
# @OUT violations_menu_cleaned @URI file:/cleaned/MenuViolations.txt
# @OUT violations_menu_dirty @URI file:/dirty/MenuViolations.txt
# @OUT violations_combined_cleaned @URI file:/cleaned/CombinedViolations.txt
# @OUT violations_combined_dirty @URI file:/dirty/CombinedViolations.txt
def main():

    # @BEGIN generate_datalog_file_dish_cleaned
    # @IN csv @AS csv_dish_cleaned @URI file:InputDishCleaned.csv
    # @IN rules @AS rules_dish @URI file:DishRules.lp
    # @OUT output @AS facts_dish_cleaned @URI file:cleaned/Dish.lp
    print("Generating datalog for Dish")
    generate_datalog_file_dish("InputDishCleaned.csv", "DishRules.lp", "generated/cleaned/Dish.lp")
    # @END generate_datalog_file_dish_cleaned

    # @BEGIN generate_datalog_file_dish_dirty
    # @IN csv @AS csv_dish_dirty @URI file:InputDishDirty.csv
    # @IN rules @AS rules_dish @URI file:DishRules.lp
    # @OUT output @AS facts_dish_dirty @URI file:dirty/Dish.lp
    generate_datalog_file_dish("InputDishDirty.csv", "DishRules.lp", "generated/dirty/Dish.lp")
    # @END generate_datalog_file_dish_dirty


    # @BEGIN generate_datalog_file_menuitem_cleaned
    # @IN csv @AS csv_menuitem_cleaned @URI file:InputMenuItemCleaned.csv
    # @IN rules @AS rules_menuitem @URI file:MenuItemRules.lp
    # @OUT output @AS facts_menuitem_cleaned @URI file:cleaned/MenuItem.lp
    print("Generating datalog for MenuItem")
    generate_datalog_file_menuitem("InputMenuItemCleaned.csv", "MenuItemRules.lp", "generated/cleaned/MenuItem.lp")
    # @END generate_datalog_file_menuitem_cleaned

    # @BEGIN generate_datalog_file_menuitem_dirty
    # @IN csv @AS csv_menuitem_dirty @URI file:InputMenuItemDirty.csv
    # @IN rules @AS rules_menuitem @URI file:MenuItemRules.lp
    # @OUT output @AS facts_menuitem_dirty @URI file:dirty/MenuItem.lp
    generate_datalog_file_menuitem("InputMenuItemDirty.csv", "MenuItemRules.lp", "generated/dirty/MenuItem.lp")
    # @END generate_datalog_file_menuitem_dirty


    # @BEGIN generate_datalog_file_menupage_cleaned
    # @IN csv @AS csv_menupage_cleaned @URI file:InputMenuPageCleaned.csv
    # @IN rules @AS rules_menupage @URI file:MenuPageRules.lp
    # @OUT output @AS facts_menupage_cleaned @URI file:cleaned/MenuPage.lp
    print("Generating datalog for MenuPage")
    generate_datalog_file_menupage("InputMenuPageCleaned.csv", "MenuPageRules.lp", "generated/cleaned/MenuPage.lp")
    # @END generate_datalog_file_menupage_cleaned

    # @BEGIN generate_datalog_file_menupage_dirty
    # @IN csv @AS csv_menupage_dirty @URI file:InputMenuPageDirty.csv
    # @IN rules @AS rules_menupage @URI file:MenuPageRules.lp
    # @OUT output @AS facts_menupage_dirty @URI file:dirty/MenuPage.lp
    generate_datalog_file_menupage("InputMenuPageDirty.csv", "MenuPageRules.lp", "generated/dirty/MenuPage.lp")
    # @END generate_datalog_file_menupage_dirty


    # @BEGIN generate_datalog_file_menu_cleaned
    # @IN csv @AS csv_menu_cleaned @URI file:InputMenuCleaned.csv
    # @IN rules @AS rules_menu @URI file:MenuRules.lp
    # @OUT output @AS facts_menu_cleaned @URI file:cleaned/Menu.lp
    generate_datalog_file_menu("InputMenuCleaned.csv", "MenuRules.lp", "generated/cleaned/Menu.lp")
    # @END generate_datalog_file_menu_cleaned

    # @BEGIN generate_datalog_file_menu_dirty
    # @IN csv @AS csv_menu_dirty @URI file:InputMenuDirty.csv
    # @IN rules @AS rules_menu @URI file:MenuRules.lp
    # @OUT output @AS facts_menu_dirty @URI file:dirty/Menu.lp
    generate_datalog_file_menu("InputMenuDirty.csv", "MenuRules.lp", "generated/dirty/Menu.lp")
    # @END generate_datalog_file_menu_dirty


    # @BEGIN generate_datalog_file_combined_cleaned
    # @IN csv_1 @AS csv_dish_cleaned @URI file:InputDishCleaned.csv
    # @IN csv_2 @AS csv_menu_cleaned @URI file:InputMenuCleaned.csv
    # @IN csv_3 @AS csv_menuitem_cleaned @URI file:InputMenuItemCleaned.csv
    # @IN csv_4 @AS csv_menupage_cleaned @URI file:InputMenuPageCleaned.csv
    # @IN rules @AS rules_combined @URI file:CombinedRules.lp
    # @OUT output @AS facts_combined_cleaned @URI file:cleaned/Combined.lp
    generate_datalog_file_combined("InputDishCleaned.csv", "InputMenuCleaned.csv",
                                   "InputMenuItemCleaned.csv", "InputMenuPageCleaned.csv",
                                   "CombinedRules.lp", "generated/cleaned/Combined.lp")
    # @END generate_datalog_file_combined_cleaned

    # @BEGIN generate_datalog_file_combined_dirty
    # @IN csv_1 @AS csv_dish_dirty @URI file:InputDishDirty.csv
    # @IN csv_2 @AS csv_menu_dirty @URI file:InputMenuDirty.csv
    # @IN csv_3 @AS csv_menuitem_dirty @URI file:InputMenuItemDirty.csv
    # @IN csv_4 @AS csv_menupage_dirty @URI file:InputMenuPageDirty.csv
    # @IN rules @AS rules_combined @URI file:CombinedRules.lp
    # @OUT output @AS facts_combined_dirty @URI file:dirty/Combined.lp
    generate_datalog_file_combined("InputDishDirty.csv", "InputMenuDirty.csv",
                                   "InputMenuItemDirty.csv", "InputMenuPageDirty.csv",
                                   "CombinedRules.lp", "generated/dirty/Combined.lp")
    # @END generate_datalog_file_combined_dirty
    

    print("Checking integrity constraints for Dish")


    # @BEGIN build_clingo_model_dish_cleaned
    # @IN facts @AS facts_dish_cleaned @URI file:cleaned/Dish.lp
    # @OUT model @AS model_dish_cleaned @URI file:cleaned/DishModel.txt
    generate_model("generated/cleaned/Dish.lp", "generated/cleaned/DishModel.txt")
    # @END build_clingo_model_dish_cleaned

    # @BEGIN validate_datalog_ic_dish_cleaned
    # @IN model @AS model_dish_cleaned @URI file:cleaned/DishModel.txt
    # @OUT violations @AS violations_dish_cleaned @URI file:cleaned/DishViolations.txt
    validate_datalog_dish("generated/cleaned/DishModel.txt", "generated/cleaned/DishViolations.txt")
    # @END validate_datalog_ic_dish_cleaned


    # @BEGIN build_clingo_model_dish_dirty
    # @IN facts @AS facts_dish_dirty @URI file:dirty/Dish.lp
    # @OUT model @AS model_dish_dirty @URI file:dirty/DishModel.txt
    generate_model("generated/dirty/Dish.lp", "generated/dirty/DishModel.txt")
    # @END build_clingo_model_dish_dirty

    # @BEGIN validate_datalog_ic_dish_dirty
    # @IN model @AS model_dish_dirty @URI file:dirty/DishModel.txt
    # @OUT violations @AS violations_dish_dirty @URI file:dirty/DishViolations.txt
    validate_datalog_dish("generated/dirty/DishModel.txt", "generated/dirty/DishViolations.txt")
    # @END validate_datalog_ic_dish_dirty


    print("Checking integrity constraints for MenuItem")

    # @BEGIN build_clingo_model_menuitem_cleaned
    # @IN facts @AS facts_menuitem_cleaned @URI file:cleaned/MenuItem.lp
    # @OUT model @AS model_menuitem_cleaned @URI file:cleaned/MenuItemModel.txt
    generate_model("generated/cleaned/MenuItem.lp", "generated/cleaned/MenuItemModel.txt")
    # @END build_clingo_model_menuitem_cleaned

    # @BEGIN validate_datalog_ic_menuitem_cleaned
    # @IN model @AS model_menuitem_cleaned @URI file:cleaned/MenuItemModel.txt
    # @OUT violations @AS violations_menuitem_cleaned @URI file:cleaned/MenuItemViolations.txt
    validate_datalog_menuitem("generated/cleaned/MenuItemModel.txt", "generated/cleaned/MenuItemViolations.txt")
    # @END validate_datalog_ic_menuitem_cleaned


    # @BEGIN build_clingo_model_menuitem_dirty
    # @IN facts @AS facts_menuitem_dirty @URI file:dirty/MenuItem.lp
    # @OUT model @AS model_menuitem_dirty @URI file:dirty/MenuItemModel.txt
    generate_model("generated/dirty/MenuItem.lp", "generated/dirty/MenuItemModel.txt")
    # @END build_clingo_model_menuitem_dirty

    # @BEGIN validate_datalog_ic_menuitem_dirty
    # @IN model @AS model_menuitem_dirty @URI file:dirty/MenuItemModel.txt
    # @OUT violations @AS violations_menuitem_dirty @URI file:dirty/MenuItemViolations.txt
    validate_datalog_menuitem("generated/dirty/MenuItemModel.txt", "generated/dirty/MenuItemViolations.txt")
    # @END validate_datalog_ic_menuitem_dirty


    print("Checking integrity constaints for MenuPage")


    # @BEGIN build_clingo_model_menupage_cleaned
    # @IN facts @AS facts_menupage_cleaned @URI file:cleaned/MenuPage.lp
    # @OUT model @AS model_menupage_cleaned @URI file:cleaned/MenuPageModel.txt
    generate_model("generated/cleaned/MenuPage.lp", "generated/cleaned/MenuPageModel.txt")
    # @END build_clingo_model_menupage_cleaned

    # @BEGIN validate_datalog_ic_menupage_cleaned
    # @IN model @AS model_menupage_cleaned @URI file:cleaned/MenuPageModel.txt
    # @OUT violations @AS violations_menupage_cleaned @URI file:cleaned/MenuPageViolations.txt
    validate_datalog_menupage("generated/cleaned/MenuPageModel.txt", "generated/cleaned/MenuPageViolations.txt")
    # @END validate_datalog_ic_menupage_cleaned


    # @BEGIN build_clingo_model_menupage_dirty
    # @IN facts @AS facts_menupage_dirty @URI file:dirty/MenuPage.lp
    # @OUT model @AS model_menupage_dirty @URI file:dirty/MenuPageModel.txt
    generate_model("generated/dirty/MenuPage.lp", "generated/dirty/MenuPageModel.txt")
    # @END build_clingo_model_menupage_dirty

    # @BEGIN validate_datalog_ic_menupage_dirty
    # @IN model @AS model_menupage_dirty @URI file:dirty/MenuPageModel.txt
    # @OUT violations @AS violations_menupage_dirty @URI file:dirty/MenuPageViolations.txt
    validate_datalog_menupage("generated/dirty/MenuPageModel.txt", "generated/dirty/MenuPageViolations.txt")
    # @END validate_datalog_ic_menupage_dirty


    print("Checking integrity constaints for Menu") 


    # @BEGIN build_clingo_model_menu_cleaned
    # @IN facts @AS facts_menu_cleaned @URI file:cleaned/Menu.lp
    # @OUT model @AS model_menu_cleaned @URI file:cleaned/MenuModel.txt
    generate_model("generated/cleaned/Menu.lp", "generated/cleaned/MenuModel.txt")
    # @END build_clingo_model_menu_cleaned

    # @BEGIN validate_datalog_ic_menu_cleaned
    # @IN model @AS model_menu_cleaned @URI file:cleaned/MenuModel.txt
    # @OUT violations @AS violations_menu_cleaned @URI file:cleaned/MenuViolations.txt
    validate_datalog_menu("generated/cleaned/MenuModel.txt", "generated/cleaned/MenuViolations.txt")
    # @END validate_datalog_ic_menu_cleaned


    # @BEGIN build_clingo_model_menu_dirty
    # @IN facts @AS facts_menu_dirty @URI file:dirty/Menu.lp
    # @OUT model @AS model_menu_dirty @URI file:dirty/MenuModel.txt
    generate_model("generated/dirty/Menu.lp", "generated/dirty/MenuModel.txt")
    # @END build_clingo_model_menu_dirty

    # @BEGIN validate_datalog_ic_menu_dirty
    # @IN model @AS model_menu_dirty @URI file:dirty/MenuModel.txt
    # @OUT violations @AS violations_menu_dirty @URI file:dirty/MenuViolations.txt
    validate_datalog_menu("generated/dirty/MenuModel.txt", "generated/dirty/MenuViolations.txt")
    # @END validate_datalog_ic_menu_dirty


    print("Checking integrity constaints for Combined") 


    # @BEGIN build_clingo_model_combined_cleaned
    # @IN facts @AS facts_combined_cleaned @URI file:cleaned/Combined.lp
    # @OUT model @AS model_combined_cleaned @URI file:cleaned/CombinedModel.txt
    generate_model("generated/cleaned/Combined.lp", "generated/cleaned/CombinedModel.txt")
    # @END build_clingo_model_combined_cleaned

    # @BEGIN validate_datalog_ic_combined_cleaned
    # @IN model @AS model_combined_cleaned @URI file:cleaned/CombinedModel.txt
    # @OUT violations @AS violations_combined_cleaned @URI file:cleaned/CombinedViolations.txt
    validate_datalog_menu("generated/cleaned/CombinedModel.txt", "generated/cleaned/CombinedViolations.txt")
    # @END validate_datalog_ic_combined_cleaned

    # @BEGIN build_clingo_model_combined_dirty
    # @IN facts @AS facts_combined_dirty @URI file:dirty/Combined.lp
    # @OUT model @AS model_combined_dirty @URI file:dirty/CombinedModel.txt
    generate_model("generated/dirty/Combined.lp", "generated/dirty/CombinedModel.txt")
    # @END build_clingo_model_combined_dirty

    # @BEGIN validate_datalog_ic_combined_dirty
    # @IN model @AS model_combined_dirty @URI file:dirty/CombinedModel.txt
    # @OUT violations @AS violations_combined_dirty @URI file:dirty/CombinedViolations.txt
    validate_datalog_menu("generated/dirty/CombinedModel.txt", "generated/dirty/CombinedViolations.txt")
    # @END validate_datalog_ic_combined_dirty


if __name__ == "__main__":
    main()

# @END main
