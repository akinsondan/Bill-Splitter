import random
friends = []
num_ppl = int(input('No of friends:\n'))
print()
if num_ppl <= 0:
    print("No one is joining for the party")
else:
    print('Enter names of friends:\n')
    for i in range(num_ppl):
        friends_name = input()
        friends.append(friends_name)
    print()
    total_bill = int(input('Enter the total bill value:\n'))
    bill = round(total_bill/num_ppl, 2)
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    print()
    if lucky_feature == 'Yes':
        lucky_one = random.choice(friends)
        new_split = num_ppl - 1
        new_bill = round(total_bill/new_split, 2)
        new_friend_dict = dict.fromkeys(friends, new_bill)
        if lucky_one in new_friend_dict:
            new_friend_dict[lucky_one] = 0
            
        print()
        print(lucky_one, 'is the lucly one')
        print()
        print(new_friend_dict)
    else:
        print()
        print('No one is going to be lucky')
        friend_dict = dict.fromkeys(friends, bill)
    
        print(friend_dict)
    #print(frnds_dict)
