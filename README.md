# AIoT 2024: Chatbot - Personal Daily Assistant

## Chatbot Persona Definition
The chatbot is designed to be a versatile personal assistant with a rich and nuanced personality. At its core, it embodies a blend of wit, humour, and deep empathy, just like a friend who can make you laugh during casual conversations but also provide profound and thoughtful advice when you are facing serious challenges.

The assistant's communication style is intentionally adaptable. In lighthearted moments, it uses humour and occasional sarcasm to keep interactions engaging and entertaining. However, when discussing more serious personal or interpersonal issues, the bot shifts to a more compassionate and serious mode of communication.

A key aspect of its personality is an unwavering commitment to personal growth. The chatbot does not just offer surface-level advice; it aims to challenge unhelpful thought patterns and encourage self-reflection. It employs relatable analogies and real-world examples to make its guidance more accessible and actionable.

The communication philosophy is thoughtfully balanced. The bot recognises that humour can be an effective way to make difficult conversations easier to handle, but it never employs humour at the expense of genuine understanding. Its main goal is to support users by offering a combination of entertainment and meaningful insights.

## Technical Approach
This chatbot leverages online OpenAI API, specifically utilising the GPT-4o-mini model, to create an intelligent conversation agent. The list of programming languages, frameworks, and libraries used includes:

- **Programming language:** Python
- **Model:** gpt-4o-mini (powerful but cheaper than the regular gpt-4o)
- **Frameworks and libraries:** `openai` for API interactions, `pickle` for memory management, and `python-dotenv` for secure configuration.

Instead of simply sending raw text to the API, the chatbot can construct sophisticated prompts that include a system message defining the bot's personality, the context of previous conversations, and the current user input. This function enables the chatbot to provide more coherent and contextually appropriate responses. Additionally, the chatbot can also utilise file-based storage to maintain conversation history, which allows for more persistent and stateful interactions, giving the bot a sense of continuity across different chat sessions. 

## Workflow Design 
![image](https://github.com/user-attachments/assets/36965bc7-eec3-49aa-ba56-447cbc1ca8d2)

- **Step 1 - Input processing:** When a user sends a message, the system first checks for existing conversation context. If a previous conversation history exists, it loads this context; if not, it initialises a new, empty context. 
- **Step 2 - Prompt construction:** Next, the chatbot constructs a comprehensive prompt, which includes a detailed system message defining the bot's personality and communication principles, the entire conversation history, and the current user input. 
- **Step 3 - API interaction:** The constructed prompt is then sent to the API, which uses the GPT-4o-mini model to generate a response, which is not just text but a response that aligns with the predefined persona and takes into account the conversation's context. 
- **Step 4 - Context management:** After receiving the response, the chatbot updates its conversation history, saving both the user's input and the assistant's reply. This updated context is then saved to a pickle file, allowing for continuity in future interactions.

## Prompt Engineering
The full system message used in the chatbot is shown below: 

```{text}
You are a witty and humorous personal assistant. You enjoy daily conversations, often with a touch of sarcasm. 
However, you also provide thoughtful and empathetic advice on handling difficult human interactions. 
Your responses should reflect this dual nature—lighthearted in casual conversation, but serious and insightful when discussing deeper topics.

Core Communication Principles:
- Provide practical, actionable guidance for personal and interpersonal challenges
- Use humour and occasional sarcasm to make difficult conversations more digestible
- Maintain a balance between compassionate support and direct feedback
- Adapt communication style to the user's emotional state and needs
- Prioritize personal growth, self-awareness, and constructive problem-solving

Interaction Style:
- Respond with wit, but never at the expense of genuine understanding
- Challenge unhelpful thought patterns gently but firmly
- Use relatable analogies and real-world examples
- Show deep empathy while avoiding toxic positivity
```

The system message clearly outlines essential communication principles. It not only instructs the AI to be witty or empathetic but also provides detailed guidelines about how to balance humour with serious support, challenge thought patterns constructively, and prioritize personal growth. To demonstrate how the prompt steer the conversation, let's consider three scenarios. 

- **Scenario 1 - Causal interaction:** When a user asks "Got any fun weekend plans?", we can expect the bot to respond in a witty manner. For instance, it may tell us some interesting activities with a lighthearted and relaxing tone. ![{CF36CDCA-6168-4E53-9717-EA84BA0C5791}](https://github.com/user-attachments/assets/bfcc51c4-379f-4724-ba38-dd3e49454173)
- **Scenario 2 - Serious personal challenge:** In this case, if the user tells the chatbot about his anxiety and mental conditions, the chatbot will use empathetic advice and constructive problem-solving principles to guide a supportive and actionable response, which is practical and shows deep empathy with a reduced sense of humour to soften the seriousness. ![{3B48AA8C-07CF-48BB-8CC5-05E2F56517E6}](https://github.com/user-attachments/assets/3837f96c-8462-4cd0-abc3-5c421cc23440)
- **Scenario 3 - Interpersonal conflict:** When a user complains about his/her social connection, the chatbot will respond in a pretty witty manner to make the conversation engaging, yet provides a constructive approach to solve the problem and avoids immediate judgement. ![{F61BB93D-840B-4855-8295-73BD7E2136CE}](https://github.com/user-attachments/assets/e2d5a5c0-24a3-4716-beb9-ac095a2d2155)

## Memory and Context Handling 
This implementation uses Python's `pickle` module to serialise and store conversation history, allowing the bot to maintain a sense of continuity across interactions. Conversations are stored as a list of dictionaries, with each dictionary representing a message and its role  (either from the user or the chatbot). this chronological record allows the chatbot to reference previous exchanges and maintain context. Specifically, the `load_context()` and `save_context()` methods handle the technical details of reading from and writing to a file. This means that even if the chat application is closed and reopened, the conversation history can still be retrieved and continued. 

## User Interaction and Interface Design
The system utilises a command-line interface (CLI) for users to interact with the assistant. When the chat begins, users are greeted with a welcoming message that includes example conversation starters, helping them understand how to interact with the bot. 

![{F580223F-7B81-4FC2-A8EE-5BB64F82799B}](https://github.com/user-attachments/assets/4ba4f495-1e9a-4ea4-82d5-4f3ab086e3e1) 

The interaction flow is very intuitive: users type messages, and the bot responds. However, the responding speed is slow for questions that require long and complicated answers due to the request-sending process to OpenAI API. When users want to end the conversation, simply type "exit" and the program will stop. 

## Additional 
There are some limitations to this system. First, it used predefined example conversation starters, which is not flexible and may limit what the chatbot can do. Next, regarding memory management, the current implementation has a fixed token limit and does not automatically truncate older messages, which could potentially lead to memory overhead for very long conversations. Last but not least, although the CLI is simple and straightforward, the user interface can be expanded to more sophisticated interfaces such as a graphical user interface (GUI) or a web-based platform to enhance user experience visually. 


