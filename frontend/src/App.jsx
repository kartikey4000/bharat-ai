import { useState } from "react";
import Sidebar from "./components/sidebar";
import ChatArea from "./components/Chatarea";

function App() {
  const [messages, setMessages] = useState([]);
  const [resumeid, setResumeId] = useState(null);
  const [compare_resume, setCompareResume] = useState(null);

  return (
    <div className="flex h-screen">
      <Sidebar
        setMessages={setMessages}
        setResumeId={setResumeId}
        setCompareResume={setCompareResume}
      />

      <ChatArea
        messages={messages}
        resumeid={resumeid}
        compare_resume={compare_resume}
        setMessages={setMessages}
      />
    </div>
  );
}

export default App;
