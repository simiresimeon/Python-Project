# Author: Simire Simeon Obamiegie
# Course: CSE110


# Creativity:
# In addition to the required analysis, i added a function to the program that allows users to enter a country name
# and view its minimum, maximum, and average life expectancy across all years.

# Load the dataset
filename = "life-expectancy.csv"

# Initialize tracking variables
lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')
lowest_record = {}
highest_record = {}

data_by_year = {}
data_by_country = {}

with open("life-expectancy.csv") as file:
    header = file.readline()  # Skip header line

    for line in file:
        parts = line.strip().split(',')
        if len(parts) != 3:
            continue  # Skip malformed lines

        country = parts[0]
        year = int(parts[1])
        life_expectancy = float(parts[2])

        # Track overall min and max
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            lowest_record = {'country': country, 'year': year, 'value': life_expectancy}

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            highest_record = {'country': country, 'year': year, 'value': life_expectancy}

        # Organize data by year
        if year not in data_by_year:
            data_by_year[year] = []
        data_by_year[year].append((country, life_expectancy))

        # Organize data by country
        if country not in data_by_country:
            data_by_country[country] = []
        data_by_country[country].append(life_expectancy)

# Display overall min and max
print(f"The overall max life expectancy is: {highest_record['value']} from {highest_record['country']} in {highest_record['year']}")
print(f"The overall min life expectancy is: {lowest_record['value']} from {lowest_record['country']} in {lowest_record['year']}")

# Prompt user for year
year_of_interest = int(input("\nEnter the year of interest: "))

if year_of_interest in data_by_year:
    year_data = data_by_year[year_of_interest]
    total = sum([entry[1] for entry in year_data])
    average = total / len(year_data)
    max_entry = max(year_data, key=lambda x: x[1])
    min_entry = min(year_data, key=lambda x: x[1])

    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {max_entry[0]} with {max_entry[1]}")
    print(f"The min life expectancy was in {min_entry[0]} with {min_entry[1]}")
else:
    print(f"No data available for the year {year_of_interest}")

# prompt user for country
country_of_interest = input("\nEnter a country to explore its life expectancy stats: ").strip()

if country_of_interest in data_by_country:
    country_data = data_by_country[country_of_interest]
    min_val = min(country_data)
    max_val = max(country_data)
    avg_val = sum(country_data) / len(country_data)

    print(f"\nFor {country_of_interest}:")
    print(f"Minimum life expectancy: {min_val}")
    print(f"Maximum life expectancy: {max_val}")
    print(f"Average life expectancy: {avg_val:.2f}")
else:
    print(f"No data available for {country_of_interest}")



