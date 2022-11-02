import os

# Step 1: Locate your directory with subdirectories and files.
# TODO: inside parenthesis insert absolute path to parent directory (containing directories with pdf files)
parentdirpath = os.path.abspath("C:/Users/")
# TODO: inside parenthesis insert same path as above (creates a list of all directories in parent folder)
dirlist = os.listdir("C:/Users/")

# step 2: iterate through list of directories, create path to each directory and create list of files
for dir in dirlist:
    subdirpath = os.path.join(parentdirpath, dir)
    filelist = os.listdir(subdirpath)
    print()

    # step 3: iteraterate over list of files and create a corresponding magick expression
    for file in filelist:
        filepathpdf = os.path.join(parentdirpath, dir, file)
        filenamebase, file_extension = os.path.splitext(file)
        filenamejpg = filenamebase + ".jpg"
        filepathjpg = os.path.join(parentdirpath, dir, filenamejpg)
        # if file is a pdf, create magick command for current file, keep high quality.
        if file_extension == ".pdf":
            magick = "magick convert -density 150 -trim " + filepathpdf + " -quality 100 -sharpen 0x1.0 " + filepathjpg
            # process magick command
            os.system(magick)
            print(file + " transformed to " + filenamejpg)
            # remove original pdf file
            os.remove(filepathpdf)
            print(file + " has been removed")
