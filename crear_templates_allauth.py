import os

# Definir la estructura de archivos y el contenido de cada template
templates = {
    "login.html": """{% extends "base.html" %}
{% load i18n widget_tweaks %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center mb-4">Iniciar Sesión</h2>
            <form method="post" action="{% url 'account_login' %}" class="p-4 border rounded shadow-sm bg-light">
                {% csrf_token %}
                {{ form.login|add_class:"form-control mb-3" }}
                {{ form.password|add_class:"form-control mb-3" }}
                {% if redirect_field_value %}
                    <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}">
                {% endif %}
                <button type="submit" class="btn btn-primary w-100">Iniciar Sesión</button>
            </form>
            <div class="text-center mt-3">
                <p><a href="{% url 'account_reset_password' %}">¿Olvidaste tu contraseña?</a></p>
                <p>¿No tienes cuenta? <a href="{% url 'account_signup' %}">Regístrate aquí</a>.</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""",
    "signup.html": """{% extends "base.html" %}
{% load i18n widget_tweaks %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center mb-4">Crear Cuenta</h2>
            <form method="post" action="{% url 'account_signup' %}" class="p-4 border rounded shadow-sm bg-light">
                {% csrf_token %}
                {{ form.username|add_class:"form-control mb-3" }}
                {{ form.email|add_class:"form-control mb-3" }}
                {{ form.password1|add_class:"form-control mb-3" }}
                {{ form.password2|add_class:"form-control mb-3" }}
                <button type="submit" class="btn btn-primary w-100">Registrarse</button>
            </form>
            <div class="text-center mt-3">
                <p>¿Ya tienes cuenta? <a href="{% url 'account_login' %}">Inicia sesión aquí</a>.</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""",
    "password_reset.html": """{% extends "base.html" %}
{% load i18n widget_tweaks %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center mb-4">Restablecer Contraseña</h2>
            <p class="text-center">Introduce tu correo electrónico para recibir un enlace de restablecimiento de contraseña.</p>
            <form method="post" action="{% url 'account_reset_password' %}" class="p-4 border rounded shadow-sm bg-light">
                {% csrf_token %}
                {{ form.email|add_class:"form-control mb-3" }}
                <button type="submit" class="btn btn-primary w-100">Enviar Enlace</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
""",
    "password_reset_done.html": """{% extends "base.html" %}
{% block content %}
<div class="container mt-5 text-center">
    <h2>Revisa tu Correo</h2>
    <p>Si existe una cuenta asociada a este correo, recibirás un enlace para restablecer tu contraseña.</p>
</div>
{% endblock %}
""",
    "password_reset_from_key.html": """{% extends "base.html" %}
{% load widget_tweaks %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center mb-4">Nueva Contraseña</h2>
            <form method="post" action="{% url 'account_reset_password_from_key' uidb36=uidb36 key=key %}" class="p-4 border rounded shadow-sm bg-light">
                {% csrf_token %}
                {{ form.new_password1|add_class:"form-control mb-3" }}
                {{ form.new_password2|add_class:"form-control mb-3" }}
                <button type="submit" class="btn btn-primary w-100">Restablecer Contraseña</button>
            </form>
        </div>
    </div>
</div>
{% endblock %}
""",
    "password_reset_from_key_done.html": """{% extends "base.html" %}
{% block content %}
<div class="container mt-5 text-center">
    <h2>Contraseña Restablecida</h2>
    <p>Tu contraseña se ha restablecido exitosamente. <a href="{% url 'account_login' %}">Inicia sesión aquí</a>.</p>
</div>
{% endblock %}
""",
    "logout.html": """{% extends "base.html" %}
{% block content %}
<div class="container mt-5 text-center">
    <h2>Sesión Cerrada</h2>
    <p>Has cerrado sesión correctamente. <a href="{% url 'account_login' %}">Inicia sesión aquí</a> para regresar.</p>
</div>
{% endblock %}
""",
    "email_confirmation_sent.html": """{% extends "base.html" %}
{% block content %}
<div class="container mt-5 text-center">
    <h2>Verificación de Correo Electrónico</h2>
    <p>Hemos enviado un enlace de verificación a tu correo. Por favor, revisa tu bandeja de entrada y sigue las instrucciones para activar tu cuenta.</p>
</div>
{% endblock %}
"""
}

# Crear la carpeta templates/account si no existe
os.makedirs("templates/account", exist_ok=True)

# Crear cada archivo de template con su contenido
for filename, content in templates.items():
    with open(f"templates/account/{filename}", "w") as file:
        file.write(content)

print("Templates de django-allauth creados exitosamente en la carpeta templates/account.")
