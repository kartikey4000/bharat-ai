function Header() {
  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur border-b border-gray-200">
      <div className="h-16 max-w-7xl mx-auto flex items-center justify-between px-6">

        {/* Left: Brand */}
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-orange-500 to-green-600 flex items-center justify-center text-white font-bold">
            🇮🇳
          </div>
          <span className="text-lg font-semibold tracking-tight">
            Bharat AI
          </span>
        </div>

        {/* Right: Meta */}
        <div className="text-xs text-gray-500">
          Powered by Base Agent
        </div>

      </div>
    </header>
  );
}

export default Header;
