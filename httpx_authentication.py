import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "kate@example.com",
    "password": "11011991"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response_data)

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Формируем payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)

#Доп задание 6.1
# # Данные для входа в систему
# login_payload = {
#     "email": "kate@example.com",
#     "password": "11011991"
# }
#
# # Выполняем запрос на аутентификацию
# login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
# login_response_data = login_response.json()
# access_token = login_response_data["token"]["accessToken"]
#
# get_user_headers = {"Authorization": f"Bearer {access_token}"}
# print(get_user_headers)
# print(login_response.status_code)
# get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)
# get_user_response_data = get_user_response.json()
# print("Get user response:", get_user_response_data)
# print("Get user status code:", get_user_response.status_code)

