import usrInput


def main():
    # Get user input for the file path
    filePath = usrInput.getUsrInput("Please enter the file or directory path")
    
    # Call the checkPath function
    dataFiles = []
    result = usrInput.checkPath(filePath, dataFiles)
    

if __name__ == "__main__":
    main()