def load_data():
  """
  Load student data from CSV file and returns it as a list of dictionaries
  """
  student = []
  try:
    with open("data/science.csv", "r") as file:
      line = file.readlines()[1:]
      for line in lines:
        name, math, science, english = line.strip().split(",")
        students.append({
          "name": name,
          "math": int(math),
          "science": int(science),
          "english": int(english)
        })
  except FileNotFoundError:
    print("File not found. Please Check the file path")
  except Exeception as e:
    print("An error occured", e)
  return students
  

def calculate_average(student):
  """
  calculates average score for a single student
  """
  total = students["math"] + students["science"] + student["english"]
  return = total/3

def main():
  students = load_data()
  if not students:
    print("No data available")
    return
  print("student Average Scores")
  print("_"*30)
  for student in students:
    avg_score = calculate_average(student)
    print(f'{student["name"]}:{avg_score:.2f}')

if _name_ == "_main_":
  main()
