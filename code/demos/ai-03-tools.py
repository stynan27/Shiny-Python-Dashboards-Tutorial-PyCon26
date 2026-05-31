# run this script with
# python code/demos/ai-03-tools.py
from dotenv import load_dotenv
from chatlas import ChatGithub, ChatAnthropic

 # this is the path to the .env file relative to working directory
load_dotenv('.env')

def pycon_locations(year: int) -> str:
    """Looks up the location PyCon US is held given a year.

    Parameters
    ----------
    year : int
        The year of the PyCon US conference.

    Returns
    -------
    str
        The city and region where PyCon US is held that year, or a message
        indicating the location is unknown.
    """
    match year:
        case 2027:
            return "The Moon"
        case 2026:
            return "New York City"
        case 2025:
            return "Vancouver, BC"

chat = ChatGithub(model="gpt-5")
#chat = ChatAnthropic()

chat.register_tool(pycon_locations)

chat.chat("Where is PyCon US 2027 being held?")
