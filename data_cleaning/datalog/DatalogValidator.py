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

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for MenuPage:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)


def validate_datalog_dish(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_id_key\(\w+,\w+,\w+,\w+\)", lines)
        regex2 = re.findall("icv_id_key\(\w+,\w+,\"\w+-\w+-\w+-\w+-\w+\",\"\w+-\w+-\w+-\w+-\w+\"\)", lines)
        regex3 = re.findall("icv_id_key\(\w+,\w+,\"\d+\.\d+\",\"\d+\.\d\"\)", lines)
        regex4 = re.findall("icv_id_key\(\w+,\w+,\"(?:\w+\s*)*\",\"(?:\w+\s*)*\"\)", lines)
        regex5 = re.findall("icv_firstappeared_lastappeared\(\d+,\d+,\d+\)", lines)
        regex6 = re.findall("icv_lowestprice_highestprice\(\d+,\d+,\d+\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for Dish:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]
            lines5 = ["{0}\n".format(m) for m in regex5]
            lines6 = ["{0}\n".format(m) for m in regex6]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)
            violations.writelines(lines5)
            violations.writelines(lines6)


def validate_datalog_menuitem(input_model_file, output_violations_file):
    with open(os.path.join(filepath, input_model_file), "r") as model:
        lines = model.read()

        regex1 = re.findall("icv_id_key\(\w+,\w+,\w+,\w+\)", lines)
        regex2 = re.findall("icv_id_key\(\w+,\w+,\"\w+-\w+-\w+-\w+-\w+\",\"\w+-\w+-\w+-\w+-\w+\"\)", lines)
        regex3 = re.findall("icv_id_key\(\w+,\w+,\"\d+\.\d+\",\"\d+\.\d\"\)", lines)
        regex4 = re.findall("icv_id_key\(\w+,\w+,\"(?:\w+\s*)*\",\"(?:\w+\s*)*\"\)", lines)
        regex5 = re.findall("icv_id_key\(\d+,\w+,\"\d+-\d+-\d+\s\d+:\d+:\d+\s\w+\",\"\d+-\d+-\d+\s\d+:\d+:\d+\s\w+\"\)", lines)

        with open(os.path.join(filepath, output_violations_file), "w+") as violations:
            violations.write("Violated integrity constraints for MenuItem:\n")

            lines1 = ["{0}\n".format(m) for m in regex1]
            lines2 = ["{0}\n".format(m) for m in regex2]
            lines3 = ["{0}\n".format(m) for m in regex3]
            lines4 = ["{0}\n".format(m) for m in regex4]
            lines5 = ["{0}\n".format(m) for m in regex5]

            violations.writelines(lines1)
            violations.writelines(lines2)
            violations.writelines(lines3)
            violations.writelines(lines4)
            violations.writelines(lines5)


def debug():
    print("Checking integrity constraints for Dish")

    generate_model("generated/cleaned/Dish.lp", "generated/cleaned/DishModel.txt")
    validate_datalog_dish("generated/cleaned/DishModel.txt", "generated/cleaned/DishViolations.txt")

    generate_model("generated/dirty/Dish.lp", "generated/dirty/DishModel.txt")
    validate_datalog_dish("generated/dirty/DishModel.txt", "generated/dirty/DishViolations.txt")

    print("Checking integrity constraints for MenuItem")
    generate_model("generated/cleaned/MenuItem.lp", "generated/cleaned/MenuItemModel.txt")
    validate_datalog_menuitem("generated/cleaned/MenuItemModel.txt", "generated/cleaned/MenuItemViolations.txt")

    generate_model("generated/dirty/MenuItem.lp", "generated/dirty/MenuItemModel.txt")
    validate_datalog_menuitem("generated/dirty/MenuItemModel.txt", "generated/dirty/MenuItemViolations.txt")

    print("Checking integrity constaints for MenuPage")
    generate_model("generated/cleaned/MenuPage.lp", "generated/cleaned/MenuPageModel.txt")
    validate_datalog_menupage("generated/cleaned/MenuPageModel.txt", "generated/cleaned/MenuPageViolations.txt")

    generate_model("generated/dirty/MenuPage.lp", "generated/dirty/MenuPageModel.txt")
    validate_datalog_menupage("generated/dirty/MenuPageModel.txt", "generated/dirty/MenuPageViolations.txt")