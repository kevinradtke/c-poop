import React, { createContext, createRef } from "react";

import { EMOJI_CODE_TEST } from "../constants/emoji-code-tests";

const initialState: any = EMOJI_CODE_TEST;

const CodeContext = createContext(initialState);

const CodeProvider = ({ children }: { children: React.ReactNode }) => {
  const ref: any = createRef();

  const addEmoji = (emoji: string) => {
    const { editor } = ref.current;
    editor.session.insert(editor.getCursorPosition(), emoji);
    editor.focus();
  };

  const setValue = (newValue: string) => {
    const { editor } = ref.current;
    editor.session.setValue(newValue);
    editor.focus();
  };

  return (
    <CodeContext.Provider
      value={{
        ref,
        EMOJI_CODE_TEST,
        addEmoji,
        setValue
      }}
    >
      {children}
    </CodeContext.Provider>
  );
};

export { CodeProvider, CodeContext };
