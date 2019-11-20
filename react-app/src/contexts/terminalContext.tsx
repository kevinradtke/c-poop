import React, { createContext, useState, useContext } from "react";
import { CodeContext, TranslatedContext } from "./";

import API from "../components/split-panes/terminal-pane/Api";

const initialState: any = "$";

const TerminalContext = createContext(initialState);

const TerminalProvider = ({ children }: { children: React.ReactNode }) => {
  const [terminal, setTerminal] = useState("$");
  const { translatedCode } = useContext(TranslatedContext);
  const { ref } = useContext(CodeContext);

  const handleTerminal = () => {
    const { editor } = ref.current;
    API.call({
      service: "compile",
      method: "post",
      params: { code: translatedCode },
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
