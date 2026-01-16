import MessageList from "./chat/MessageList";
import { useState } from "react";
import { chatWithAgent } from "../services/api";
import Header from "./header";

function ChatArea({ messages, setMessages, resumeid, compare_resume }) {
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);

  async function handleSend() {
    if (!input.trim() || sending) return;

    setSending(true);

    // Add user message
    setMessages(prev => [
      ...prev,
      { role: "user", text: input }
    ]);

    const userInput = input;
    setInput("");

    try {
      const response = await chatWithAgent({
        question: userInput,
        role: "general",
        resume_id: resumeid,
        compare_resume_id: compare_resume
      });

      console.log("BACKEND RESPONSE 👉", response);

      setMessages(prev => [
        ...prev,
        { role: "ai", text: response.answer }
      ]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { role: "ai", text: `⚠️ Backend error: ${err.message || err}` }
      ]);
    } finally {
      setSending(false);
    }
  }

  return (
    <main className="flex-1 flex flex-col bg-gray-50">
      <Header />

      {/* Messages */}
      <MessageList messages={messages} />

      {/* Input */}
      <div className="border-t bg-white p-4 rounded-lg">
        <div className="flex items-center gap-3">
          <input
            type="text"
            placeholder="Type your message..."
            className="flex-1 border rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") handleSend();
            }}
            disabled={sending}
          />

          <button
            onClick={handleSend}
            disabled={sending}
            className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-blue-700 disabled:opacity-50"
          >
            {sending ? "Sending..." : "Send"}
          </button>
        </div>
      </div>
    </main>
  );
}

export default ChatArea;
