class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]
        return self.lines

    def count(self):
        return len(self.lines)




lc = LineCounter('example_log.txt')
# print(lc.read())
# print(lc.count())


# functional programming functions are stateless and rely only on their given inputs to produce an output.
# no side effects
# pure function:
def pure_func_sum(a,b):
    return a+b

#impure
#side effects occur when changes inside function are outside of its scope
A = 1
def impure_fun(b):
    return A+b



lines = lc.read()

print(lines.map(lambda l: l.split("\n")))

line = [l for l in lines]
print(line)
# sorted = sorted(lines, key= lambda x:x.split(' '))
#
# print(sorted)


def open_dataset(file_name):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    return data


def sum_and_diff(a, b):
    sum=a+b
    diff=a-b
    return sum, diff #return a tuple
#if want to return a list => return [sum, diff]



test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]
words: "buttface"


def append_to_str(s1, s2):
    s = s1.