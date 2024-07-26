import tabula
import csv
from os import listdir
from tqdm import tqdm


fees = []
data = []


class PDFtoCSV:
    def __init__(self, path: str) -> None:
        self.write(path)
        self.cleanup()

    def write(self, path: str):
        # _ = 1
        for i in tqdm(
            range(1, 31),
            desc="Reading / Wiritng",
            ascii=False,
            ncols=75,
            delay=0,
            colour="red",
        ):
            if i <= 30:
                df = tabula.read_pdf(path, pages=i)  # address of pdf file
                df[0].to_csv(f"matrix/comedk_matrix{i}.csv")
            # _ += 1

        # print("-" * 50 + "\nOperation Done!")
        # print("-" * 50 + "\n\n")

    def cleanup(self):
        # for file in listdir("matrix"):
        for i in tqdm(
            range(0, len(listdir("matrix"))),
            desc="Cleaning Up",
            ascii=False,
            ncols=75,
            delay=0.5,
            colour="blue",
        ):
            fullpath = f"matrix/{listdir('matrix')[i]}"

            filecontent = []

            readfile = open(fullpath, "r")
            reader = csv.reader(readfile)

            for contnet in reader:
                filecontent.append(contnet)

            _ = list(reversed(filecontent))
            _.pop()
            _.pop()
            filecontent = list(reversed(_)).copy()

            readfile.close()

            writefile = open(fullpath, "w")
            writer = csv.writer(writefile)

            writer.writerows(filecontent)

        # print("Cleaning Done")


class csvReader:
    def __init__(self, path: str) -> None:
        self.path = path
        self.lines = 0
        self.file = open(self.path, mode="r")

    def read(self):
        self.reader = csv.reader(self.file)

    def parse(self, subject: str):
        self.avg = 0
        for content in self.reader:
            if content != [] and len(content) >= 9:
                self.lines += 1
                if subject.upper() in content[3].upper():
                    data.append(content)
                    # try:
                    #     content[9] = content[9].replace(",", "_")
                    #     content[9] = content[9].removesuffix(".00")
                    #     fees.append(int(content[9]))

                    # except IndexError:
                    #     print(self.lines)

    def writepdf(self, file: str = ""):
        

    def close(self):
        self.file.close()


# pdfcsv = PDFtoCSV("comedk_matrix.pdf")

if __name__ == "__main__":
    for i in listdir("matrix"):
        fullpath = f"matrix/{i}"
        csvRead = csvReader(fullpath)

        csvRead.read()
        csvRead.parse("Computer Science")

        csvRead.close()

    print(data)


