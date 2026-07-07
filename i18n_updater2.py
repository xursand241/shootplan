with open('c:/Users/xursand/Desktop/jadvalim/lang.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Add to uz
text = text.replace('"status_completed": "Yakunlangan"', '"status_completed": "Yakunlangan",\n        "login_pending_msg": "Hisobingiz tasdiqlanmagan. Iltimos, admin ruxsatini kuting.",\n        "admin_tab_users": "Foydalanuvchilar",\n        "btn_approve": "Tasdiqlash"')

# Add to ru
text = text.replace('"status_completed": "Завершено"', '"status_completed": "Завершено",\n        "login_pending_msg": "Ваш аккаунт не подтвержден. Дождитесь разрешения администратора.",\n        "admin_tab_users": "Пользователи",\n        "btn_approve": "Одобрить"')

# Add to en
text = text.replace('"status_completed": "Completed"', '"status_completed": "Completed",\n        "login_pending_msg": "Your account is not approved yet. Please wait for admin approval.",\n        "admin_tab_users": "Users",\n        "btn_approve": "Approve"')

with open('c:/Users/xursand/Desktop/jadvalim/lang.js', 'w', encoding='utf-8') as f:
    f.write(text)
