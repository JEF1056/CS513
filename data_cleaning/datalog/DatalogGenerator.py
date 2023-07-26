import pandas as pd
import math
import os
import pathlib

filepath = pathlib.Path(__file__).parent.absolute()

def generate_datalog_file_dish(input_csv_file, rules_file, output_datalog_file):

    with open(os.path.join(filepath, rules_file), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, output_datalog_file), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, input_csv_file))

            comment = "% Generated from {0}\n".format(input_csv_file)
            file.write(comment)

            for _, row in df.iterrows():
                name = str(row["name"]).replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["name"]) else ""
                description = str(row["description"]).replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["description"]) else ""

                lowest_price = 0 if math.isnan(row["lowest_price"]) else int(row["lowest_price"])
                highest_price = 0 if math.isnan(row["highest_price"]) else int(row["highest_price"])

                line = "dish({0}, \"{1}\", \"{2}\", {3}, {4}, {5}, {6}, {7}, {8}).\n".format(row["id"], name, description, row["menus_appeared"], row["times_appeared"], row["first_appeared"], row["last_appeared"], lowest_price, highest_price)
                file.write(line)
            
    print("Done generating datalog file {0}.".format(output_datalog_file))


def generate_datalog_file_menuitem(input_csv_file, rules_file, output_datalog_file):
    with open(os.path.join(filepath, rules_file), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, output_datalog_file), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, input_csv_file))

            comment = "% Generated from {0}\n".format(input_csv_file)
            file.write(comment)

            for _, row in df.iterrows():
                price = 0.0 if math.isnan(row["price"]) else row["price"]
                high_price = 0.0 if math.isnan(row["high_price"]) else row["high_price"]
                dish_id = -1 if math.isnan(row["dish_id"]) else int(row["dish_id"])

                line = "menuitem({0}, {1}, \"{2}\", \"{3}\", {4}, \"{5}\", \"{6}\", \"{7}\", \"{8}\").\n".format(row["id"], row["menu_page_id"], price, high_price, dish_id, row["created_at"], row["updated_at"], row["xpos"], row["ypos"])
                file.write(line)

    print("Done generating datalog file {0}.".format(output_datalog_file))


def generate_datalog_file_menupage(input_csv_file, rules_file, output_datalog_file):
    with open(os.path.join(filepath, rules_file), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, output_datalog_file), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, input_csv_file))

            comment = "% Generated from {0}\n".format(input_csv_file)
            file.write(comment)

            for _, row in df.iterrows():
                page_number = 0 if math.isnan(row["page_number"]) else int(row["page_number"])
                full_height = 0 if math.isnan(row["full_height"]) else int(row["full_height"])
                full_width = 0 if math.isnan(row["full_width"]) else int(row["full_width"])

                line = "menupage({0}, {1}, {2}, {3}, {4}, {5}, \"{6}\").\n".format(row["id"], row["menu_id"], page_number, row["image_id"], full_height, full_width, row["uuid"])
                file.write(line)

    print("Done generating datalog file {0}.".format(output_datalog_file))


def debug():
    print("Generating datalog for Dish")
    generate_datalog_file_dish("InputDishCleaned.csv", "DishRules.lp", "generated/cleaned/Dish.lp")
    generate_datalog_file_dish("InputDishDirty.csv", "DishRules.lp", "generated/dirty/Dish.lp")

    print("Generating datalog for MenuItem")
    generate_datalog_file_menuitem("InputMenuItemCleaned.csv", "MenuItemRules.lp", "generated/cleaned/MenuItem.lp")
    generate_datalog_file_menuitem("InputMenuItemDirty.csv", "MenuItemRules.lp", "generated/dirty/MenuItem.lp")

    print("Generating datalog for MenuPage")
    generate_datalog_file_menupage("InputMenuPageCleaned.csv", "MenuPageRules.lp", "generated/cleaned/MenuPage.lp")
    generate_datalog_file_menupage("InputMenuPageDirty.csv", "MenuPageRules.lp", "generated/dirty/MenuPage.lp")
