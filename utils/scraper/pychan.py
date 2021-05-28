import basc_py4chan
from random import choice

boards = ['g', 'v', 'sci', 'tv', 'o', 'a']

def  random_4chan():
    board = basc_py4chan.Board(choice(boards)) # chooses a random board from the list
    thread_ids = board.get_all_thread_ids() 
    str_thread_ids = [str(id) for id in thread_ids]
    thread_id = choice(str_thread_ids) # chooses a random thread from the list
    thread = board.get_thread(thread_id)
    files = thread.files() # retrieves the URLS of all the files in the thread
    str_files = [str(url) for url in files]
    # returns a random image URL from the list
    return choice(str_files), thread.url, board.name

random_4chan()