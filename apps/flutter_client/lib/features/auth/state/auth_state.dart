class AuthState {
  final bool isAuthenticated;
  final String? accessToken;

  const AuthState({required this.isAuthenticated, this.accessToken});

  factory AuthState.initial() => const AuthState(isAuthenticated: false);
}
