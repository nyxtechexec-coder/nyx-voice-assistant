class TTSProvider:
    def synthesize(self, text: str, voice_id: str | None = None):
        raise NotImplementedError
