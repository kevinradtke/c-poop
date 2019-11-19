import React, { createContext, useState, createRef } from "react";

import { EMOJI_HASH } from "../constants/emoji-categories";
import {
  EMOJI_CODE_TEST,
  EMOJI_TRANSLATED_TEST
} from "../constants/emoji-code-tests";

const regex = new RegExp(Object.keys(EMOJI_HASH).join("|"), "gi");

const initialState: any = {
  code: EMOJI_CODE_TEST,
  translatedCode: EMOJI_TRANSLATED_TEST
};

const CodeContext = createContext(initialState);

const CodeProvider = ({ children }: { children: React.ReactNode }) => {
  const [code, setCode] = useState(initialState.code);
  const [translatedCode, setTranslatedCode] = useState(
    initialState.translatedCode
  );

  const ref: any = createRef();

  const addEmoji = (emoji: string) => {
    const { editor } = ref.current;
    editor.session.insert(editor.getCursorPosition(), emoji);
    editor.focus();
  };

  const handleTranslation = (newCode: string) => {
    const aux = newCode.replace(regex, matched => {
      return EMOJI_HASH[matched];
    });
    setTranslatedCode(aux);
  };

  return (
    <CodeContext.Provider
      value={{
        code,
        setCode,
        ref,
        addEmoji,
        translatedCode,
        setTranslatedCode,
        handleTranslation
      }}
    >
      {children}
    </CodeContext.Provider>
  );
};

export { CodeProvider, CodeContext };
