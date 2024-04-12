import itertools

# Define the fuzzy sets
tire_condition_values = {
    'degraded': 100, 'light_damage': 50, 'competitive': 0, 'optimal': -50, 'prime_performance': -100,
}

fuel_level_values = {
    'low': 40, 'half': 0, 'full': -50,
}

race_progress_values = {'start': 0, 'middle': -10, 'end': -50, 'final_stretch': -100}

race_position_values = {'excellent': 0, 'good': 30, 'poor': 60}

# Define the output terms
output_terms = {
    'all_ok': (-1000, 20),
    'can_wait': (20, 50),
    'high_risk': (50, 80),
    'urgent': (80, 1000),
}

# Generate combinations of inputs
inputs_combinations = list(itertools.product(tire_condition_values, fuel_level_values, race_progress_values, race_position_values))

# Store the rules in a list
rules = []
for i, combination in enumerate(inputs_combinations, start=1):
    tire_condition, fuel_level, race_progress, race_position = combination

    urgency = tire_condition_values[tire_condition] + fuel_level_values[fuel_level] + race_progress_values[race_progress] + race_position_values[race_position]
    for name, urange in output_terms.items():
        if urange[0] <= urgency < urange[1]:
            urgency_label = name
            break

    # Create rule statement
    rule = f"RULE {i} : IF (tire_condition IS {tire_condition}) AND (fuel_level IS {fuel_level}) AND (race_progress IS {race_progress}) AND (race_position IS {race_position}) THEN pitstop_necessity IS {urgency_label};\n"
    rules.append(rule)

# Write the rules to the file
with open('template/rules.txt', 'w') as file:
    file.write("RULEBLOCK first\n\n")
    file.writelines(rules)
    file.write("\nEND_RULEBLOCK\n")

print("Rules have been written to rules.txt file.")

# Read the head from head.txt
with open('template/head.txt', 'r') as head_file:
    head_content = head_file.read()

# Read the tail from tail.txt
with open('template/tail.txt', 'r') as tail_file:
    tail_content = tail_file.read()

# Write head, rules, and tail to formula1.fcl
with open('formula1.fcl', 'w') as fcl_file:
    fcl_file.write(head_content)  # Write head content
    fcl_file.write('\n\n')  # Write a blank line
    fcl_file.writelines(rules)  # Write rules content
    fcl_file.write('\n\n')  # Write a blank line
    fcl_file.write(tail_content)  # Write tail content

print("Head, rules, and tail have been written to formula1.fcl.")
