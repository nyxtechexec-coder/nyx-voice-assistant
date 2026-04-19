import 'package:flutter/material.dart';

class VoiceControls extends StatelessWidget {
  final VoidCallback? onTap;

  const VoiceControls({super.key, this.onTap});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton.icon(
      onPressed: onTap,
      icon: const Icon(Icons.mic),
      label: const Text('Push to Talk'),
    );
  }
}
