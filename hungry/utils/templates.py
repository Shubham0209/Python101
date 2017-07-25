import os
import datetime


def get_template_file(path):
    file_path = os.path.join(os.path.dirname(__file__), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid path %s" % (file_path))
    return file_path


def get_template(path):
    file_path = get_template_file(path)
    return open(file_path).read()


def render_context(template_string, context):
    return template_string.format(**context)
