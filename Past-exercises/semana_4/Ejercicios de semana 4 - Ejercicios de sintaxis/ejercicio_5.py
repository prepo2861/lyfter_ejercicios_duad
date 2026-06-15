"""
5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas.

"""

def calculate_grades():
    try:
        total_grades = int(input("Enter the number of grades:  "))

        if total_grades < 0:
            raise ValueError("You cannot enter a value less than 0")
        
        grades = []

        # We ask for the grades
        for i in range(total_grades):
            grade = float(input(f"Enter grade number {i+1}:  "))
            if grade < 0:
                raise ValueError("Grades must be greater than 0")
            grades.append(grade) 

        # We separate approved grades from failed ones using lists
        approved = [n for n in grades if n >= 70]
        failed = [n for n in grades if n < 70]

        # We get the counts 
        approved_count = len(approved)  # With len we get the number of grades in the list 
        failed_count = len(failed)

        # We calculate the averages
        # With sum we get the sum of all elements in the list
        overall_average = sum(grades) / len(grades) if grades else 0  # We use if grades else 0 so the program doesn't crash. If the list has values, perform the process. If not, show 0
        approved_average = sum(approved) / len(approved) if approved else 0
        failed_average = sum(failed) / len(failed) if failed else 0

        # Results
        print("===========================================")
        print(f"Approved grades: {approved_count}")
        print(f"Approved average: {approved_average:.2f}")
        print(f"Failed grades: {failed_count}")
        print(f"Failed average: {failed_average:.2f}")
        print(f"Overall average: {overall_average:.2f}")
        print("===========================================")
    except ValueError as e:
        print("Error:", e)

# Run
calculate_grades()
