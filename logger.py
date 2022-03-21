
class LogX:
    def writeLog(inputString):
        try:
            text_file = open("log.txt", "w")
            n = text_file.write(inputString)
            text_file.close()
        except:
            print("Logging Error")