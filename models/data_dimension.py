class DataDimension:
    def __init__(self, data_key, year, month_num, month_full, month_abbr, quarter_num,
                 quarter_full, quarter_abbr, year_and_quarter_num, quarter_abbr_and_year,
                 month_abbr_and_year, month_and_year, month_name, month_name_abbr,
                 quarter_and_year, quarter_and_year_abbr2, year_and_month_num):
        self.data_key = data_key
        self.year = year
        self.month_num = month_num
        self.month_full = month_full
        self.month_abbr = month_abbr
        self.quarter_num = quarter_num
        self.quarter_full = quarter_full
        self.quarter_abbr = quarter_abbr
        self.year_and_quarter_num = year_and_quarter_num
        self.quarter_abbr_and_year = quarter_abbr_and_year
        self.month_abbr_and_year = month_abbr_and_year
        self.month_and_year = month_and_year
        self.month_name = month_name
        self.month_name_abbr = month_name_abbr
        self.quarter_and_year = quarter_and_year
        self.quarter_and_year_abbr2 = quarter_and_year_abbr2
        self.year_and_month_num = year_and_month_num

