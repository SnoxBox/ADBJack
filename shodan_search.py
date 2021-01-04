import shodan
import sys
import os

SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

logo = '''
 ▄▄▄· ·▄▄▄▄  ▄▄▄▄·  ▐▄▄▄ ▄▄▄·  ▄▄· ▄ •▄
▐█ ▀█ ██▪ ██ ▐█ ▀█▪  ·██▐█ ▀█ ▐█ ▌▪█▌▄▌▪
▄█▀▀█ ▐█· ▐█▌▐█▀▀█▄▪▄ ██▄█▀▀█ ██ ▄▄▐▀▀▄·
▐█ ▪▐▌██. ██ ██▄▪▐█▐▌▐█▌▐█ ▪▐▌▐███▌▐█.█▌
 ▀  ▀ ▀▀▀▀▀• ·▀▀▀▀  ▀▀▀• ▀  ▀ ·▀▀▀ ·▀  ▀ \n'''

try:
    #print logo
    print(logo)

    #Take search term and save it
    user_input = "Android Debug Bridge"
    user_page_input = "1"
    shodan_query = api.search(user_input, user_page_input)


    #show the results
    f = open("ips.txt","a+")
    print('Results found: {}'.format(shodan_query['total']))
    for shodan_query in shodan_query['matches']:
        print('IP: {}'.format(shodan_query['ip_str']))
        f.write('{}\n'.format(shodan_query['ip_str']))

except shodan.APIError as e:
    print('Error: {}'.format(e))
