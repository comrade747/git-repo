# documentation here
# https://openpyxl.readthedocs.io/en/stable/usage.html

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def exercise1():
    wb = Workbook()

    # grab the active worksheet
    ws = wb.active

    ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
    # or
    ws2 = wb.create_sheet("Mysheet", 0) # insert at first position

    ws.title = "New Title"

    ws.sheet_properties.tabColor = "1072BA"

    ws3 = wb["New Title"]

    print(wb.sheetnames)

    source = wb.active
    target = wb.copy_worksheet(source)

    # Data can be assigned directly to cells
    ws['A1'] = 42
    d = ws.cell(row=4, column=2, value=10)

    # add a simple formula
    ws["A1"] = "=SUM(1, 1)"

    # Rows can also be appended
    ws.append([1, 2, 3])

    # Python types will automatically be converted
    import datetime
    ws['A2'] = datetime.datetime.now()

    cell_range = ws['A1':'C2']

    for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
       for cell in row:
           print(cell)

    for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
        for cell in col:
            print(cell)

    for row in ws.values:
       for value in row:
         print(value)

    for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
      print(row)

    # Save the file
    wb.save("sample.xlsx")


def exercise2():
    wb = Workbook()

    dest_filename = 'empty_book.xlsx'

    ws1 = wb.active
    ws1.title = "range names"

    for row in range(1, 40):
        ws1.append(range(600))

    ws2 = wb.create_sheet(title="Pi")

    ws2['F5'] = 3.14

    ws3 = wb.create_sheet(title="Data")
    for row in range(10, 20):
        for col in range(27, 54):
            _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
    print(ws3['AA10'].value)
    AA
    wb.save(filename = dest_filename)