class Garden(object):
    """Create a kindergarten class garden."""

    default_students = [
                'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
                ]

    def __init__(self, diagram, students=default_students):
        """Find student's row of plants."""
        self.students = sorted(students)
        self.diagram = diagram

    def plants(self, student):
        """Get plants."""
        output = []
        plant_dict = {
            'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'
            }
        rows = self.diagram.split('\n')
        rows[0] = [rows[0][x:x+2] for x in range(0, len(rows[0]), 2)]
        rows[1] = [rows[1][x:x+2] for x in range(0, len(rows[1]), 2)]
        relevant_index = self.students.index(student)
        output.append(plant_dict.get(rows[0][relevant_index][0]))
        output.append(plant_dict.get(rows[0][relevant_index][1]))
        output.append(plant_dict.get(rows[1][relevant_index][0]))
        output.append(plant_dict.get(rows[1][relevant_index][1]))

        return output
