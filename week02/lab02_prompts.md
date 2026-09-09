# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

python
def count_vowels(text: str) -> int:
    return sum(character.lower() in "aeiou" for character in text)


### Antigravity CLI

 Installed and authenticated successfully. Version: 1.1.23

## Shared task

## Shared prompt
```text
copilot -p "Write a Python function named count_vowels(text: str) -> int that counts the vowels a, e, i, o, and u regardless of case. Do not count y. Return the total number of vowels in the string."
agy -p "Write a Python function named count_vowels(text: str) -> int that counts the vowels a, e, i, o, and u regardless of case. Do not count y."
```

### Copilot CLI observations

 Copilot CLI approach seemed very simple to me. It almost seemed too simple. It was suggesting to create a variable tosum the times it read 'a,e,i,o,u'. Just from initially looking at it, it seems too good and easy to be true. I would be interested if it suggested anything to confirm the letter y is not included. 

### Antigravity CLI observations

 On the other hand with Antigravity, it suggested something very similar. An integer that returns the count of the count of a,e,i,o,u. There is also something else at the bottom that says something about vowels = set("aeiouAEIOU) which I am assuming is just testing case sensative vowels. I think I will be using this one.  
### Comparison

 Copilot gave me a short and compact version of the function. It lowers each character and checks if it’s in the string of vowels. The code works, but it does extra lowercase operations on every character. Antigravity’s version is a little more detailed and uses a set containing both uppercase and lowercase vowels. I liked this because it makes checking faster and easier to understand because the set already includes every single vowel form. Both tools produced correct solutions, but Antigravity’s approach feels clearer and more organized. Because of that, I decided to use the Antigravity version in my final code. 

## Test-guided implementation

 When I ran the Week 02 tests, they helped confirm that each function behaved exactly the way the instructions described. The tests covered normal inputs, edge cases, and tricky situations, which made it easy to see whether the functions matched the expected contracts. For count_vowels, the tests checked uppercase vowels, strings with no vowels, and strings containing “y,” which should not be counted. Seeing these pass showed that the set‑based approach was correct. I also reviewed the behavior of make_greeting and is_even to make sure they handled empty strings and negative numbers properly. Since everything passed, I didn’t need major revisions, but I verified that the logic was clear and consistent. The final code fully matches the required behavior.

## Preferred tool combination

When I look at how each tool fits into my workflow, they all serve different purposes. The browser chat is the easiest place for me to think through ideas, ask questions, and get explanations in normal language. GitHub Copilot in VS Code is helpful when I’m already writing code and want quick suggestions without leaving the editor. Copilot CLI feels more direct and fast for generating small functions or checking code behavior from the terminal. Antigravity CLI is the most structured and gives detailed reasoning, which helps when I want a clearer breakdown of changes. Right now, I prefer using browser chat plus Antigravity because they give me the most guidance. But if I were working on a bigger project with lots of files open, I could see myself switching to VS Code Copilot more often.

