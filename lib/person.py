#!/usr/bin/env python3

class Person:
    approved_jobs = ["Sales", "Engineer", "Doctor", "ITC"]

    def __init__(self, name="", job=""):
        self.name = name  # This will call the name setter
        self.job = job    # This will call the job setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Ensure invalid value is not saved
        else:
            self._name = value.title()  # Convert to title case if valid

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
            self._job = None  # Ensure invalid value is not saved
        else:
            self._job = value
