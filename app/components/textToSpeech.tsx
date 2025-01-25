
import { useSpeechSynthesis } from 'react-speech-kit';

export default function TextToSpeech() {
  const { speak } = useSpeechSynthesis();

  return (
    <div>
      <button onClick={() => speak({ text: 'hello i am siri' })}>Speak</button>
    </div>
  );
}