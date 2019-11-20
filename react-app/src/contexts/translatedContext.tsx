import React, { createContext, useState, useContext } from "react";
import { CodeContext } from "./";

import { EMOJI_HASH } from "../constants/emoji-categories";
import { EMOJI_TRANSLATED_TEST } from "../constants/emoji-code-tests";

const regex = new RegExp(Object.keys(EMOJI_HASH).join("|"), "gi");

const initialState: any = "";

const TranslatedContext = createContext(initialState);

const TranslatedProvider = ({ children }: { children: React.ReactNode }) => {
  const [translatedCode, setTranslatedCode] = useState(EMOJI_TRANSLATED_TEST);
  const { ref } = useContext(CodeContext);

  const handleTranslation: any = () => {
    const { editor } = ref.current;
    var value: string = editor.getValue();
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
