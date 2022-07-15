"""
Contains scripts in the form of multiline comments that directly be printed.
"""

list_scripts = ['script_loop_multiprocessing']

script_loop_multiprocessing = '''

    # Script for creating multiprocessing loops
    # as an example, writing a dataframe column to a text file

    from tqdm.auto import tqdm
    import multiprocessing as mp

    def process_i(i):
        # Here write the thing you want to do with "i"
        # As an example I will read the value in the dataframe column and write it into a file
        
        txt = df['text'][i]
        with open("text.txt", "a") as f:
            f.write(txt+'\\n')
    
    # Now the main part, run it with multiprocessing
    runlength = len(df)
    with mp.Pool(mp.cpu_count()) as p:
        r = list(tqdm(p.imap(process_i, range(runlength)), total=runtlength))
        
    # There you go!

    '''