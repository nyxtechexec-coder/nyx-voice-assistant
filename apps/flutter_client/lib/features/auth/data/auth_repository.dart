import '../../../core/network/api_client.dart';
import '../models/login_result.dart';

class AuthRepository {
  AuthRepository({ApiClient? apiClient})
      : _apiClient = apiClient ?? ApiClient(baseUrl: 'http://localhost:8000');

  final ApiClient _apiClient;

  Future<LoginResult> login(String email, String password) async {
    final data = await _apiClient.post('/auth/login', {
      'email': email,
      'password': password,
    });
    return LoginResult(
      accessToken: data['access_token'] as String,
      refreshToken: data['refresh_token'] as String,
      userId: data['user_id'] as String,
    );
  }
}
