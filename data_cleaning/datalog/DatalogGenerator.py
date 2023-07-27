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


def generate_datalog_file_menu(input_csv_file, rules_file, output_datalog_file):
    with open(os.path.join(filepath, rules_file), "r") as rules:
        lines = rules.readlines()

        with open(os.path.join(filepath, output_datalog_file), "w+") as file:
            file.writelines(lines)

            df = pd.read_csv(os.path.join(filepath, input_csv_file))

            comment = "% Generated from {0}\n".format(input_csv_file)
            file.write(comment)

            for _, row in df.iterrows():
                name = row["name"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["name"]) else ""
                sponsor = row["sponsor"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["sponsor"]) else ""
                event = row["event"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["event"]) else ""
                venue = row["venue"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["venue"]) else ""
                
                if set(["venue_1", "venue_2", "venue_3"]).issubset(df.columns):
                    venue_1 = row["venue_1"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["venue_1"]) else ""
                    venue_2 = row["venue_2"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["venue_2"]) else ""
                    venue_3 = row["venue_3"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["venue_3"]) else ""

                    merged_venue = ";".join((venue, venue_1, venue_2, venue_3))
                else:
                    merged_venue = venue
                
                place = row["place"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["place"]) else ""
                physical_description = row["physical_description"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description"]) else ""
                
                if set(["physical_description_1", "physical_description_2", "physical_description_3", "physical_description_4", "physical_description_5", "physical_description_6"]).issubset(df.columns):
                    pd_1 = row["physical_description_1"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description_1"]) else ""
                    pd_2 = row["physical_description_2"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description_2"]) else ""
                    pd_3 = row["physical_description_3"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description_3"]) else ""
                    pd_4 = row["physical_description_4"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description_4"]) else ""
                    pd_5 = row["physical_description_5"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description_5"]) else ""
                    pd_6 = row["physical_description_6"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["physical_description_6"]) else ""

                    merged_physical_description = ";".join((physical_description, pd_1, pd_2, pd_3, pd_4, pd_5, pd_6))
                else:
                    merged_physical_description = physical_description

                occasion = row["occasion"] = row["occasion"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["occasion"]) else ""
                notes = row["notes"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes"]) else ""

                if set(["notes_1", "notes_2", "notes_3", "notes_4", "notes_5", "notes_6", "notes_7", "notes_8", "notes_9", "notes_10",
                        "notes_11", "notes_12", "notes_13", "notes_14", "notes_15", "notes_16", "notes_17", "notes_18", "notes_19"]).issubset(df.columns):
                    n_1 = row["notes_1"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_1"]) else ""
                    n_2 = row["notes_2"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_2"]) else ""
                    n_3 = row["notes_3"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_3"]) else ""
                    n_4 = row["notes_4"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_4"]) else ""
                    n_5 = row["notes_5"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_5"]) else ""
                    n_6 = row["notes_6"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_6"]) else ""
                    n_7 = row["notes_7"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_7"]) else ""
                    n_8 = row["notes_8"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_8"]) else ""
                    n_9 = row["notes_9"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_9"]) else ""
                    n_10 = row["notes_10"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_10"]) else ""
                    n_11 = row["notes_11"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_11"]) else ""
                    n_12 = row["notes_12"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_12"]) else ""
                    n_13 = row["notes_13"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_13"]) else ""
                    n_14 = row["notes_14"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_14"]) else ""
                    n_15 = row["notes_15"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_15"]) else ""
                    n_16 = row["notes_16"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_16"]) else ""
                    n_17 = row["notes_17"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_17"]) else ""
                    n_18 = row["notes_18"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_18"]) else ""
                    n_19 = row["notes_19"].replace('\\', "").replace('"', "").replace('\n', "").replace(r'\s{2,}', "") if pd.notnull(row["notes_19"]) else ""

                    merged_notes= ";".join((notes, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10, n_11, n_12, n_13, n_14, n_15, n_16, n_17, n_18, n_19))
                else:
                    merged_notes = notes

                call_number = row["call_number"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["call_number"]) else ""
                
                keywords = row["keywords"].replace('\\', "").replace('"', "").replace('\n', "") if set(["keywords"]).issubset(df.columns) and pd.notnull(row["keywords"]) else ""
                language = row["language"].replace('\\', "").replace('"', "").replace('\n', "") if set(["language"]).issubset(df.columns) and pd.notnull(row["language"]) else ""
                date = row["date"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["date"]) else ""
                location = row["location"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["location"]) else ""
                location_type = row["location_type"].replace('\\', "").replace('"', "").replace('\n', "") if set(["location_type"]).issubset(df.columns) and pd.notnull(row["location_type"]) else ""
                currency = row["currency"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["currency"]) else ""
                currency_symbol = row["currency_symbol"].replace('\\', "").replace('"', "").replace('\n', "") if pd.notnull(row["currency_symbol"]) else ""
                status = row["status"].replace('\\', "").replace('"', "").replace('\n', "")  if pd.notnull(row["status"]) else ""
                page_count = 0 if math.isnan(row["page_count"]) else row["page_count"]
                dish_count = 0 if math.isnan(row["dish_count"]) else row["dish_count"]

                line = "menu({0}, \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{9}\", \"{10}\", \"{11}\", \"{12}\", \"{13}\", \"{14}\", \"{15}\", \"{16}\", \"{17}\", {18}, {19}).".format(
                    row["id"], name, sponsor, event, merged_venue, place, merged_physical_description, occasion, merged_notes, call_number, keywords, language,
                    date, location, location_type, currency, currency_symbol, status, page_count, dish_count
                )
                file.write(line)

    print("Done generating datalog file {0}.".format(output_datalog_file))


def main():
    generate_datalog_file_menu("InputMenuDirty.csv", "MenuRules.lp", "generated/dirty/Menu.lp")
    generate_datalog_file_menu("InputMenuCleaned.csv", "MenuRules.lp", "generated/cleaned/Menu.lp")

if __name__ == "__main__":
    main()
