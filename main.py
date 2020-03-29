import json
import requests
def login(session,url,username,password):
    login_url = url + '/auth/login'
    body = {'email':username,'passwd':password}
    session.post(login_url,data=body)
def report(session,url):
    url = url + '/user/checkin'
    print(json.loads(session.post(url).text))

def main():
    base_url = input('url:')
    email = input('email:')
    password = input('password:')
    session = requests.Session()
    login(session,base_url,email,password)
    report(session,base_url)
if __name__ == '__main__':
    main()