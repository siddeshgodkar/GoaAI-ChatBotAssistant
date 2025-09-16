import React from "react";
import ChatBox from "./components/ChatBox";

export default function App() {
  return (
    <div className="h-screen w-screen flex bg-black text-white overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-900 p-4 flex flex-col border-r border-gray-800">
        <button className="w-full py-2 px-3 bg-green-600 hover:bg-green-500 rounded-lg mb-4">
          + New Chat
        </button>

        {/* History (just placeholder for now) */}
        <div className="flex-1 overflow-y-auto space-y-2 text-sm">
          <div className="p-2 rounded hover:bg-gray-800 cursor-pointer">
            Yesterday’s Chat
          </div>
          <div className="p-2 rounded hover:bg-gray-800 cursor-pointer">
            GoaAI Test
          </div>
          <div className="p-2 rounded hover:bg-gray-800 cursor-pointer">
            Research Notes
          </div>
        </div>

        {/* Footer */}
        <div className="border-t border-gray-800 pt-4 text-xs text-gray-400">
          GoaAI v1.0
        </div>
      </aside>

      {/* Chat Area */}
      <main className="flex-1 flex justify-center items-center p-6">
        <ChatBox />
      </main>
    </div>
  );
}
