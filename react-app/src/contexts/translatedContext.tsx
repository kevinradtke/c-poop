import React, { createContext, useState, useContext } from "react";
import { CodeContext } from "./codeContext";

import { EMOJI_HASH } from "../constants/emoji-categories";

const regex = new RegExp(Object.keys(EMOJI_HASH).join("|"), "gi");

const initialState: any = "";

const TranslatedContext = createContext(initialState);

const TranslatedProvider = ({ children }: { children: React.ReactNode }) => {
  const [translatedCode, setTranslatedCode] = useState(initialState);
  const { ref } = useContext(CodeContext);

  const handleTranslation: any = () => {
    const { editor } = ref.current;
    const value: string = editor.getValue();
    const aux = value.replace(regex, matched => {
      return EMOJI_HASH[matched];
    });

    setTranslatedCode(aux);
    editor.focus();
  };

  return (
    <TranslatedContext.Provider
      value={{
        translatedCode,
        setTranslatedCode,
        handleTranslation
      }}
    >
      {children}
    </TranslatedContext.Provider>
  );
};

export { TranslatedProvider, TranslatedContext };
