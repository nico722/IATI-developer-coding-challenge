import os
import csv
import re


class RowData:
    def __init__(self, row = []):
        self.project_id = str(row[0])
        self.start_date = str(row[1])
        self.total_budget_value_usd = float(row[2])

    def is_from_year(self, year):
        return self.start_date.find(str(year), 0, 4) == 0


def validate_year_format(date):
    if type(date) is not str:
        raise Exception('Date must be an str value')

    if  len(date) != 4 or re.match(r"([12]\d{3})+", date) is None:
        raise Exception('Invalid date format')

    return True


def process_file_row(row, year):
    row_data = RowData(row)
    if row_data.is_from_year(year):
        return row_data.total_budget_value_usd
    return 0


def get_total_budget_value(csv_filepath, year):
    """Compute the total USD value of projects for the input year.

    Args:
        csv_filepath (str): A path to a CSV file containing three columns: project-id; start-date; total-budget-value-usd.
        year (int): A value corresponding to a year.

    Returns:
        (float) The USD value of projects that start in the given year
    """
    total = 0
    with open(csv_filepath, 'r') as fp:
        reader = csv.reader(fp)
        for idx, row in enumerate(reader):
            if idx == 0 or row == []: # Ignore unnecesary rows (empty and column names)
                continue
            total += process_file_row(row, year)

    return total


def run():
    while(True):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        samples_filename = f"{BASE_DIR}/tests/sample_data_fully_valid_10_rows.csv"
        year = str(input('Input a year in YYYY format:\n'))
        
        try:
            validate_year_format(year)
            total = get_total_budget_value(samples_filename, year)
            print(f'The budget for the year {year} is {total}')
        except FileNotFoundError:
            print(f'{samples_filename} could not be found')
        except (Exception, AttributeError, KeyError) as e:
            print(e)

        print()

if __name__ == '__main__':
	run()