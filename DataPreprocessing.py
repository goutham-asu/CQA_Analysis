
import Files

import HelperClass as HC

"""
Main Function
"""
def main():

    #Step 1. Parse all the input files
    print(Files.InputFiles)

    helperObj = HC.HelperClass()

    for file in Files.InputFiles.keys():
        try:
            helperObj.ParseFile(Files.InputFiles[file], file )

        except:
            print("Error Parsing File")


    helperObj.PairCommentWithPosts()


    #Step 2. Create Question Answer Pairs
    questionAnswerPairs = helperObj.CreateQuestionAnswerPair()

    # Step 3. We have created Q/A pairs. Now we need to extract the features.
    helperObj.ExtractAllFeatures()
    helperObj.CreateLabels()

    c = 20


if __name__ == "__main__":
    #Call main function
    main()
    print("End")