import re
import os

files = {
    'index.html': 'c:/Users/xursand/Desktop/jadvalim/index.html',
    'login.html': 'c:/Users/xursand/Desktop/jadvalim/login.html',
    'admin.html': 'c:/Users/xursand/Desktop/jadvalim/admin.html'
}

replacements = {
    # Navigatsiya
    r'<span class="nav-text">Asosiy</span>': r'<span class="nav-text" data-i18n="nav_home">Asosiy</span>',
    r'<span class="nav-text">Jadval</span>': r'<span class="nav-text" data-i18n="nav_calendar">Jadval</span>',
    r'<span class="nav-text">Mijozlar</span>': r'<span class="nav-text" data-i18n="nav_clients">Mijozlar</span>',
    r'<span class="nav-text">Profil</span>': r'<span class="nav-text" data-i18n="nav_profile">Profil</span>',
    
    # Filterlar
    r'<div class="pill active" onclick="setFilter\(\'Barchasi\'\)">Barchasi</div>': r'<div class="pill active" onclick="setFilter(\'Barchasi\')" data-i18n="filter_all">Barchasi</div>',
    r'<div class="pill" onclick="setFilter\(\'To\'y\'\)">To\'y</div>': r'<div class="pill" onclick="setFilter(\'To\'y\')" data-i18n="filter_wedding">To\'y</div>',
    r'<div class="pill" onclick="setFilter\(\'Portret\'\)">Portret</div>': r'<div class="pill" onclick="setFilter(\'Portret\')" data-i18n="filter_portrait">Portret</div>',
    r'placeholder="Qidirish\.\.\."': r'placeholder="Qidirish..." data-i18n="search_placeholder"',
    
    # Profil
    r'<div class="stat-label">Bu oy</div>': r'<div class="stat-label" data-i18n="prof_this_month">Bu oy</div>',
    r'<div class="stat-label">Jami</div>': r'<div class="stat-label" data-i18n="prof_total">Jami</div>',
    r'<div class="stat-label">Daromad</div>': r'<div class="stat-label" data-i18n="prof_revenue">Daromad</div>',
    r'<div class="setting-left"><i class="ti ti-bell"></i> Bildirishnomalar</div>': r'<div class="setting-left"><i class="ti ti-bell"></i> <span data-i18n="prof_notif">Bildirishnomalar</span></div>',
    r'<div class="setting-left"><i class="ti ti-moon"></i> Qorong\'u rejim</div>': r'<div class="setting-left"><i class="ti ti-moon"></i> <span data-i18n="prof_darkmode">Qorong\'u rejim</span></div>',
    r'<div class="setting-left"><i class="ti ti-star"></i> Ilovani baholash</div>': r'<div class="setting-left"><i class="ti ti-star"></i> <span data-i18n="prof_rate">Ilovani baholash</span></div>',
    r'<div class="setting-left"><i class="ti ti-logout"></i> Chiqish</div>': r'<div class="setting-left"><i class="ti ti-logout"></i> <span data-i18n="prof_logout">Chiqish</span></div>',
    r'<div class="settings-section-label">Hisob va xavfsizlik</div>': r'<div class="settings-section-label" data-i18n="prof_sec">Hisob va xavfsizlik</div>',
    
    # Modals / Forms
    r'<label>Sana\*</label>': r'<label data-i18n="form_date">Sana*</label>',
    r'<label>Vaqt</label>': r'<label data-i18n="form_time">Vaqt</label>',
    r'<label>Manzil\*</label>': r'<label data-i18n="form_location">Manzil*</label>',
    r'<label>Narx \(so\'m\)</label>': r'<label data-i18n="form_price">Narx (so\'m)</label>',
    r'<label>Izoh</label>': r'<label data-i18n="form_notes">Izoh</label>',
    r'<button type="button" class="btn-ghost" onclick="closeModal\(\)">Bekor qilish</button>': r'<button type="button" class="btn-ghost" onclick="closeModal()" data-i18n="btn_cancel">Bekor qilish</button>',
    r'<button type="submit" class="btn-fill">Saqlash</button>': r'<button type="submit" class="btn-fill" data-i18n="btn_save">Saqlash</button>',
    
    # Login
    r'<h2 class="title">Qaytib keldingiz! 👋</h2>': r'<h2 class="title" data-i18n="login_title">Qaytib keldingiz! 👋</h2>',
    r'<p class="subtitle">Hisobingizga kiring va syomkalarni boshqaring.</p>': r'<p class="subtitle" data-i18n="login_subtitle">Hisobingizga kiring va syomkalarni boshqaring.</p>',
    r'<h2 class="title">Hisob yarating ✨</h2>': r'<h2 class="title" data-i18n="reg_title">Hisob yarating ✨</h2>',
    r'<p class="subtitle">ShootPlan orqali barcha syomkalarni boshqaring.</p>': r'<p class="subtitle" data-i18n="reg_subtitle">ShootPlan orqali barcha syomkalarni boshqaring.</p>',
    r'<div class="tab active" onclick="switchTab\(\'login\'\)">Kirish</div>': r'<div class="tab active" onclick="switchTab(\'login\')" data-i18n="login_tab">Kirish</div>',
    r'<div class="tab" onclick="switchTab\(\'register\'\)">Ro\'yxat</div>': r'<div class="tab" onclick="switchTab(\'register\')" data-i18n="reg_tab">Ro\'yxat</div>',
    
    # Admin
    r'<h1 style="color:var\(--gold\); font-size:1.5rem;">Boshqaruv Paneli</h1>': r'<h1 style="color:var(--gold); font-size:1.5rem;" data-i18n="admin_title">Boshqaruv Paneli</h1>',
    r'Ilovaga qaytish': r'<span data-i18n="admin_back">Ilovaga qaytish</span>',
    r'Eksport \(CSV\)': r'<span data-i18n="admin_export">Eksport (CSV)</span>',
}

for name, path in files.items():
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Inject lang.js script tag if not there
    if '<script src="lang.js"></script>' not in content:
        content = content.replace('</head>', '    <script src="lang.js"></script>\n</head>')
        
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated HTML files with translations tags.")
