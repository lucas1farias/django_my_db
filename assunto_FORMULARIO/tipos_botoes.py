

"""
* ========== Formulário configurado via padrão (input manual) ==========

<form action="{% url 'model_form' %}" method="post">
    {% csrf_token %}
    <input type="text" name="name" size='20' min=3 placeholder="Nome da linguagem" required >

    <button type="submit">Enviar (via button)</button>
    <input type="submit" value="Enviar (via input)">
</form>

* ========== Formulário configurado via model Form ==========

<form action="{% url 'model_form' %}" method="post">
    {% csrf_token %}
    {{ form }}

    <button type="submit">Enviar (via button)</button>
    <input type="submit" value="Enviar (via input)">
</form>
"""
