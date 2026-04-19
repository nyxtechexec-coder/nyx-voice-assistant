import '../models/chat_message.dart';

class ChatRepository {
  Future<List<ChatMessage>> loadMessages() async {
    return const [
      ChatMessage(id: '1', role: 'assistant', content: 'Hello, I am Nyx. Ready when you are.'),
    ];
  }
}
