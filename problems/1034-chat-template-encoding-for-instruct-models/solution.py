
def encode(text):
    return [ord(c) for c in text]

def get_system_header():
    return header_ids["START_HEADER_ID"]+encode("system")+header_ids["END_HEADER_ID"]+encode("\n\n")

def get_user_header():
    return header_ids["START_HEADER_ID"]+encode("user")+header_ids["END_HEADER_ID"]+encode("\n\n")

def get_assistant_header():
    return header_ids["START_HEADER_ID"]+encode("assistant")+header_ids["END_HEADER_ID"]+encode("\n\n")


header_ids = {
        "BEGIN_OF_TXT": [1],
        "START_HEADER_ID": [2],
        "END_HEADER_ID": [3],
        "EOT_ID": [4]
    }

def encode_chat(user_message: str, system_message: str = None) -> list:
    """
    Build a Llama-3-style chat template token sequence.

    Args:
        user_message: the user's message (string)
        system_message: optional system message (string). If None, use
            "You are a helpful assistant.".

    Returns:
        A list of integer token IDs.
    """

    if system_message is None:
        system_message = "You are a helpful assistant."


    system_encoded = encode(system_message)
    user_encoded= encode(user_message)

    encodings = header_ids["BEGIN_OF_TXT"]+get_system_header()+system_encoded+header_ids["EOT_ID"]+get_user_header()+user_encoded+header_ids["EOT_ID"]+get_assistant_header()
    
    return encodings


