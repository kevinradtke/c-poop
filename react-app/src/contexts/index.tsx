import React from "react";

import { CodeContext, CodeProvider } from "./codeContext";
import { ThemeContext, ThemeProvider } from "./themeContext";
import { TranslatedContext, TranslatedProvider } from "./translatedContext";

const AppProvider = ({ children }: { children: React.ReactNode }) => {
  return (
    <CodeProvider>
      <ThemeProvider>
        <TranslatedProvider>{children}</TranslatedProvider>
      </ThemeProvider>
    </CodeProvider>
  );
};

export { AppProvider, CodeContext, ThemeContext, TranslatedContext };
