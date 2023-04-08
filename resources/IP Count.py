
# This Code write By Malek Aldossary 
import openpyxl
import ipaddress

input_file = openpyxl.load_workbook('input_file.xlsx')
input_sheet = input_file.active

output_file = openpyxl.Workbook()
output_sheet = output_file.active

output_sheet.cell(row=1, column=1, value='CIDR')
output_sheet.cell(row=1, column=2, value='IP Count')

for row in input_sheet.iter_rows(values_only=True):
    for cell in row:
        if isinstance(cell, str) and '/' in cell:
            try:
                ip_network = ipaddress.IPv4Network(cell, strict=False)
                ip_count = ip_network.num_addresses
                
                output_sheet.append([str(ip_network), ip_count])
            except ValueError:
                pass

output_file.save('output_file.xlsx')
