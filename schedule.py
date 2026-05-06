import csv
from schedule_item import ScheduleItem

class Schedule:
    def __init__(self):
        self.schedule_dict = {}

    def add_entry(self, item: ScheduleItem):
        key = item.get_key()
        self.schedule_dict[key] = item

    def print_header(self):
        print(f"{'Subject':<6} {'Catalog':<7} {'Section':<8} {'Component':<10} "
              f"{'Session':<8} {'Units':<5} {'TotEnrl':<8} {'CapEnrl':<8} Instructor")