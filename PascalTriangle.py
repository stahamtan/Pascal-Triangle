from __future__ import print_function

def generate_triangle(rows=10, mode=None):
    row = list()
    row.append([1])
    row.append([1,1])

    currentNumber = int()

    for i in range(2,rows):
        aRow = [1]
        for j in range(1,i):
            currentNumber = row[i-1][j] + row[i-1][j-1]

            if mode != None:
                currentNumber = currentNumber % mode

            aRow.append(currentNumber)
        aRow.append(1)
        row.append(aRow)

    return row


def pretty_triangle_text(aTriangle):
    for aRow in aTriangle:
        print("\t".join(map(str,aRow)))

