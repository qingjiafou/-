from werkzeug.security import check_password_hash,generate_password_hash

user_input_password = "admin"
password_hash = generate_password_hash(user_input_password)
print(password_hash)
result = check_password_hash(password_hash, user_input_password)
print(result)  # 输出 True 或 False