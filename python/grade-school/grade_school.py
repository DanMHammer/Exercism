class School(object):
    def __init__(self, name):
        """Initialize school."""
        self.records = {}

    def add(self, student, grade):
        """Add student."""
        self.records[student] = grade

    def sort(self):
        """Sort student records."""
        sorted_keys = set()
        sorted_list = []
        for k, v in self.records.items():
            sorted_keys.add(v)

        for key in sorted_keys:
            sorted_list.append((key, self.grade(key)))

        return sorted_list

    def grade(self, number):
        """Return all students in grade."""
        output = []
        for k, v in self.records.items():
            if v == number:
                output.append(k)
        return output
