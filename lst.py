#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Dec 2019
# This program uses a list


def avarages(mark):
    total = 0
    for counter in range(0, len(mark)):
        total += int(mark.pop())
    avarage = total / (counter+1)

    return avarage


def main():
    # this function uses a list

    mark = []
    temp_word = None

    # input
    print("Once you finished entering your marks, "
          "press -1 to calculate avarage.")

    temp_word = input("Enter a mark: ")
    mark.append(temp_word)
    while temp_word != "-1":
        temp_word = input("Enter a mark: ")
        mark.append(temp_word)
    mark.pop()  # remove the "Stop" that was added
    print("")
    caculate = avarages(mark)
    print("Your average is: {0}".format(caculate))


if __name__ == "__main__":
    main()
