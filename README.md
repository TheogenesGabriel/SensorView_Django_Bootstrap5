# SensorView 🌡️💧
**Monitor de Temperatura e Umidade Residencial**

Sistema web desenvolvido com Django para receber, armazenar e exibir leituras de um sensor de temperatura e umidade (DHT11/DHT22) instalado em casa.

---

## 📁 Estrutura do Projeto

```
sensorview/
├── sensorview/          # Configurações do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                # App: página inicial e informações gerais
│   ├── views.py
│   ├── urls.py
│   └── templates/core/
│       ├── home.html    # Página inicial com leitura atual
│       └── sobre.html   # Informações sobre o sistema
├── leituras/            # App: histórico, gráfico e endpoint do sensor
│   ├── views.py
│   ├── urls.py
│   └── templates/leituras/
│       ├── historico.html  # Tabela com histórico de leituras
│       └── grafico.html    # Gráfico com Chart.js
├── templates/
│   └── base.html        # Template base (navbar, rodapé)
├── static/              # Arquivos estáticos (CSS, JS futuros)
├── manage.py
└── requirements.txt
```

## 🔗 Rotas do sistema

| URL | Descrição |
|-----|-----------|
| `/` | Página inicial — leitura atual do sensor |
| `/sobre/` | Informações sobre o SensorView |
| `/leituras/historico/` | Tabela com histórico de leituras |
| `/leituras/grafico/` | Gráfico de variação do dia |
| `/leituras/receber/` | Endpoint HTTP POST para o sensor |

## 🚀 Como rodar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/sensorview.git
cd sensorview
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar o servidor
```bash
python manage.py migrate
python manage.py runserver
```

Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📡 Endpoint do Sensor

Para enviar dados do ESP32/Arduino, faça uma requisição **HTTP POST** para:

```
POST /leituras/receber/
Content-Type: application/json

{
    "temperatura": 28.5,
    "umidade": 65.0
}
```

---

## 🛠️ Tecnologias

- **Django** — framework web
- **Bootstrap 5** — layout responsivo
- **Chart.js** — gráfico de leituras
- **Sensor DHT11/DHT22 + ESP32** — hardware

---

## 📌 Status do Projeto

Este projeto está em desenvolvimento como atividade do curso.
- [x] Estrutura inicial do Django
- [x] Pages: home, histórico, gráfico, sobre
- [x] Endpoint para receber dados do sensor
- [ ] Banco de dados (models)
- [ ] Integração real com sensor físico
- [ ] Deploy em rede local
