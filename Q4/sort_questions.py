'''
    Read questions file and sort questions in correct order
    Write sorted questions in soretdQuestions.txt file
'''
questionsMap = {}
with open('questions.txt', 'r') as r:
    # Loop through each line of file
    for line in r:
        # Remove extra spaces in file
        trimmedLine = line.strip()
        # Check if the line is a question
        if trimmedLine.startswith('Q'):
            # Grab first character of file
            questionNumber = int(trimmedLine[1])
            # check if question exist in dictionary
            if questionNumber in questionsMap:
                # append line to same question
                questionsMap[questionNumber] = questionsMap[questionNumber] + '\n' + line
            else:
                # stor new question number with data
                questionsMap[questionNumber] = line
        else:
            # Append no question line to previous question
            lastKey = list(questionsMap)[-1]
            questionsMap[lastKey] = questionsMap[lastKey] + '\n' + line

# Sort dictionary inorder
sortedQuestion = {k: questionsMap[k] for k in sorted(questionsMap)}

# Write dictionary to file
with open("sortedQuestions.txt", 'w') as f: 
    for key, value in sortedQuestion.items(): 
        f.write(value)
