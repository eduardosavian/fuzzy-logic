#!/bin/bash

# Set the path to tool.jar
tool_path="libs/jfuzzy.jar"

file_path=src/formula1.fcl

# Prompt the user for inputs
echo "Enter fuel level:"
read fuel_level

echo "Enter race position:"
read race_position

echo "Enter race progress:"
read race_progress

echo "Enter tire condition:"
read tire_condition

# Run your Java program with the specified tool.jar and user inputs
java -jar "$tool_path" -e $file_path $fuel_level $race_position $race_progress $tire_condition

# Optionally, you can store the output in a variable if you want to use it later
# output=$(java -jar "$tool_path" $fuel_level $race_position $race_progress $tire_condition)
# echo "Output: $output"
