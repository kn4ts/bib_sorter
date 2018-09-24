def parser():
    # bibfile = open('./reference.bib','r')
    bibfile = open('./anarticle.bib','r')
    for line in bibfile:
        print(line.strip())
    bibfile.close()

if __name__=='__main__':
    parser()