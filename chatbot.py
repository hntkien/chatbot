import openai
import pickle
import os
from dotenv import load_dotenv

class MyChatBot:
    def __init__(self, api_key, context_file='chat_memory.pkl'):
        """
        Initializes the chatbot with API key and context file.

        Args:
            api_key (str): OpenAI API key.
            context_file (str): Path to the file storing conversation history.
        """
        openai.api_key = api_key
        self.context_file = context_file
        self.system_message = """
        You are a witty and humorous personal assistant. You enjoy daily conversations, often with a touch of sarcasm. 
        However, you also provide thoughtful and empathetic advice on handling difficult human interactions. 
        Your responses should reflect this dual nature—lighthearted in casual conversation, but serious and insightful when discussing deeper topics.

        Core Communication Principles:
        - Provide practical, actionable guidance for personal and interpersonal challenges
        - Use humor and occasional sarcasm to make difficult conversations more digestible
        - Maintain a balance between compassionate support and direct feedback
        - Adapt communication style to the user's emotional state and needs
        - Prioritize personal growth, self-awareness, and constructive problem-solving

        Interaction Style:
        - Respond with wit, but never at the expense of genuine understanding
        - Challenge unhelpful thought patterns gently but firmly
        - Use relatable analogies and real-world examples
        - Show deep empathy while avoiding toxic positivity
        """
    
    def initial_greeting(self):
        """
        Provides an initial greeting with example questions.

        Returns:
            str: Greeting message with example questions.
        """
        greeting = (
            "Hello! I'm your personal assistant.\n\n"
            "If you are not familiar with me, here are some things you can ask me:\n"
            "- \"How do I deal with a stubborn colleague?\"\n"
            "- \"Any tips for handling stress?\"\n"
            "- \"What's the best way to apologize sincerely?\"\n"
            "- \"Tell me a funny story!\"\n"
            "- \"Why do people ghost others?\"\n\n"
            "So, what's on your mind today?"
        )
        return greeting

    def load_context(self):
        """
        Loads the conversation context from storage.

        Returns:
            list: Conversation history as a list of messages.
        """
        if os.path.exists(self.context_file):
            with open(self.context_file, 'rb') as file:
                return pickle.load(file)
        return []

    def save_context(self, context):
        """
        Saves the conversation context to storage.

        Args:
            context (list): Conversation history to save.
        """
        with open(self.context_file, 'wb') as file:
            pickle.dump(context, file)

    def build_prompt(self, user_input, context):
        """
        Constructs the complete prompt for the GPT model.

        Args:
            user_input (str): The user's input message.
            context (list): Previous messages to maintain conversation continuity.

        Returns:
            dict: Structured prompt ready for the OpenAI API.
        """
        messages = [{"role": "system", "content": self.system_message}]
        messages.extend(context)
        messages.append({"role": "user", "content": user_input})
        return {"messages": messages}

    def get_gpt_response(self, prompt):
        """
        Sends a prompt to the OpenAI API and retrieves the chatbot's response.

        Args:
            prompt (dict): Structured prompt containing conversation context.

        Returns:
            str: The chatbot's reply.
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  # Specify the model
                messages=prompt['messages'],
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except openai.OpenAIError as e:
            return f"Sorry, I encountered an issue: {e}"

    def chat(self, user_input):
        """
        Manages the complete chatbot workflow: input processing, response generation, and memory handling.

        Args:
            user_input (str): The user's input message.

        Returns:
            str: The chatbot's reply.
        """
        # Load the existing context
        context = self.load_context()
        
        # Build the prompt with the current context
        prompt = self.build_prompt(user_input, context)
        
        # Get a response from the API
        assistant_reply = self.get_gpt_response(prompt)
        
        # Update the context with the latest exchange
        context.append({"role": "user", "content": user_input})
        context.append({"role": "assistant", "content": assistant_reply})
        self.save_context(context)
        
        return assistant_reply
    
if __name__ == "__main__":
    # Load APi Key from .env
    load_dotenv() 
    api_key = os.getenv('OPENAI_API_KEY')
    chatbot = MyChatBot(api_key=api_key)
    
    # Display the initial greeting
    print(chatbot.initial_greeting())
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            print("Chat ended. Goodbye!")
            break
        
        # Get and print the chatbot's reply
        reply = chatbot.chat(user_input)
        print(f"Assistant: {reply}")
