def get_valid_date(prompt, year_range=(1920, 2025)):
    while True:
        try:
            date_str = input(prompt)
            year, month, day = map(int, date_str.split('-'))
            if not (1 <= month <= 12):
                raise ValueError("Invalid month.")
            if not (1 <= day <= 31):
                raise ValueError("Invalid day.")
            if not (year_range[0] <= year <= year_range[1]):
                raise ValueError("Year out of range.")
            return date_str
        except ValueError as e:
            print(f"Error: {e}")

def get_valid_input(prompt, valid_options):
    while True:
        value = input(prompt).strip().upper()
        if value in valid_options:
            return value
        print(f"Invalid input. Expected one of {valid_options}.")
