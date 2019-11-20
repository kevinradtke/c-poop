import React from "react";

import { CodeContext, CodeProvider } from "./codeContext";
import { ThemeContext, ThemeProvider } from "./themeContext";
import { TranslatedContext, TranslatedProvider } from "./translatedContext";
import { TerminalContext, TerminalProvider } from "./terminalContext";

const AppProvider = ({ children }: { children: React.ReactNode }) => {
  return (
    <CodeProvider>
      <ThemeProvider>
        <TranslatedProvider>
          <TerminalProvider>{children}</TerminalProvider>
        </TranslatedProvider>
      </ThemeProvider>
    </CodeProvider>
  );
};

export {
  AppProvider,
  CodeContext,
  ThemeContext,
  TranslatedContext,
  TerminalContext
};
