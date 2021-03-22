{% load static %}
{
    id: 'main_menu',
    width: 200,
    view: "menu",
    openAction: "click",
    type: {
        subsign: true
    },
    scroll: "y",
    layout: "y",
    subMenuPos: "right",
    submenuConfig: {
        width: 255,
        zIndex: 1000
    },
    data: [
        {% if perms.library.view_author %}
            {
                id: "authors",
                value: "Authors",
                icon: "fas fa-pen-fancy",
                url: "{% url 'admin_webix:library.author.list' %}",
                loading_type: 'js_script',
            },
        {% endif %}
        {% if perms.library.view_book %}
            {
                id: "books",
                value: "Books",
                icon: "fas fa-book",
                url: "{% url 'admin_webix:library.book.list' %}",
                loading_type: 'js_script',
            },
        {% endif %}
    ],
    on: {
        onMenuItemClick: function (id) {
            var item = this.getMenuItem(id);
            var loading_type = item.loading_type;
            var url = item.url;
            if (loading_type === 'redirect') {
                loading(url);
            } else if (loading_type === 'js_script') {
                load_js(url);
            }
        }
    }
}
