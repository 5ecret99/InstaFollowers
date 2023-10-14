import json

followers = open('followers_1.json')
followers_data = json.load(followers)

followers_set = set()
for acount in followers_data:
    followers_set.add(acount['string_list_data'][0]['value'])

following = open('following.json')
following_data = json.load(following)['relationships_following']

print("Number of followers: ", len(followers_data), end = '\n' )
print("Number of following: ", len(following_data), end = '\n' )

unfollowers_count = 0
print("Unfollowers acounts: ", end = '\n' )
for acount in following_data:
    if acount['string_list_data'][0]['value'] not in followers_set:
        print(acount['string_list_data'][0]['value'], end = ' -------> ')
        print(acount['string_list_data'][0]['href'], end = '\n')
        unfollowers_count+=1

print("Number of unfollowers: ", unfollowers_count, end = '\n' )
followers.close();
following.close();

