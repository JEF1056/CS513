import pandas as pd
import math
import os
import pathlib

filepath = pathlib.Path(__file__).parent.absolute()

def main():
    # Read datalog rules from existing file
    with open(os.path.join(filepath, "MenuPageRules.lp"), "r") as datalog_rules:
        lines = datalog_rules.readlines()

        # Create new file to store datalog rules and facts
        with open(os.path.join(filepath, "MenuPage.lp"), "w+") as datalog_full:
            datalog_full.writelines(lines)

            # Read input data from csv
            df = pd.read_csv(os.path.join(filepath, 'InputMenuPage.csv'))

            for _, row in df.iterrows():
                full_height = 0 if math.isnan(row["full_height"]) else int(row["full_height"])
                full_width = 0 if math.isnan(row["full_width"]) else int(row["full_width"])
                page_number = 0 if math.isnan(row["page_number"]) else int(row["page_number"])

                mystr = "menupage({0}, {1}, {2}, {3}, {4}, {5}, \"{6}\").\n".format(row["id"], row["menu_id"], page_number, row["image_id"], full_height, full_width, row["uuid"])

                datalog_full.write(mystr)

if __name__ == "__main__":
    main()