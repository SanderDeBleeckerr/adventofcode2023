WORD = "XMAS"
FILE = 'day4_input.txt'



def main():
    '''counts occurences of the word xmas written in different directions from a gibberish file'''
    grid = load_grid(FILE)
    # find_xmas_occurences(grid)

    find_x_of_two_mas_occurences(grid)


def find_x_of_two_mas_occurences(grid):
    center_letter = "A"
    count = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==center_letter and has_two_times_mas_via_adjecent_coords((r,c),grid,rows, cols):
                count=count+1
    print(count)


def find_xmas_occurences(grid):
    word = "XMAS"
    count = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if(grid[r][c]==word[0]):
                coords = (r,c)
                i = 1
                adj_coords = find_adjecent_coords(coords)
                matching_adj_coords = find_coords_that_match_letter(word[i],adj_coords, grid);
                for matching_adj_coord in matching_adj_coords:
                    count = count + search_further_in_same_direction(coords, matching_adj_coord, i, grid, rows, cols, word)
    print(count)


def find_adjecent_coords(coords):
    r, c = coords
    return [(r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)]

def has_two_times_mas_via_adjecent_coords(coords, grid, rows, cols):
    r, c = coords
    if r == 0 or c == 0:
        return False
    if r == rows-1 or c == cols-1:
        return False

    has_diagonal_mas = (grid[r+1][c-1]=='M' and grid[r-1][c+1]=='S') or (grid[r+1][c-1]=='S' and grid[r-1][c+1]=='M')   
    has_reverse_diagonal_mas = (grid[r+1][c+1]=='M' and grid[r-1][c-1]=='S') or (grid[r+1][c+1]=='S' and grid[r-1][c-1]=='M')   
    return has_diagonal_mas and has_reverse_diagonal_mas

def search_further_in_same_direction(coords, matching_adj_coord, index_in_word, grid, rows, cols, word):
    i = index_in_word
    i+=1

    next_coord = get_next_coord(coords, matching_adj_coord)
    r, c = next_coord
    if(r<0 or c<0):
        return 0
    elif(c>=cols or r>=rows):
        return 0
    elif(grid[r][c]==word[i]):
        if(i==len(word)-1):
            return 1
        else:
            return search_further_in_same_direction(matching_adj_coord, next_coord, i, grid, rows, cols, word)
    else:
        return 0

def get_next_coord(coord1, coord2):
    delta = (coord2[0] - coord1[0], coord2[1] - coord1[1])
    next_coord = (coord2[0] + delta[0], coord2[1] + delta[1])
    return next_coord


def find_coords_that_match_letter(letter, coords, grid):
    matching_coords = list()
    rows, cols = len(grid), len(grid[0])

    for coord in coords:
        r, c = coord
        if(r<0 or c<0):
            continue
        if(c>=cols or r>=rows):
            continue

        if(grid[r][c]==letter):
            matching_coords.append(coord)
    return matching_coords

def load_grid(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip().replace(" ", "")) for line in file if line.strip()]
    return grid


if __name__ == "__main__":
    main()