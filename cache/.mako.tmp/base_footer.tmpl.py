# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1515773763.950798
_enable_loop = True
_template_filename = 'themes/hpstr/templates/base_footer.tmpl'
_template_uri = 'base_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if content_footer:
            __M_writer('    <div class="footer-wrapper">\n        <footer role="contentinfo">\n            <p>')
            __M_writer(str(content_footer))
            __M_writer('</p>\n            ')
            __M_writer(str(template_hooks['page_footer']()))
            __M_writer('\n        </footer>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/hpstr/templates/base_footer.tmpl", "uri": "base_footer.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "33": 2, "34": 13, "40": 4, "48": 4, "49": 5, "50": 6, "51": 8, "52": 8, "53": 9, "54": 9, "60": 54}}
__M_END_METADATA
"""
