import re

with open('c:/Users/xursand/Desktop/jadvalim/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert my bad injection
content = content.replace("${t('status_pending')}", "pending")
content = content.replace("${t('status_approved')}", "approved")
content = content.replace("${t('status_completed')}", "completed")

# Also fix the initial ones that might still be in Uzbek
content = content.replace("Kutilmoqda", "pending")
content = content.replace("Tasdiqlangan", "approved")
content = content.replace("Yakunlangan", "completed")

# Fix status CSS classes
content = content.replace(".status-tasdiqlangan", ".status-approved")
content = content.replace(".status-kutilmoqda", ".status-pending")
content = content.replace(".status-yakunlangan", ".status-completed")

# Fix rendering strings
content = content.replace("${s.status}</div>", "${t('status_' + s.status)}</div>")
content = content.replace("document.getElementById('detStatus').textContent = s.status;", "document.getElementById('detStatus').textContent = t('status_' + s.status);")

with open('c:/Users/xursand/Desktop/jadvalim/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Status logic fixed.")
