#!/bin/bash

# Set the path to tool.jar
tool_path="tools/jfuzzy.jar"

# Run your Java program with the specified tool.jar and file argument
java -jar "$tool_path" $*