import '../models/chat_message.dart';

class ChatState {
  final List<ChatMessage> messages;

  const ChatState({required this.messages});

  factory ChatState.initial() => const ChatState(messages: []);

  ChatState copyWith({List<ChatMessage>? messages}) {
    return ChatState(messages: messages ?? this.messages);
  }
}
