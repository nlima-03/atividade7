from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape  # Essencial para segurança (evita XSS)

app = Flask(__name__)
# A chave secreta é OBRIGATÓRIA para usar sessões (cookies) de forma segura no Flask
# Nunca use 'devkey' em produção!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# --- Base de Dados (Simulação) ---
# NUNCA armazene passwords em texto simples num código real!
# Aqui, usamos um hash placeholder para a demo.
USERS = {'admin': 'pbkdf2:sha256:150000$hQxY$308d7a...'}

# Estados simulados dos dispositivos
DEVICE_STATUS = {
    'luz_sala': 'Desligada',
    'alarme_casa': 'Desligado',
    'termostato': '20°C'
}


# --- Rotas (Endpoints) ---

@app.route('/')
def home():
    # Verifica se o utilizador está logado antes de mostrar o dashboard
    if 'username' not in session:
        return redirect(url_for('login'))

    # RENDERIZAÇÃO SEGURA: Usar 'render_template' garante que as variáveis são tratadas
    # como HTML seguro por padrão no Jinja2.
    return render_template('dashboard.html',
                           username=session['username'],
                           devices=DEVICE_STATUS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 1. SEGURANÇA BÁSICA: Obtenção de credenciais de forma segura (via POST)
        username = request.form['username']
        password = request.form['password']

        # 2. SIMULAÇÃO DE VALIDAÇÃO (Num sistema real, usaria bcrypt para verificar o hash)
        if username in USERS and password == 'password123':  # Usado apenas para a demo.
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Login falhou. Tente novamente."

    return """
    <form method="POST">
        Utilizador: <input name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Entrar">
    </form>
    """


@app.route('/device/control', methods=['POST'])
def control_device():
    if 'username' not in session:
        return redirect(url_for('login'))

    device = request.form.get('device')
    action = request.form.get('action')

    if device in DEVICE_STATUS:
        # 3. SEGURANÇA NA ENTRADA DE DADOS: Sanitização explícita (embora o Jinja faça por padrão)
        safe_device = str(escape(device))

        # Lógica de Controlo (simulada)
        if action == 'toggle':
            current = DEVICE_STATUS[device]
            new_status = 'Ligada' if current == 'Desligada' else 'Desligada'
            DEVICE_STATUS[device] = new_status

            return f"Dispositivo '{safe_device}' alterado para {new_status}."

    return "Ação Inválida."


if __name__ == '__main__':
    # NUNCA use debug=True em produção.
    app.run(debug=True, port=8080)