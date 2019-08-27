import json

from pyramid.view import view_config

from docutils_ast.process.translate import CodeTranslator
import logging

logger = logging.getLogger(__name__)

@view_config(route_name='home', renderer='json')
def my_view(request):
    try:
        data = json.loads(request.body)
    except:
        return {}
    code = data['code']
    logger.debug('%s', code)
    translater = CodeTranslator(logger=logger)

    r = translater.do_translate(code, filename="input.py", output_filename="out.ts")
    return {'file': r}

