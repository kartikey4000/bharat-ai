import ReactMarkdown from "react-markdown";

function AiMessage({ text }) {
  return (
    <div className="flex justify-start">
      <div className="max-w-[70%] bg-white border border-gray-200 rounded-xl px-4 py-2 shadow-sm">
        <div className="prose prose-sm max-w-none text-gray-800">
          <ReactMarkdown>{text}</ReactMarkdown>
        </div>
      </div>
    </div>
  );
}

export default AiMessage;
