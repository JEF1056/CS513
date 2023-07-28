import os
import pathlib
import re
import subprocess

filepath = pathlib.Path(__file__).parent.absolute()


def generate_model(input_file, output_model_file):
    with open(os.path.join(filepath, output_model_file), "w+") as model:
        p = subprocess.run(["clingo", "{0}".format(os.path.join(filepath, input_file)), "--models", "1", "--parallel-mode", "4"], stdout=model)


def validate_datalog_menupage(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_id_key\(\w+,\w+,\w+,\w+\)", lines)
        regex2 = re.findall("icv_id_key\(\w+,\w+,\"\w+-\w+-\w+-\w+-\w+\",\"\w+-\w+-\w+-\w+-\w+\"\)", lines)
        regex3 = re.findall("icv_id_key\(\w+,\w+,\"\d+\.\d+\",\"\d+\.\d\"\)", lines)
        regex4 = re.findall("icv_page_number\(\w+,\w+,\w+,\w+\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for MenuPage:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)


def validate_datalog_dish(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_id_key\(\w+,\w+,\w+,\w+\)", lines)
        regex2 = re.findall("icv_id_key\(\w+,\w+,\"\w+-\w+-\w+-\w+-\w+\",\"\w+-\w+-\w+-\w+-\w+\"\)", lines)
        regex3 = re.findall("icv_id_key\(\w+,\w+,\"\d+\.\d+\",\"\d+\.\d\"\)", lines)
        regex4 = re.findall("icv_id_key\(\w+,\w+,\"(?:\w+\s*)*\",\"(?:\w+\s*)*\"\)", lines)
        regex5 = re.findall("icv_menus_appeared\(\d+,\d+,\d+\)", lines)
        regex6 = re.findall("icv_times_appeared\(\d+,\d+,\d+\)", lines)
        regex7 = re.findall("icv_first_appeared\(\d+,\d+,\d+\)", lines)
        regex8 = re.findall("icv_firstappeared_lastappeared\(\d+,\d+,\d+\)", lines)
        regex9 = re.findall("icv_lowestprice_highestprice\(\d+,\d+,\d+\)", lines)
        regex10 = re.findall("icv_timesappeared_menusappeared\(\d+,\d+,\d+\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for Dish:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]
            lines5 = ["{0}\n".format(m) for m in regex5]
            lines6 = ["{0}\n".format(m) for m in regex6]
            lines7 = ["{0}\n".format(m) for m in regex7]
            lines8 = ["{0}\n".format(m) for m in regex8]
            lines9 = ["{0}\n".format(m) for m in regex9]
            lines10 = ["{0}\n".format(m) for m in regex10]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)
            violations.writelines(lines5)
            violations.writelines(lines6)
            violations.writelines(lines7)
            violations.writelines(lines8)
            violations.writelines(lines9)
            violations.writelines(lines10)


def validate_datalog_menuitem(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_id_key\(\w+,\w+,\w+,\w+\)", lines)
        regex2 = re.findall("icv_id_key\(\w+,\w+,\"\w+-\w+-\w+-\w+-\w+\",\"\w+-\w+-\w+-\w+-\w+\"\)", lines)
        regex3 = re.findall("icv_id_key\(\w+,\w+,\"\d+\.\d+\",\"\d+\.\d\"\)", lines)
        regex4 = re.findall("icv_id_key\(\w+,\w+,\"(?:\w+\s*)*\",\"(?:\w+\s*)*\"\)", lines)
        regex5 = re.findall("icv_id_key\(\d+,\w+,\"\d+-\d+-\d+\s\d+:\d+:\d+\s\w+\",\"\d+-\d+-\d+\s\d+:\d+:\d+\s\w+\"\)", lines)
        regex6 = re.findall("icv_createdat\(\d+,\"\d+-\d+-\d+\s\d+:\d+:\d+\sUTC\",\"\d+-\d+-\d+\s\d+:\d+:\d+\sUTC\"\)", lines)
        regex7 = re.findall("icv_createdat_updatedat\(\d+,\"\d+-\d+-\d+\s\d+:\d+:\d+\sUTC\",\"\d+-\d+-\d+\s\d+:\d+:\d+\sUTC\"\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for MenuItem:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]
            lines5 = ["{0}\n".format(m) for m in regex5]
            lines6 = ["{0}\n".format(m) for m in regex6]
            lines7 = ["{0}\n".format(m) for m in regex7]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)
            violations.writelines(lines5)
            violations.writelines(lines6)
            violations.writelines(lines7)


def validate_datalog_menu(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_id_key\(\w+,\w+,\w+,\w+\)", lines)
        regex2 = re.findall("icv_id_key\(\w+,\w+,\"\w+-\w+-\w+-\w+-\w+\",\"\w+-\w+-\w+-\w+-\w+\"\)", lines)
        regex3 = re.findall("icv_id_key\(\w+,\w+,\"\d+\.\d+\",\"\d+\.\d\"\)", lines)
        regex4 = re.findall("icv_id_key\(\w+,\w+,\"(?:\w+\s*)*\",\"(?:\w+\s*)*\"\)", lines)
        regex5 = re.findall("icv_id_key\(\d+,\w+,\"\d+-\d+-\d+\s\d+:\d+:\d+\s\w+\",\"\d+-\d+-\d+\s\d+:\d+:\d+\s\w+\"\)", lines)
        regex6 = re.findall("icv_pagecount\(\d+,\d+,\d+\)", lines)
        regex7 = re.findall("icv_dishcount\(\d+,\d+,\d+\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for Menu:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]
            lines5 = ["{0}\n".format(m) for m in regex5]
            lines6 = ["{0}\n".format(m) for m in regex6]
            lines7 = ["{0}\n".format(m) for m in regex7]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)
            violations.writelines(lines5)
            violations.writelines(lines6)
            violations.writelines(lines7)


def validate_datalog_combined(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_menuid_is_fk_in_menu\(-{0,1}\d+\)", lines)
        regex2 = re.findall("icv_menupageid_is_fk_in_menupage\(-{0,1}\d+\)", lines)
        regex3 = re.findall("icv_dishid_is_fk_in_menuitem\(-{0,1}\d+\)", lines)
        regex4 = re.findall("icv_dishid_in_menuitem\(-{0,1}\d+\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for Combined:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)


def main():
    generate_model("generated/dirty/Combined.lp", "generated/dirty/CombinedModel.txt")
    validate_datalog_menu("generated/dirty/CombinedModel.txt", "generated/dirty/CombinedViolations.txt")

    generate_model("generated/cleaned/Combined.lp", "generated/cleaned/CombinedModel.txt")
    validate_datalog_menu("generated/cleaned/CombinedModel.txt", "generated/cleaned/CombinedViolations.txt")

if __name__ == "__main__":
    main()
