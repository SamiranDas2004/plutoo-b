import { ChatMessage } from '@/types';
import { formatTime } from '@/lib/utils';

interface ChatMessageBubbleProps {
  message: ChatMessage;
}

export function ChatMessageBubble({ message }: ChatMessageBubbleProps) {
  const isBot = message.sender === 'bot';

  return (
    <div className={`flex ${isBot ? 'justify-start' : 'justify-end'} mb-4`}>
      <div
        className={`max-w-xs px-4 py-2 rounded-lg ${
          isBot
            ? 'bg-slate-100 text-slate-900'
            : 'bg-slate-900 text-white'
        }`}
      >
        <p className="text-sm">{message.content}</p>
        <p className={`text-xs mt-1 ${isBot ? 'text-slate-500' : 'text-slate-300'}`}>
          {formatTime(message.timestamp)}
        </p>
      </div>
    </div>
  );
}
