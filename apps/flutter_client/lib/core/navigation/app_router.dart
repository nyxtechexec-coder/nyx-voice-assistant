import 'package:flutter/material.dart';
import '../../features/auth/presentation/login_screen.dart';
import '../../features/chat/presentation/chat_home_screen.dart';

class AppRouter {
  static const login = '/login';
  static const chatHome = '/chat';

  static final routes = <String, WidgetBuilder>{
    login: (_) => const LoginScreen(),
    chatHome: (_) => const ChatHomeScreen(),
  };
}
