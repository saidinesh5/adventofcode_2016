import re

def decompressed_length(text):
    result = len(text)

    compress_expression = re.compile('\(\d+x\d+\)')
    number_expression = re.compile('\d+')

    matches = compress_expression.finditer(text)
    while True:
        match = None
        try:
            match = next(matches)
        except StopIteration:
            break

        #Compute the change this compress sequence brings to the decompressed text
        match_text = match.group(0)
        select_length, select_repetition = list(map(int, number_expression.findall(match_text)))
        selection = text[match.end() : match.end() + select_length]

        #select_repetition - 1, because they are already counted as part of result=len(text)
        result  += ( len(selection)*(select_repetition - 1) - len(match_text) )

        #Now, ignore the compress sequences that are to be treated as normal text
        #because they are in the text selected by this compress sequence
        for m in compress_expression.finditer(selection):
            next(matches)

    return result

def main():
    #print(decompressed_length('ADVENT'))
    #print(decompressed_length('A(1x5)BC'))
    #print(decompressed_length('(3x3)XYZ'))
    #print(decompressed_length('A(2x2)BCD(2x2)EFG'))
    #print(decompressed_length('(6x1)(1x3)A'))
    #print(decompressed_length('X(8x2)(3x3)ABCY'))
    text = open('input9.txt').read().strip()
    print(decompressed_length(text))

if __name__ == '__main__':
    main()
