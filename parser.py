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
    for line in bibfile:
    #     char_list = line.split('=')
        if line[0]=='@':
            paper_list.append(temp)
            temp.clear()
            # print('aaaaaaaaaaaaaaaaaaaaaaaaa')
        else:
            char_list = [ x.strip('@{ "",\n}') for x in re.split('[{=]',line)]
            if char_list[0]=='title':
                temp["title"] = char_list[1]
            elif char_list[0]=='year':
                temp["year"] = char_list[1]
            elif char_list[0]=='author':
                temp["author"] = char_list[1]
            elif char_list[0]=='keyword':
                temp["keyword"] = char_list[1]
            # print(temp)
            # print(char_list)
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
        # print(line.strip())
    bibfile.close()
    print(paper_list)

    return paper_list


if __name__=='__main__':
    parser()