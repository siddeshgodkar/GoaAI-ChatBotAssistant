export default function MessageBubble({ role, content }) {
  return (
    <div
      className={`p-2 rounded-lg ${
        role === "user" ? "bg-blue-500 self-end" : "bg-gray-700 self-start"
      }`}
    >
      {content}
    </div>
  );
}
