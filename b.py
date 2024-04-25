from flask import Flask, render_template
import openpyxl

app = Flask(__name__)


# Функция для чтения данных из файла Excel
def get_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []

    for row in sheet.iter_rows(values_only=True):
        date, grade, subject = row[:3]  # Предполагается, что дата и оценка идут первыми двумя столбцами
        data.append((date, grade, subject))

    return data


@app.route('/')
def index():
    file_path = 'grades.xlsx'  # Путь к файлу Excel с оценками и датами
    data = get_data_from_excel(file_path)

    return render_template('ww.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
