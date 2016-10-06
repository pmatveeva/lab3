from Client import Client
from Friends import Friends

u_id = Client('id6684003').execute()
friends = Friends(u_id).execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))