from flask import Blueprint

example_two = Blueprint('example_2', __name__)


@example_two.route('/', methods=['GET'], strict_slashes=False)
def index():
    return "Getting response from example two"
