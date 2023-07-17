import pandas as pd
import math
import os
import pathlib

filepath = pathlib.Path(__file__).parent.absolute()

# id,name,description,menus_appeared,times_appeared,first_appeared,last_appeared,lowest_price,highest_price
# 1,"Consomme, Printaniere Royal",Consomme Printaniere Royal,8,8,1897,1927,0.2,0.4

def main():
    with open(os.path.join(filepath, "DishRules.lp"), "r") as datalog_rules:
        lines = datalog_rules.readlines()

        output_file_name = "generated/Dish.lp"

        with open(os.path.join(filepath, output_file_name), "w+") as datalog_full:
            datalog_full.writelines(lines)

            input_file_name = 'InputDishCleaned.csv'
            df = pd.read_csv(os.path.join(filepath, input_file_name))

            comment = "% Generated from {0}\n".format(input_file_name)

            datalog_full.write(comment)

            for _, row in df.iterrows():
                lowest_price = 0.0 if math.isnan(row["lowest_price"]) else int(row["lowest_price"])
                highest_price = 0.0 if math.isnan(row["highest_price"]) else int(row["highest_price"])

                name = str(row["name"]).replace('\\', "").replace('"', "") if pd.notnull(row["name"]) else ""
                description = str(row["description"]).replace('\\', "").replace('"', "") if pd.notnull(row["description"]) else ""

                line = "dish({0}, \"{1}\", \"{2}\", {3}, {4}, {5}, {6}, \"{7}\", \"{8}\").\n".format(row["id"], name, description, row["menus_appeared"], row["times_appeared"], row["first_appeared"], row["last_appeared"], lowest_price, highest_price)

                datalog_full.write(line)

        print("Done generating datalog file {0}.".format(output_file_name))

if __name__ == "__main__":
    main()