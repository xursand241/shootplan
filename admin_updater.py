import re

with open('c:/Users/xursand/Desktop/jadvalim/admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Nav Item to Sidebar
content = content.replace(
    '<a href="index.html" class="nav-item">',
    '<a href="#" class="nav-item" onclick="switchView(\'viewUsers\', this)"><i data-i18n="admin_tab_users">👤</i> <span data-i18n="admin_tab_users">Foydalanuvchilar</span></a>\n                <a href="index.html" class="nav-item">'
)

# 2. Add Nav Item to Bottom Nav
content = content.replace(
    '<a href="#" class="bottom-nav-item" style="color: var(--danger);" onclick="logout()">',
    '<a href="#" class="bottom-nav-item" onclick="switchView(\'viewUsers\', this)"><i>👤</i><span data-i18n="admin_tab_users">Users</span></a>\n            <a href="#" class="bottom-nav-item" style="color: var(--danger);" onclick="logout()">'
)

# 3. Add viewUsers HTML block before </main>
users_view = """
                <!-- --- Foydalanuvchilar View --- -->
                <div class="view" id="viewUsers">
                    <div class="table-toolbar">
                        <div class="search-box">
                            <i>🔍</i>
                            <input type="text" id="userSearch" placeholder="Foydalanuvchi izlash..." oninput="renderUsersView()">
                        </div>
                    </div>
                    
                    <div class="table-card glass">
                        <table class="data-table">
                            <thead>
                                <tr>
                                    <th>Ism</th>
                                    <th>Email</th>
                                    <th>Holati</th>
                                    <th style="text-align:right">Amallar</th>
                                </tr>
                            </thead>
                            <tbody id="usersTbody">
                                <!-- JS -->
                            </tbody>
                        </table>
                    </div>
                </div>
"""
content = content.replace('            </div>\n        </main>', users_view + '\n            </div>\n        </main>')

# 4. Update switchView function
content = content.replace(
    "const titles = { 'viewDashboard': 'Dashboard', 'viewShoots': 'Syomkalar Jadvali', 'viewClients': 'Mijozlar' };",
    "const titles = { 'viewDashboard': 'Dashboard', 'viewShoots': 'Syomkalar Jadvali', 'viewClients': 'Mijozlar', 'viewUsers': 'Foydalanuvchilar' };"
)
content = content.replace(
    "if (viewId === 'viewClients') renderClientsView();",
    "if (viewId === 'viewClients') renderClientsView();\n            if (viewId === 'viewUsers') renderUsersView();"
)

# 5. Add renderUsersView logic before initTheme
js_logic = """
        // --- Foydalanuvchilar Logic ---
        function renderUsersView() {
            const users = JSON.parse(localStorage.getItem('shootplan_users') || '[]');
            const tbody = document.getElementById('usersTbody');
            const search = document.getElementById('userSearch').value.toLowerCase();
            
            let html = '';
            let filtered = users;
            
            if (search) {
                filtered = users.filter(u => (u.name || '').toLowerCase().includes(search) || (u.email || '').toLowerCase().includes(search));
            }
            
            if (filtered.length === 0) {
                html = `<tr><td colspan="4" style="text-align:center; padding: 40px; color: var(--text-muted);">Mijozlar topilmadi.</td></tr>`;
            } else {
                filtered.forEach(u => {
                    const statusText = u.approvalStatus === 'approved' ? 'Tasdiqlangan' : 'Kutilmoqda';
                    const statusColor = u.approvalStatus === 'approved' ? 'var(--success)' : 'var(--warn)';
                    const statusBg = u.approvalStatus === 'approved' ? 'rgba(76, 175, 120, 0.1)' : 'rgba(245, 166, 35, 0.1)';
                    
                    let actions = '';
                    if (u.approvalStatus === 'pending') {
                        actions += `<button class="btn-primary" style="padding: 6px 12px; font-size: 0.75rem; min-width: auto; height: auto;" onclick="approveUser('${u.id}')">Tasdiqlash</button> `;
                    }
                    if (u.email !== 'admin@shootplan.uz') {
                        actions += `<button class="btn-primary" style="padding: 6px 12px; font-size: 0.75rem; min-width: auto; height: auto; background: var(--danger); border-color: var(--danger); color: white;" onclick="deleteUser('${u.id}')">O'chirish</button>`;
                    }
                    
                    html += `
                        <tr>
                            <td><div style="font-weight:700;">${u.name}</div></td>
                            <td>${u.email}</td>
                            <td>
                                <span style="background: ${statusBg}; color: ${statusColor}; padding: 4px 10px; border-radius: 50px; font-size: 0.75rem; font-weight: 600;">
                                    ${statusText}
                                </span>
                            </td>
                            <td style="text-align:right;">${actions}</td>
                        </tr>
                    `;
                });
            }
            tbody.innerHTML = html;
        }

        function approveUser(id) {
            const users = JSON.parse(localStorage.getItem('shootplan_users') || '[]');
            const idx = users.findIndex(u => u.id === id);
            if (idx > -1) {
                users[idx].approvalStatus = 'approved';
                localStorage.setItem('shootplan_users', JSON.stringify(users));
                renderUsersView();
            }
        }
        
        function deleteUser(id) {
            if(confirm("Foydalanuvchini o'chirishni tasdiqlaysizmi?")) {
                let users = JSON.parse(localStorage.getItem('shootplan_users') || '[]');
                users = users.filter(u => u.id !== id);
                localStorage.setItem('shootplan_users', JSON.stringify(users));
                renderUsersView();
            }
        }

"""
content = content.replace('        // --- Theme ---', js_logic + '\n        // --- Theme ---')

with open('c:/Users/xursand/Desktop/jadvalim/admin.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Admin HTML modified successfully.")
