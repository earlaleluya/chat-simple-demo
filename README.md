# Basic Chat System - Educational Implementation

This project demonstrates fundamental concepts of chat communication using Python via terminal.

## 📁 Files

- `chat_send.py` - Interactive chat sender with message validation and formatting
- `chat_receive.py` - Real-time chat receiver that monitors for new messages
- `chat_messages.txt` - Chat file (created automatically when first message is sent)

## 🎯 Learning Objectives

This implementation teaches:
- **User Input Handling**: Getting and validating user input
- **Message Formatting**: Structuring messages with timestamps and metadata
- **File I/O Operations**: Reading from and writing to files
- **Real-time Monitoring**: Checking for file changes continuously
- **Data Validation**: Ensuring message quality and security
- **JSON Processing**: Storing and parsing structured data
- **Error Handling**: Managing exceptions gracefully
- **Interactive CLI**: Building user-friendly command-line interfaces
- **Multi-threading**: Most importantly, you will learn how to handle deadlock in a multi-threaded process

## 🚀 How to Run

### Method 1: Test the Complete Chat System

1. **Start the Receiver** (in first terminal):
   ```powershell
   cd "c:\Users\Earl Keifer\Desktop\coe128"
   python chat_receive.py
   ```

2. **Start the Sender** (in second terminal):
   ```powershell
   cd "c:\Users\Earl Keifer\Desktop\coe128"
   python chat_send.py
   ```

3. **Send Messages**: Type messages in the sender terminal and watch them appear in the receiver terminal!

### Method 2: Just Send Messages

Run only the sender to create and send messages:
```powershell
cd "c:\Users\Earl Keifer\Desktop\coe128"
python chat_send.py
```

## 💬 Chat Sender Features

- **Interactive Interface**: User-friendly terminal chat interface
- **Username Management**: Personalized messaging with usernames
- **Message Validation**: Prevents empty messages and enforces character limits
- **Timestamp Integration**: All messages include precise timestamps
- **Command System**: Built-in commands for enhanced functionality
- **Message History**: View recent chat messages
- **File Management**: Automatic chat file creation and management

### Available Commands:
- `/help` - Show help information
- `/info` - Display chat session details
- `/history` - Show recent messages
- `/clear` - Clear terminal screen
- `/quit` or `/exit` - Exit the chat

## 📡 Chat Receiver Features

- **Real-time Monitoring**: Continuously watches for new messages
- **Automatic Display**: Shows new messages as they arrive
- **Message History**: Displays existing messages on startup
- **Duplicate Prevention**: Ensures messages aren't displayed multiple times
- **Error Handling**: Gracefully handles file access issues

## 🏗️ Technical Implementation

### Message Structure
Each message is stored in two formats:
```
Human-readable: [2024-10-03 14:30:15] John: Hello, world!
JSON: {"timestamp": "2024-10-03 14:30:15", "username": "John", "message": "Hello, world!", "message_id": 1696348215000}
```

### File Communication
- Messages are written to `chat_messages.txt`
- Receiver monitors file changes every 2 seconds
- JSON format enables structured data processing
- Human-readable format allows manual inspection

### Validation Rules
- Messages must be 2-500 characters
- Usernames must be at least 2 characters
- Basic content filtering (customizable)
- Empty message prevention

## 🎓 Educational Concepts Demonstrated

1. **Input/Output (I/O)**
   - File reading and writing
   - User input collection and validation
   - Terminal output formatting

2. **Data Structures**
   - Dictionary usage for message formatting
   - JSON serialization and deserialization
   - List management for message history

3. **Error Handling**
   - Try-catch blocks for file operations
   - Input validation and error messages
   - Graceful exception management

4. **Real-time Programming**
   - Polling-based file monitoring
   - Sleep intervals for system efficiency
   - Continuous loop management

5. **User Interface Design**
   - Command-line interface best practices
   - Help systems and user guidance
   - Visual formatting with emojis and symbols

## 🔧 Customization Ideas

- Modify validation rules in `validate_message()`
- Change monitoring interval in `monitor_chat()`
- Add encryption for message security
- Implement network communication instead of file-based
- Add user authentication features
- Create message threading or channels
- Add file attachment support

## 🐛 Common Issues

1. **"Chat file not found"**: Start `chat_send.py` first to create the chat file
2. **Permission errors**: Ensure write access to the directory
3. **Encoding issues**: Files use UTF-8 encoding for international character support

## 📚 Your Assignment

After understanding this implementation, consider exploring:
- Modify the program so that two or more computers can communicate using Socket programming for network communication.
- Apply multi-threading so that you have only one file `chat.py` which you can send and receive messages, simultenously and smoothly.
- Optionally, you can implement encryption.