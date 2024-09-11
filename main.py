from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts('<video-id>')

for transcript in transcript_list:
    translated_transcript = transcript.translate('<lang>').fetch()
    joined_text = " ".join(item['text'] for item in translated_transcript)
    print(joined_text)