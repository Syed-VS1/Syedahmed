import os.path


def checkPath(filePath, dataFiles):
    if not os.path.exists(filePath):
        print(filePath + " does not exist.")
        return 1
    elif os.path.isdir(filePath):
        for file in os.listdir(filePath):
            checkPath(os.path.join(filePath, file), dataFiles)
    elif filePath.endswith("_formatted.json"):

        print("already formatted JSON file:  {filePath}")
    elif filePath.endswith((".json", ".pdf")):
        dataFiles.append(filePath)
    return tuple(dataFiles)

def getUsrInput(msg):

    prompt =f"{msg}: "

    userInput = input(prompt).strip()
    return userInput
