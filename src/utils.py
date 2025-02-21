def format_response(response):
    return response.replace("\n", "<br>")
def validate_input(user_input):
    if not user_input or len(user_input.strip()) == 0:
        return False
    return True