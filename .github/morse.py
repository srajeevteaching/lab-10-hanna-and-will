import random as rn
import os
def read_file(filename):
    data_list=[]
    file=open(filename,"r")
    for line in file:
        data_list.append(line.split('	'))
    file.close()
    return data_list
def fixlast(l):
    for x in l:
        x[-1] = x[-1].strip()
    return l
def make_dict( m ):
    morse_dict = { }
    for line in m:
        morse_dict[str(line[1])]=str(line[0])
    return morse_dict
def decode(m,file):
    f=open(file,"r")
    morse_list=[]
    output=''
    for line in f:
        morse_list.append(line.split(' '))
    f.close()
    morse_list=fixlast(morse_list)
    for i in morse_list:
        for x in i:
            if x in m:
                output=output+str(m[x])
        output=output+' '
    print(output)


def main():
    # morse1=read_file('morse1.txt')
    # morse2=read_file('morse2.txt')
    # morse3=read_file('morse3.txt')
    print(os.listdir())
    morsecode=read_file('morsecode.txt')
    # print(morsecode)
    morsecode=fixlast(morsecode)
    # print(morsecode)
    morse_dict=make_dict(morsecode)
    # print(morse_dict)
    decode(morse_dict,'morse1.txt')
    decode(morse_dict, 'morse2.txt')
    decode(morse_dict, 'morse3.txt')
main()