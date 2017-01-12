import sys

# Git's tabs are 8 spaces unless you explicitly use spaces :(
# This converts tabs (that are at the beginning of a line) to spaces, 
# using number of spaces specified in the command line argument.

# Usage: Takes in path to file to convert, then number of spaces per tab
# python tabs_to_spaces.py ./test_tab_file.txt 4
# Outputs the results to a file with the same name with __converted appended

def convert_tab_to_space(line, num_space_in_tab):
    i = 0
    if line[i] == '\t':
        spaces = ""
        # Start at beginning and convert tabs until hit a non tab
        while i < len(line):
            if line[i] == '\t':
                # Add specified number of space for each tab
                for j in range(0, num_space_in_tab):
                    spaces += " "
            else:
                break

            i += 1

        return spaces + line[i:]
    else:
        return line

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Expect 2 arguments: path to the file, and number of spaces in a tab")
        sys.exit(3);

    with open(sys.argv[1], 'r') as fp:
        filename = fp.name

        # Find extensions to produce good output file name
        split = filename.rfind('.')

        # If no file Extension is found. Searches for a period not found at the beginning or end,
        # and not preceded or followed by anything other than a letter or a number
        if (
                split == -1 or split == 0 or split == len(filename) - 1 
                or (not filename[split - 1].isalpha() and not filename[split - 1].isnumeric())
                or (not filename[split + 1].isalpha() and not filename[split + 1].isnumeric())
            ):
            wp = open(filename + '__converted', 'w')
            print("writing to : " + filename + '__converted')
        else:
            newEnd = '__converted' + fp.name[split:]
            wp = open(fp.name[:split] + newEnd, 'w')
            print("writing to : " + fp.name[:split] + newEnd)

        with wp:
            # Write to new filename
            for line in fp:
                wp.write(convert_tab_to_space(line, int(sys.argv[2])))

