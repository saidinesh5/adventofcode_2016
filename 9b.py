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

        decompressed_selection_length = decompressed_length(selection)
        #select_repetition - 1, because they are already counted as part of result=len(text)
        result  += ( decompressed_selection_length*(select_repetition - 1) - len(match_text) )

    return result

def main():
    #print(decompressed_length('(3x3)XYZ'))
    #print(decompressed_length('X(8x2)(3x3)ABCY'))
    #print(decompressed_length('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
    #print(decompressed_length('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))
    text = open('input9.txt').read().strip()
    print(decompressed_length(text))

if __name__ == '__main__':
    main()
