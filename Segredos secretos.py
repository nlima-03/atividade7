from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape  # Essencial para segurança (evita XSS)

app = Flask(__name__)
# A chave secreta é OBRIGATÓRIA para usar sessões (cookies) de forma segura no Flask
# Nunca use 'devkey' em produção!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# --- Base de Dados (Simulação) ---
# NUNCA armazene senhas em texto simples num código real!
# Aqui, estamos armazenando a senha diretamente no código (Vulnerabilidade).
USERS = {'admin': 'password123'}  # Senha em texto simples

# Estados simulados dos dispositivos
DEVICE_STATUS = {
    'luz_sala': 'Desligada',
    'alarme_casa': 'Desligado',
    'termostato': '20°C'
}


# --- Rotas (Endpoints) ---

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Vulnerabilidade XSS: A variável 'username' é diretamente exibida no HTML, sem sanitização adequada
    return render_template('dashboard.html', username=session['username'], devices=DEVICE_STATUS)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Vulnerabilidade: Senha em texto simples (sem hash) e verificação fraca
        username = request.form['username']
        password = request.form['password']

        # Vulnerabilidade de SQL Injection: A query não é sanitizada
        # No código real, usaria uma biblioteca como o SQLAlchemy ou prepared statements.
        if username in USERS and USERS[username] == password:  # Verificação de senha em texto simples
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

    # Vulnerabilidade: Falta de validação para controlar dispositivos
    device = request.form.get('device')
    action = request.form.get('action')

    if device in DEVICE_STATUS:
        # Vulnerabilidade XSS: Falta de sanitização no nome do dispositivo
        safe_device = device  # Sem sanitização com 'escape'

        # Lógica de Controlo (simulada)
        if action == 'toggle':
            current = DEVICE_STATUS[device]
            new_status = 'Ligada' if current == 'Desligada' else 'Desligada'
            DEVICE_STATUS[device] = new_status
            return f"Dispositivo '{safe_device}' alterado para {new_status}."

    return "Ação Inválida."


if __name__ == '__main__':
    # Vulnerabilidade: Debug habilitado (em produção, pode ser acessado por usuários maliciosos)
    app.run(debug=True, port=8080)  # NUNCA use debug=True em produção