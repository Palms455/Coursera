import requests
import json

def calc_age(user_name):

    link_user = 'https://api.vk.com/method/users.get'
    parameter = {'v': '5.71',
                'access_token': '370382ac370382ac370382ac4b376dd65933703370382ac6ae73c1630972c2481a1852b',
                'user_ids': user_name,
                }
    r = requests.get(link_user, params = parameter)
    user_id = r.json()['response'][0]['id']
    
    
    
    link_friend = 'https://api.vk.com/method/friends.get'
    parameter1 = {'v': '5.71',
                'access_token': '370382ac370382ac370382ac4b376dd65933703370382ac6ae73c1630972c2481a1852b',
                'user_id': user_id,
                'fields': 'bdate'
                }

    get_friend = requests.get(link_friend, params = parameter1)
    new_list = []
    dic = {}

    friend_list = get_friend.json()['response']['items']
    for i in friend_list:
        if 'bdate' in i:
            d = i['bdate'].split('.')
            if len(d) == 3:
                years = 2019 - int(d[2])
                if years not in dic:
                    dic[years] = 1
                else:
                    dic[years] +=1
    friend_list = []
    for j in dic:    
        friend_list.append((j , dic[j]) )
    friend_list = sorted(friend_list, key=lambda x: x[0], reverse = False)    
    friend_list = sorted(friend_list, key=lambda x: x[1], reverse = True)
    return friend_list


if __name__ == '__main__':
    res = calc_age('insmile_sterlitamak')
    print(res)