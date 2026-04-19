class STTProvider:
    def start_stream(self):
        raise NotImplementedError

    def send_audio_chunk(self, chunk: bytes):
        raise NotImplementedError

    def stop_stream(self):
        raise NotImplementedError
