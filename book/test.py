# class SecretString:
#  """A not-at-all secure way to store a secret string."""
#  def __init__(self, plain_string, pass_phrase):
#      self.__plain_string = plain_string
#      self.__pass_phrase = pass_phrase
#
#  def decrypt(self, pass_phrase):
#     """Only show the string if the pass_phrase is correct."""
#     if pass_phrase == self.__pass_phrase:
#         return self.__plain_string
#     else:
#         return ""
#
# secret_string = SecretString("butt", "sex")
# print(secret_string) #nobody can access our plain_string attribute without the passphrase,
# #When we use a double underscore, the property is prefixed with _<classname>
# print(secret_string._SecretString__plain_string)
#


from tabulate import tabulate
a = ['year', 'salary']
b = [[i+1, 60000*(1.1**i)] for i in range(10)]
print(tabulate(b, a))

def inc(num):
    res = []
    for i in range(10):
       res.append(num*(1.1 ** i))
    return res
print(tabulate(inc(60), a))


# def calSalary(startSal, percentIncrease, numOfYears):
#     for yr in numOfYears:
#         newYearlySalary = startSal + startSal * percentIncrease
#         print(f'{year}: {startSal}')
#
