import React, { createContext, useState, createRef } from "react";

const initialState: any = "console.log('C💩 Rocks!');";

const CodeContext = createContext(initialState);

const CodeProvider = ({ children }: { children: React.ReactNode }) => {
  const [code, setCode] = useState(undefined);
  const ref: any = createRef();

  const addEmoji = (emoji: string) => {
    const { editor } = ref.current;
    editor.session.insert(editor.getCursorPosition(), emoji);
    editor.focus();
  };

  return (
    <CodeContext.Provider value={{ code, setCode, ref, addEmoji }}>
      {children}
    </CodeContext.Provider>
  );
};

export { CodeProvider, CodeContext };
