#!/usr/bin/env python3
"""
Basic Chat Sender - Educational Implementation
This script demonstrates the fundamental concepts of sending messages in a chat system.
Concepts covered: user input, message formatting, timestamp, basic validation.
"""

import datetime
import json
import os

class BasicChatSender:
    def __init__(self, username=None, chat_file="chat_messages.txt"):
        """
        Initialize the chat sender with a username and chat file location.
        
        Args:
            username (str): The username for this chat session
            chat_file (str): Path to the file where messages will be stored
        """
        self.username = username or self.get_username()
        self.chat_file = chat_file
        self.ensure_chat_file_exists()
    
    def get_username(self):
        """Get username from user input with basic validation."""
        while True:
            username = input("Enter your username: ").strip()
            if username and len(username) >= 2:
                return username
            print("Username must be at least 2 characters long. Please try again.")
    
    def ensure_chat_file_exists(self):
        """Create the chat file if it doesn't exist."""
        if not os.path.exists(self.chat_file):
            with open(self.chat_file, 'w', encoding='utf-8') as f:
                f.write("=== Chat Session Started ===\n")
            print(f"Created new chat file: {self.chat_file}")
    
    def format_message(self, message_text):
        """
        Format a message with timestamp and username.
        
        Args:
            message_text (str): The raw message text
            
        Returns:
            dict: Formatted message with metadata
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        formatted_message = {
            "timestamp": timestamp,
            "username": self.username,
            "message": message_text,
            "message_id": self.generate_message_id()
        }
        
        return formatted_message
    
    def generate_message_id(self):
        """Generate a simple message ID based on timestamp."""
        return int(datetime.datetime.now().timestamp() * 1000)
    
    def validate_message(self, message):
        """
        Basic message validation.
        
        Args:
            message (str): Message to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not message.strip():
            return False, "Message cannot be empty"
        
        if len(message) > 500:
            return False, "Message too long (max 500 characters)"
        
        # Check for basic prohibited content
        prohibited_words = ["spam", "test123"]  # Simple example
        if any(word in message.lower() for word in prohibited_words):
            return False, "Message contains prohibited content"
        
        return True, ""
    
    def send_message(self, message_text):
        """
        Send a message to the chat.
        
        Args:
            message_text (str): The message to send
            
        Returns:
            bool: True if message was sent successfully, False otherwise
        """
        # Validate the message
        is_valid, error_msg = self.validate_message(message_text)
        if not is_valid:
            print(f"❌ Message not sent: {error_msg}")
            return False
        
        # Format the message
        formatted_message = self.format_message(message_text)
        
        try:
            # Write message to file (simulating sending to a chat server)
            with open(self.chat_file, 'a', encoding='utf-8') as f:
                # Write in both human-readable and JSON format for educational purposes
                human_format = f"[{formatted_message['timestamp']}] {formatted_message['username']}: {formatted_message['message']}\n"
                json_format = f"JSON: {json.dumps(formatted_message)}\n"
                
                f.write(human_format)
                f.write(json_format)
                f.write("-" * 50 + "\n")
            
            print(f"✅ Message sent successfully!")
            print(f"📝 Saved to: {self.chat_file}")
            return True
            
        except Exception as e:
            print(f"❌ Error sending message: {e}")
            return False
    
    def show_chat_info(self):
        """Display information about the current chat session."""
        print("\n" + "="*50)
        print("📱 BASIC CHAT SENDER")
        print("="*50)
        print(f"👤 Username: {self.username}")
        print(f"📁 Chat file: {self.chat_file}")
        print(f"🕒 Session started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
    
    def show_help(self):
        """Display help information."""
        help_text = """
📚 CHAT SENDER HELP
Commands:
  • Type any message to send it
  • /help - Show this help
  • /info - Show chat session info
  • /history - Show recent messages
  • /clear - Clear the terminal
  • /quit or /exit - Exit the chat

💡 Tips:
  • Messages are limited to 500 characters
  • Empty messages cannot be sent
  • All messages are saved with timestamps
        """
        print(help_text)
    
    def show_recent_messages(self, count=5):
        """Show recent messages from the chat file."""
        try:
            if not os.path.exists(self.chat_file):
                print("No chat history found.")
                return
            
            with open(self.chat_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Filter for human-readable message lines (not JSON or separators)
            message_lines = [line for line in lines if line.startswith('[') and ']:' in line]
            recent_messages = message_lines[-count:]
            
            print(f"\n📜 Recent {len(recent_messages)} messages:")
            print("-" * 40)
            for msg in recent_messages:
                print(msg.strip())
            print("-" * 40)
            
        except Exception as e:
            print(f"Error reading chat history: {e}")
    
    def run_interactive_chat(self):
        """Run the interactive chat interface."""
        self.show_chat_info()
        self.show_help()
        
        print("\n🚀 Chat is ready! Start typing messages (type /help for commands)")
        
        while True:
            try:
                # Get user input
                user_input = input(f"\n{self.username}> ").strip()
                
                # Handle special commands
                if user_input.lower() in ['/quit', '/exit']:
                    print("👋 Goodbye!")
                    break
                elif user_input.lower() == '/help':
                    self.show_help()
                elif user_input.lower() == '/info':
                    self.show_chat_info()
                elif user_input.lower() == '/history':
                    self.show_recent_messages()
                elif user_input.lower() == '/clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                elif user_input.startswith('/'):
                    print(f"❓ Unknown command: {user_input}")
                    print("Type /help to see available commands")
                else:
                    # Send the message
                    if user_input:
                        self.send_message(user_input)
                    else:
                        print("💭 Type a message to send it!")
                        
            except KeyboardInterrupt:
                print("\n\n👋 Chat interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")

def main():
    """Main function to run the chat sender."""
    print("🎯 Welcome to Basic Chat Sender!")
    print("This program demonstrates fundamental chat sending concepts.")
    
    # Create and run the chat sender
    chat_sender = BasicChatSender()
    chat_sender.run_interactive_chat()

if __name__ == "__main__":
    main()