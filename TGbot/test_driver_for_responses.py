from types import TracebackType
import responses

inputmsg = 'Good morning'
input_msg = responses.input_parsing(inputmsg)
indicator = responses.classify_input(input_msg)

print(indicator)

response = responses.handle_response(indicator, input_msg)
print(response)
