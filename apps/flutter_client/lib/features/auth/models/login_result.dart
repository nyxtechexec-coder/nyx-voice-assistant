class LoginResult {
  final String accessToken;
  final String refreshToken;
  final String userId;

  const LoginResult({
    required this.accessToken,
    required this.refreshToken,
    required this.userId,
  });
}
