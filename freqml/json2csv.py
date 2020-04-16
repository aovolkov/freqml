import csv, json
def json2csv(jsonfile, csvfile):
    input = open(jsonfile)
    output = open(csvfile, 'w')
    data = json.load(input)
    input.close()
    output = csv.writer(output)
    output.writerow(data[0].keys())
    for row in data:
        output.writerow(row.values())