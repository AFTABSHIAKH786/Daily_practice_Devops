import re

error = "Theis is a sample error log with lots of error errors are not stoping lots and lots of error."

errors = re.search('error', error)

print(errors.group())