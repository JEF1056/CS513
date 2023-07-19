import pandas as pd
import math
import os
import pathlib
import sys

filepath = pathlib.Path(__file__).parent.absolute()

print(filepath)

def generate_datalog_file_dish(inputCsvFile, rulesFile, outputDatalogFile):
    with open(os.path.join(filepath, rulesFile), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, outputDatalogFile), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, inputCsvFile))

            comment = "% Generated from {0}\n".format(inputCsvFile)
            file.write(comment)

            for _, row in df.iterrows():
                name = str(row["name"]).replace('\\', "").replace('"', "") if pd.notnull(row["name"]) else ""
                description = str(row["description"]).replace('\\', "").replace('"', "") if pd.notnull(row["description"]) else ""

                lowest_price = 0 if math.isnan(row["lowest_price"]) else int(row["lowest_price"])
                highest_price = 0 if math.isnan(row["highest_price"]) else int(row["highest_price"])

                line = "dish({0}, \"{1}\", \"{2}\", {3}, {4}, {5}, {6}, {7}, {8}).\n".format(row["id"], name, description, row["menus_appeared"], row["times_appeared"], row["first_appeared"], row["last_appeared"], lowest_price, highest_price)
                file.write(line)
            
    print("Done generating datalog file {0}.".format(outputDatalogFile))


def generate_datalog_file_menuitem(inputCsvFile, rulesFile, outputDatalogFile):
    with open(os.path.join(filepath, rulesFile), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, outputDatalogFile), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, inputCsvFile))

            comment = "% Generated from {0}\n".format(inputCsvFile)
            file.write(comment)

            for _, row in df.iterrows():
                price = 0.0 if math.isnan(row["price"]) else row["price"]
                high_price = 0.0 if math.isnan(row["high_price"]) else row["high_price"]
                dish_id = -1 if math.isnan(row["dish_id"]) else int(row["dish_id"])

                line = "menuitem({0}, {1}, \"{2}\", \"{3}\", {4}, \"{5}\", \"{6}\", \"{7}\", \"{8}\").\n".format(row["id"], row["menu_page_id"], price, high_price, dish_id, row["created_at"], row["updated_at"], row["xpos"], row["ypos"])
                file.write(line)

    print("Done generating datalog file {0}.".format(outputDatalogFile))


def generate_datalog_file_menupage(inputCsvFile, rulesFile, outputDatalogFile):
    with open(os.path.join(filepath, rulesFile), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, outputDatalogFile), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, inputCsvFile))

            comment = "% Generated from {0}\n".format(inputCsvFile)
            file.write(comment)

            for _, row in df.iterrows():
                page_number = 0 if math.isnan(row["page_number"]) else int(row["page_number"])
                full_height = 0 if math.isnan(row["full_height"]) else int(row["full_height"])
                full_width = 0 if math.isnan(row["full_width"]) else int(row["full_width"])

                line = "menupage({0}, {1}, {2}, {3}, {4}, {5}, \"{6}\").\n".format(row["id"], row["menu_id"], page_number, row["image_id"], full_height, full_width, row["uuid"])
                file.write(line)

    print("Done generating datalog file {0}.".format(outputDatalogFile))


def main():
    print("Generating datalog for Dish")
    # generate_datalog_file_dish("InputDishCleaned.csv", "DishRules.lp", "generated/Dish.lp")
    
    print("Generating datalog for MenuItem")
    generate_datalog_file_menuitem("InputMenuItemCleaned.csv", "MenuItemRules.lp", "generated/MenuItem.lp")

    print("Generating datalog for MenuPage")
    # generate_datalog_file_menupage("InputMenuPageCleaned.csv", "MenuPageRules.lp", "generated/MenuPage.lp")
    
if __name__ == "__main__":
    main()