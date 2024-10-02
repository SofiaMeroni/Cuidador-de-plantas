input_file = 'tabla_completa.md'
output_file = 'tabla_datos.csv'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    for line in infile:   
        columns = line.strip().split('|')
        columns = [col.strip() for col in columns if col.strip()] 
        if len(columns) > 1: 
            outfile.write(','.join(columns) + '\n')

#Aqui toma la carpeta "tabla_completa.md" para luego convertirla en un .csv, eliminando espacios y cualquier otro caracter, dejando solo comas