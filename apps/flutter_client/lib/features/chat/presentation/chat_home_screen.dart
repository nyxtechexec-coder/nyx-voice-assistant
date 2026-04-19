import 'package:flutter/material.dart';

class ChatHomeScreen extends StatelessWidget {
  const ChatHomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Nyx Voice Assistant')),
      body: Column(
        children: const [
          Expanded(
            child: Center(
              child: Text('Conversation view will live here'),
            ),
          ),
          Padding(
            padding: EdgeInsets.all(16),
            child: Text('Push-to-talk and transcript controls will be added next'),
          )
        ],
      ),
    );
  }
}
