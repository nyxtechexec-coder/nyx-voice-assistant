import 'package:flutter/material.dart';

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
      home: const Scaffold(
        body: Center(
          child: Text('Nyx Voice Assistant scaffold is ready'),
        ),
      ),
    );
  }
}
