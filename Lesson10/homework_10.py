import requests

registrate_user = {
  "name": "nick",
  "lastName": "lashen",
  "email": "hello65@test.com",
  "password": "Qwerty12345",
  "repeatPassword": "Qwerty12345"
}

login_user = {
  "email": "hello65@test.com",
  "password": "Qwerty12345",
  "remember": False
}

session = requests.session()

registrate_new_user = session.post("https://qauto2.forstudy.space/api/auth/signup", json=registrate_user)
login_mew_user = session.post("https://qauto2.forstudy.space/api/auth/signin", json=login_user)
get_current_user = session.get("https://qauto2.forstudy.space/api/users/profile")
print(registrate_new_user.text)
print(login_mew_user.text)
print(get_current_user.text)

