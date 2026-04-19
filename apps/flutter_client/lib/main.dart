import 'package:flutter/material.dart';
import 'core/navigation/app_router.dart';

void main() {
  runApp(const NyxVoiceAssistantApp());
}

class NyxVoiceAssistantApp extends StatelessWidget {
  const NyxVoiceAssistantApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Nyx Voice Assistant',
      theme: ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal)),
      initialRoute: AppRouter.login,
      routes: AppRouter.routes,
    );
  }
}
