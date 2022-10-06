import csv


class BaseCsvReader:
    def read(csvFile: str) -> dict[str, list[any]]:
        with open(csvFile) as file:
            reader = csv.reader(file, delimiter=',')
            return list(reader)


class ColumnCsvReader(BaseCsvReader):
    def read(csvFile: str) -> dict[str, list[any]]:
        with open(csvFile) as file:
            reader = csv.reader(file, delimiter=',')
            labels = next(reader)

            data = {}

            for label in labels:
                data.update({label: []})

            for row in reader:
                for key, i in zip(data.keys(), range(0, len(labels))):
                    data[key].append(row[i])

            return data
