import '../../../core/network/api_client.dart';
import '../models/chat_message.dart';

class ChatRepository {
  ChatRepository({ApiClient? apiClient})
      : _apiClient = apiClient ?? ApiClient(baseUrl: 'http://localhost:8000');

  final ApiClient _apiClient;

  Future<List<ChatMessage>> loadMessages({String conversationId = 'demo'}) async {
    try {
      final data = await _apiClient.get('/conversations/$conversationId/messages');
      return (data as List)
          .map((item) => ChatMessage(
                id: item['id'] as String,
                role: item['role'] as String,
                content: item['content'] as String,
              ))
          .toList();
    } catch (_) {
      return const [
        ChatMessage(id: '1', role: 'assistant', content: 'Hello, I am Nyx. Ready when you are.'),
      ];
    }
  }
}
