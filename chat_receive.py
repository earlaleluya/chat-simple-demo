#!/usr/bin/env python3
"""
Basic Chat Receiver - Educational Implementation
This script demonstrates the fundamental concepts of receiving and displaying chat messages.
Concepts covered: file monitoring, message parsing, real-time display.
"""

import time
import json
import os
from datetime import datetime

class BasicChatReceiver:
    def __init__(self, chat_file="chat_messages.txt"):
        """
        Initialize the chat receiver.
        
        Args:
            chat_file (str): Path to the chat file to monitor
        """
        self.chat_file = chat_file
        self.last_position = 0
        self.displayed_messages = set()
    
    def check_chat_file_exists(self):
        """Check if the chat file exists."""
        if not os.path.exists(self.chat_file):
            print(f"❌ Chat file not found: {self.chat_file}")
            print("💡 Start the chat_send.py script first to create messages!")
            return False
        return True
    
    def read_new_messages(self):
        """
        Read new messages from the chat file since last check.
        
        Returns:
            list: List of new message dictionaries
        """
        new_messages = []
        
        try:
            with open(self.chat_file, 'r', encoding='utf-8') as f:
                f.seek(self.last_position)
                new_content = f.read()
                self.last_position = f.tell()
            
            if new_content.strip():
                # Parse messages from the new content
                lines = new_content.split('\n')
                
                for line in lines:
                    line = line.strip()
                    if line.startswith('JSON: '):
                        try:
                            # Parse JSON message
                            json_str = line[6:]  # Remove 'JSON: ' prefix
                            message_data = json.loads(json_str)
                            
                            # Avoid duplicate messages
                            msg_id = message_data.get('message_id')
                            if msg_id and msg_id not in self.displayed_messages:
                                new_messages.append(message_data)
                                self.displayed_messages.add(msg_id)
                                
                        except json.JSONDecodeError:
                            continue  # Skip malformed JSON
            
        except Exception as e:
            print(f"❌ Error reading messages: {e}")
        
        return new_messages
    
    def format_message_display(self, message_data):
        """
        Format a message for display.
        
        Args:
            message_data (dict): Message data from JSON
            
        Returns:
            str: Formatted message for display
        """
        timestamp = message_data.get('timestamp', 'Unknown time')
        username = message_data.get('username', 'Unknown user')
        message_text = message_data.get('message', '')
        
        # Create a visually appealing format
        time_part = timestamp.split(' ')[1]  # Get just the time part
        formatted = f"💬 [{time_part}] {username}: {message_text}"
        
        return formatted
    
    def display_message(self, message_data):
        """
        Display a single message.
        
        Args:
            message_data (dict): Message data to display
        """
        formatted_msg = self.format_message_display(message_data)
        print(formatted_msg)
    
    def show_receiver_info(self):
        """Display information about the chat receiver."""
        print("\n" + "="*50)
        print("📱 BASIC CHAT RECEIVER")
        print("="*50)
        print(f"📁 Monitoring file: {self.chat_file}")
        print(f"🕒 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("🔄 Checking for new messages every 2 seconds...")
        print("📝 Press Ctrl+C to exit")
        print("="*50)
    
    def show_existing_messages(self, count=10):
        """
        Show existing messages from the chat file.
        
        Args:
            count (int): Maximum number of recent messages to show
        """
        if not os.path.exists(self.chat_file):
            return
        
        try:
            messages = []
            with open(self.chat_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Extract JSON messages
            for line in lines:
                line = line.strip()
                if line.startswith('JSON: '):
                    try:
                        json_str = line[6:]
                        message_data = json.loads(json_str)
                        messages.append(message_data)
                    except json.JSONDecodeError:
                        continue
            
            if messages:
                print(f"\n📜 Showing last {min(count, len(messages))} messages:")
                print("-" * 50)
                
                # Show the most recent messages
                recent_messages = messages[-count:]
                for msg in recent_messages:
                    formatted_msg = self.format_message_display(msg)
                    print(formatted_msg)
                    # Track displayed messages to avoid duplicates
                    msg_id = msg.get('message_id')
                    if msg_id:
                        self.displayed_messages.add(msg_id)
                
                print("-" * 50)
                
                # Update file position to end
                with open(self.chat_file, 'r', encoding='utf-8') as f:
                    f.seek(0, 2)  # Seek to end
                    self.last_position = f.tell()
            else:
                print("📭 No messages found yet.")
                
        except Exception as e:
            print(f"❌ Error reading existing messages: {e}")
    
    def monitor_chat(self):
        """
        Main monitoring loop - continuously check for new messages.
        """
        if not self.check_chat_file_exists():
            return
        
        self.show_receiver_info()
        
        # Show existing messages first
        self.show_existing_messages()
        
        print("\n🔍 Monitoring for new messages...")
        
        try:
            while True:
                # Check for new messages
                new_messages = self.read_new_messages()
                
                # Display any new messages
                for message in new_messages:
                    print("🆕 New message received:")
                    self.display_message(message)
                
                # Wait before checking again
                time.sleep(2)
                
        except KeyboardInterrupt:
            print("\n\n👋 Chat receiver stopped. Goodbye!")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
    
    def show_help(self):
        """Display help information."""
        help_text = """
📚 CHAT RECEIVER HELP

This program monitors a chat file for new messages and displays them in real-time.

🎯 Purpose:
  • Demonstrates message receiving concepts
  • Shows file-based communication
  • Illustrates real-time monitoring

🔧 How it works:
  1. Monitors the chat_messages.txt file
  2. Detects new messages added by chat_send.py
  3. Displays messages in a formatted way
  4. Updates every 2 seconds

💡 To test:
  1. Run this receiver: python chat_receive.py
  2. In another terminal: python chat_send.py
  3. Send messages and watch them appear here!

⚠️  Note: Both scripts should be in the same directory
        """
        print(help_text)

def main():
    """Main function to run the chat receiver."""
    print("🎯 Welcome to Basic Chat Receiver!")
    print("This program demonstrates fundamental chat receiving concepts.")
    
    # Show help if no chat file exists
    receiver = BasicChatReceiver()
    if not receiver.check_chat_file_exists():
        receiver.show_help()
        return
    
    # Start monitoring
    receiver.monitor_chat()

if __name__ == "__main__":
    main()