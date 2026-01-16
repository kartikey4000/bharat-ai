import UserMessage from "./UserMessage";
import AiMessage from "./AiMessage";

function MessageList({ messages }) {
    return (
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
            {messages.map((msg, index) => {
                if (msg.role === "user") {
                    return <UserMessage key={index} text={msg.text} />;
                }

                return <AiMessage key={index} text={msg.text} />;
            })}
        </div>
    );
}

export default MessageList;
