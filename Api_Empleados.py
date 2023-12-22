import requests

# Hacer la solicitud GET a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    data = response.json()

    # Obtener la lista de empleados
    employees = data["data"]

    # Obtener el número total de empleados
    total_employees = len(employees)

    # Calcular el promedio de salario
    total_salary = sum(float(employee["employee_salary"]) for employee in employees)
    average_salary = total_salary / total_employees

    # Calcular el promedio de edad
    total_age = sum(int(employee["employee_age"]) for employee in employees)
    average_age = total_age / total_employees

    # Encontrar salario mínimo y máximo
    salaries = [float(employee["employee_salary"]) for employee in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)

    # Encontrar edad mínima y máxima
    ages = [int(employee["employee_age"]) for employee in employees]
    min_age = min(ages)
    max_age = max(ages)

    # Mostrar los resultados
    print(f"Número total de empleados: {total_employees}")
    print(f"Promedio de salario: {average_salary}")
    print(f"Promedio de edad: {average_age}")
    print(f"Salario mínimo: {min_salary}")
    print(f"Salario máximo: {max_salary}")
    print(f"Edad mínima: {min_age}")
    print(f"Edad máxima: {max_age}")

else:
    print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")