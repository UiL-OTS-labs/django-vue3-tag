# django-vue3-tag

A small library that helps integrate Vue3 components in Django templates, using a `{% vue %}` template tag.

## Example

```django
{% block content %}
<div>
    Please complete the following survey:
    {% vue SurveyView :definition=survey.content :invite_id=invite_id %}
</div>
{% endblock %}
```


## Why use it?
Using this library, you can structure your application with old-school Django templates, and introduce interactivity where necessary using Vue components.

## Getting started

The library assumes that the Vue application was loaded and that `createApp()` and the relevant components are accessible from the global window object.
(You only need to expose the components that you directly load with a `{% vue %}` tag)

For example, you might use the following tags somewhere in your templates to include a compile Vue app from the static folder:

```html
<!-- load vue app from static folder (run 'yarn watch') -->
<script src="{% static 'vue/js/chunk-vendors.js' %}"></script>
<script src="{% static 'vue/js/app.js' %}"></script>
```

Or from a live reload server:

```html
<!-- load vue app from webpack server with hot-reloading (run 'yarn serve') -->
<script src="http://localhost:8080/js/chunk-vendors.js"></script>
<script src="http://localhost:8080/js/app.js"></script>
```

You also need to add `vue3_tag` to Django's `INSTALLED_APPS` in `settings.py`

## Binding

Binding properties mimics Vue's system with some small differences. The following kinds of bindings are available:


| Syntax  | Behaviour  |
|:--|:--|
| `prop="thing"`  | bind the constant `thing` to the property `prop`  |
| `:prop="thing"`  | bind the Javascript expression `thing` to the property `prop`  |
| `:prop=thing`  | bind the (Python) template variable `thing` to the property `prop`  |
| `:prop`  | shortcut for `:prop=prop` |
| `@event="handler"`  | bind the Javascript expression `handler` as an event handler for the event `event` |


## How does it work?

The template tag injects a div container for the component and a script tag that calls Vue's `createApp`.
