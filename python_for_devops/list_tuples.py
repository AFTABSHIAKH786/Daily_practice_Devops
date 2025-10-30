admins = ('Jhon', 'Lynda', 'Grey')

s3_buckets = ['Jhon_bucket', 'Lynda_bucket']

grey_bucket = 'Grey_bucket'

s3_buckets.append(grey_bucket);

print(s3_buckets)

### So with this example we can use list and tuples in real life scenrios for s3 we can create and delete the components but there should be only defined number of admins in the orgs so the values that are not need to be manipulated frequently they should be used in a tuple. 

s3_buckets.remove(grey_bucket)

print(s3_buckets)