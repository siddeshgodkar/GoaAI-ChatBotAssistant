import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  // Scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;
    setMessages((m) => [...m, { sender: 'user', text: input }]);
    setInput('');
    setIsTyping(true);

    try {
      const res = await axios.post('http://35.154.28.24:8000/api/chat', { message: input });
      setMessages((m) => [...m, { sender: 'bot', text: res.data.reply }]);
    } catch (err) {
      setMessages((m) => [...m, { sender: 'bot', text: "⚠ Error sending message" }]);
    }
    setIsTyping(false);
  };

  return (
    <motion.div
      className="w-full max-w-2xl h-[85vh] bg-black rounded-2xl shadow-lg flex flex-col text-white"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
    >
      {/* Messages */}
      <div className="flex-1 p-4 overflow-y-auto space-y-1">
        {messages.map((msg, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <span
              className={`px-4 py-2 rounded-2xl max-w-xs sm:max-w-md text-sm sm:text-base ${
                msg.sender === 'user'
                  ? 'bg-green-600 text-white'
                  : 'bg-gray-800 text-gray-100'
              }`}
            >
              {msg.text}
            </span>
          </motion.div>
        ))}
        {isTyping && <div className="text-gray-400 animate-pulse">GoaAI is typing...</div>}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="p-4 border-t border-gray-700">
        <div className="flex items-center bg-gray-800 rounded-full px-4 py-2">
          <input
            type="text"
            className="flex-1 bg-transparent text-white outline-none px-2"
            placeholder="Ask me anything..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          />
          <button
            onClick={handleSend}
            className="ml-2 px-4 py-2 bg-green-600 hover:bg-green-500 rounded-full text-sm"
          >
            Send
          </button>
        </div>
      </div>
    </motion.div>
  );
}
