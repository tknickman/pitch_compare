from pyramid.exceptions import HTTPBadRequest
from jsonschema import Draft3Validator
import logging
import json
import six


logger = logging.getLogger(__name__)


def validate_api_input(request, schema):
    """
    Validates that the params on the given `request` match the given
    JSON `schema`. If the params match, return them as a dict - otherwise
    return None.

    :param request: pyramid.request.Request
    :param schema: dict
    :return: dict | None
    """

    # get the input params off the request
    api_input = dict(request.params)

    # all GET params come across as strings
    # force ints where possible. Also, use six.iteritems to
    # preserve 2.x and 3.x compatibility (dict.iteritems() is deprecated
    # in 3.x)
    for key, value in six.iteritems(api_input):
        try:
            api_input[key] = int(value)
        except ValueError:
            pass

    # validate the input against the given schema
    if Draft3Validator(schema).is_valid(api_input):
        return api_input
    else:
        logger.debug('error=invalid input')
        return None


def error_response(data):
    """
    Return an HTTP bad response with the given `data`

    :param data: *
    :return: pyramid.exceptions.HTTPBadRequest
    """

    # build the response
    response = HTTPBadRequest()
    # use sux to convert to unicode to preserve 2.x and 3.x compatibility
    response.text = six.u(json.dumps(data))
    response.content_type = 'application/json'

    # return the response
    return response
