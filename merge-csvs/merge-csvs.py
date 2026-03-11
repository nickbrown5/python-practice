import csv

# function to merge multiple CSV files
def merge_csvs(inFiles, outFile):
    columns = []
    for file in inFiles:
        with open(file, 'r') as input_file:
            field = csv.DictReader(input_file).fieldnames
            columns.extend(f for f in field if f not in columns)

    with open(outFile, 'w') as output_file:
        writer = csv.DictWriter(output_file, fieldnames = columns)
        writer.writeheader()
        for file in inFiles:
            with open(file, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    writer.writerow(row)

if __name__ == '__main__':
    # pass list of input files and output file, output being last
    merge_csvs(['input1.csv', 'input2.csv'], 'output.csv')
    """ output
        Tony,61,51,
        Nick,98,91,
        Keith,85,73,
        Alice,52,79,87
        Steve,84,77,53
        Ralph,82,91,83
    """