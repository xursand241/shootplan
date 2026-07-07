import re

file_path = 'c:/Users/xursand/Desktop/jadvalim/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r"Kutilmoqda": r"${t('status_pending')}",
    r"Tasdiqlangan": r"${t('status_approved')}",
    r"Yakunlangan": r"${t('status_completed')}",
    r"saqlandi!": r"${t('msg_saved')}",
    r"O'chirildi": r"${t('msg_deleted')}",
    r"Xatolik yuz berdi": r"${t('msg_error')}",
    r"Muvaffaqiyatli saqlandi!": r"${t('msg_saved')}",
    r"Barcha majburiy maydonlarni to'ldiring": r"${t('msg_fill_required')}"
}

for pattern, replacement in replacements.items():
    content = content.replace(pattern, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("JS strings translated")
