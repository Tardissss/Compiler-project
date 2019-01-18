def error_check(text):
    print '----------------------------------------'
    print 'Checking error:'
    check_result = 1 # variable to store the error check result
    line = 1 # line number counter
    pre = -1 # varaible to locate the last instruction
    for ch in range(len(text)):
        # if we find an = and this = is not in the bool expression, we think it may should be :=
        if text[ch] == '=' and text[ch-1] != ':' and text[ch-1] != '!' and text[ch-1] != '<' and text[ch-1] != '>' and text[pre:ch].find('\"') == -1 and text[pre:ch].find('if') == -1 and text[pre:ch].find('while') == -1:
            print 'Detect \'=\' in line '+str(line) + ', you may want to change it to \':=\'.'
            res = input('[1/0]')
            # print res
            # if the programmer want to change this, change it
            if res == 1:
                text = text[:ch] + ':' + text[ch:]
                check_result = 2;
        # instruction ++
        elif text[ch] == '\n':
            pre = ch
            line = line + 1

    line = 1 # line counter
    pre = -1 # variable to locate instruction
    ch = 0 # text pointer
    while ch < len(text):
        # if read a whole instruction
        if text[ch] == '\n':
            # if not in bool expression
            if text[pre+1:ch].find(';') == -1 and text[pre+1:ch].find('while') == -1:
                if ch == len(text)-1:
                    pass
                else:
                    # if curr instruction is in a sub stmtlist
                    if text[ch:].find('end') != -1:
                        # if curr is not the last in this stmt list
                        if text[ch:text.find('end')].count('\n') > 1:
                            print '1:Can\'t detect \';\' in line '+ str(line) + ', you may want to add \';\' to the end.'
                            print text[pre+1:ch]
                            res = input('[1/0]')
                            # print res
                            if res == 1:
                                text = text[:ch] + ';' + text[ch:]
                                check_result = 2;
                                # print text
                                # print text[ch]
                                ch = ch + 1
                                line = line + 1
                    else:
                        # print text[ch:]
                        print '2:Can\'t detect \';\' in line '+ str(line) + ', you may want to add \';\' to the end.'
                        print text[pre+1:ch]
                        res = input('[1/0]')
                        # print res
                        if res == 1:
                            text = text[:ch] + ';' + text[ch:]
                            check_result = 2;
                            # print text
                            # print text[ch]
                            ch = ch + 1   
                            line = line + 1 
            line = line + 1
            pre = ch                   

        # additional check for the last of the progrram
        if ch == len(text)-1:
            if text[ch] == ';':
                print 'We detect \';\' in line '+ str(line) + ', you may want to erase \';\' at the end.'
                print text[pre+1:ch+1]
                res = input('[1/0]')
                # print res
                if res == 1:
                    text = text[:ch]
                    check_result = 2;                    

                line = line + 1
                pre = ch
        ch = ch + 1        

    return text, check_result