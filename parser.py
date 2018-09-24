import re

# class LineParser:
#     line = ""
#     position = 0
#     def __init__(self, line):
#         self.line = line


def parser():

    paper_list = []
    temp ={}

    bibfile = open('./reference.bib','r')
    # bibfile = open('./anarticle.bib','r')

    # num_of_art=

    for line in bibfile:
    #     char_list = line.split('=')
        char_list = [ x.strip('@{ "",\n') for x in re.split('[{=]',line)]
        if line[0]=='@':
            temp.clear()
            # print('aaaaaaaaaaaaaaaaaaaaaaaaa')
        else:
            if char_list[0]=='inproceedings':
                # print('AAAAAAAAAAAAAAAAAAAAAAAAAAA')
                temp["ID"] = char_list[1]
            elif char_list[0]=='title':
                temp["title"] = char_list[1]
            elif char_list[0]=='year':
                temp["year"] = char_list[1]
            elif char_list[0]=='author':
                temp["author"] = char_list[1]
            elif char_list[0]=='keyword':
                temp["keyword"] = char_list[1]
            # print(temp)
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')

        if line[0]=='}':
            paper_list.append(temp.copy())

        # print(line[0])            
        # print(char_list)
        # print(line.strip())
        # print(temp)
    bibfile.close()
    print(paper_list)

    return paper_list


if __name__=='__main__':
    parser()
