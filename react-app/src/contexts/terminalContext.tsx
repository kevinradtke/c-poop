import React, { createContext, useState, useContext } from "react";
import { TranslatedContext } from "./translatedContext";
import { CodeContext } from "./codeContext";

import API from "../components/split-panes/terminal-pane/Api";

import { EMOJI_HASH } from "../constants/emoji-categories";

const regex = new RegExp(Object.keys(EMOJI_HASH).join("|"), "gi");

const initialState: any = "$";

const TerminalContext = createContext(initialState);

const TerminalProvider = ({ children }: { children: React.ReactNode }) => {
  const [terminal, setTerminal] = useState("$");
  const { setTranslatedCode } = useContext(TranslatedContext);
  const { ref } = useContext(CodeContext);

  const handleTerminal = () => {
    const { editor } = ref.current;
    const value: string = editor.getValue();
    const aux = value.replace(regex, matched => {
      return EMOJI_HASH[matched];
    });

    setTranslatedCode(aux);

    API.call({
      service: "compile",
      method: "post",
      params: { code: aux },
      success: (response: string) => {
        setTerminal(response);
      }
    });
    editor.focus();
  };

  return (
    <TerminalContext.Provider
      value={{
        terminal,
        handleTerminal
      }}
    >
      {children}
    </TerminalContext.Provider>
  );
};

export { TerminalProvider, TerminalContext };
