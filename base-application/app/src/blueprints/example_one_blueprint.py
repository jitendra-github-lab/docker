from flask import Blueprint

example_one = Blueprint('example_1', __name__)


@example_one.route('/', methods=['GET'], strict_slashes=False)
def index():
    return 'Getting response from example one.'
