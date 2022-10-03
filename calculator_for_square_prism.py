#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: Oct. 03, 2022
# This program asks the user for the base edge (a)
# and the height of a square prism. It then calculates
# and displays the Volume and Surface Area in cm


def main():
    # input, base edge changed under style rules. Over 79 characters
    print("\33[31mSquare Prism Calculator")
    unit = str(input("Enter the units you will be using: "))
    print("")
    base_edge = float(
        input(
            "\33[33mEnter the base edge (a) of the square prism in {}".format(unit)
            + ": "
        )
    )
    height = float(
        input("Enter the height (h) of the square prism in {}".format(unit) + ": ")
    )

    # process
    volume = base_edge**2 * height
    surface_area = 2 * base_edge**2 + 4 * base_edge * height

    # output, placed + for "strings" or else it won't work
    print("")
    print(
        "\33[32mThe volume of the square prism is = {:,.2f}".format(volume)
        + " "
        + (unit)
        + "³"
    )
    print(
        "The surface area of the square prism is = {:,.2f}".format(surface_area)
        + " "
        + (unit)
        + "²"
    )


if __name__ == "__main__":
    main()
