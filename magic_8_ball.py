import logging 
import requests 

# Configure your logger. filename - where to write to. otherwise logs write to the console
# level is the minimum log level that is recorded. DEBUG means log everything. 
# format sets the format of the string that is recorder for each log event. See docs for example format strings. 
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

""" A program with an lot of logging. """

def get_user_question():
    question = ''
    while not question:
        question = input('please enter your question: ')
        if not question:
            logging.debug(f'user has entered invalid data "{question}"')

    logging.info(f'User has entered valid question "{question}"')
    return question


def ask_magic_8_ball(question):
    url = f'https://8ball.delegator.com/magic/JSON/{question}'
    
    try:
        logging.info(f'About to make request to Magic 8 ball API at url {url}')
        response = requests.get(url)
        logging.debug(f'response received from API {response}')
    except:
        logging.exception(f'Error requesting URL {url}')
        return 
    
    try:
        json = response.json()
        logging.debug(f'Decoded JSON response {json}')
    except:
        logging.exception(f'Error decoding respose into JSON')
        return 
    
    try:
        answer = json['magic']['answer']
        logging.debug(f'Returning "{answer}"" from API')
        return answer
    except:
        logging.exception(f'Error reading data from response {response}')



def main():
    question = get_user_question()
    response = ask_magic_8_ball(question)
    if response:
        logging.info(f'Answer recieved from magic 8-ball {response}')
        print('Magic 8 Ball Says... ' + response)
    else:
        logging.error('No response received from magic 8 ball')
        print('Sorry, the Magic 8 Ball is not able to answer right now.')


if __name__ == '__main__':
    logging.info('Magic 8-Ball Program Launched')
    main()