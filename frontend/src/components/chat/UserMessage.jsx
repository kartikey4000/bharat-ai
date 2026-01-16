function UserMessage({ text }) {
  return (
    <div className="flex justify-end">
      <div className="max-w-[70%] bg-blue-600 text-white rounded-xl px-4 py-2">
        <p className="text-sm leading-relaxed">
          {text}
        </p>
      </div>
    </div>
  );
}

export default UserMessage;
