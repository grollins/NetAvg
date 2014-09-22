from sys import argv
from os.path import join
from glob import glob
from prody import parsePDB, writePDB


MAX_FRAMES = 1000


def main():
    directory_with_pdbs = argv[1]
    output_filename = argv[2]
    search_string = join(directory_with_pdbs, '*.pdb')
    path_list = glob(search_string)
    
    if len(path_list) > MAX_FRAMES:
        raise RuntimeError('Got %d frames, but only up to %d frames are allowed.')
    else:
        pass

    atom_group = parsePDB(path_list[0])
    for i, path in enumerate(path_list):
        if i == 0:
            continue
        else:
            p = parsePDB(path)
            atom_group.addCoordset(p)
    writePDB(output_filename, atom_group)

if __name__ == '__main__':
    main()
