import pandas as pd
import math
import os
import pathlib

filepath = pathlib.Path(__file__).parent.absolute()

def main():
    with open(os.path.join(filepath, "MenuPageRules.lp"), "r") as datalog_rules:
        lines = datalog_rules.readlines()

        with open(os.path.join(filepath, "MenuPage.lp"), "w+") as datalog_full:
            datalog_full.writelines(lines)

            input_file_name = 'InputMenuPage.csv'
            df = pd.read_csv(os.path.join(filepath, input_file_name))

            comment = "% Generated from {0}\n".format(input_file_name)

            datalog_full.write(comment)

            for _, row in df.iterrows():
                page_number = 0 if math.isnan(row["page_number"]) else int(row["page_number"])
                full_height = 0 if math.isnan(row["full_height"]) else int(row["full_height"])
                full_width = 0 if math.isnan(row["full_width"]) else int(row["full_width"])

                line = "menupage({0}, {1}, {2}, {3}, {4}, {5}, \"{6}\").\n".format(row["id"], row["menu_id"], page_number, row["image_id"], full_height, full_width, row["uuid"])

                datalog_full.write(line)

if __name__ == "__main__":
    main()