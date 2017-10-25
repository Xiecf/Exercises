def count_words(filename):
    '''计算文件包含多少单词'''
    try:
        with open(filename) as a:
           x = a.read()
    except FileNotFoundError:
        msg = 'Sorry,the file ' + filename + ' does not exist.'
        print(msg)
    else:
        words = x.split()
        print('The file ' + '(' + filename + ')' + ' has about ' + 
        str(len(words)) + 'words.')
            
