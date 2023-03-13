

def paginacao():
    """
    {% if is_paginated %}
        <nav aria-label="nav-page">
            <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li>
            {% endif %}

            {% for each_page in paginator.page_range %}
                {% if page_obj.number == each_page %}
                    <li class="page-item active"><a class="page-link" href="#">{{ each_page }}</a></li>
                {% else %}
                    <li class="page-item"><a class="page-link" href="?page={{ each_page }}">{{ each_page }}</a></li>
                {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li>
            {% endif %}
            </ul>
        </nav>
    {% endif %}
    """
