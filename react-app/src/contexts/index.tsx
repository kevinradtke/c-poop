import React from "react";

import { CodeContext, CodeProvider } from "./codeContext";
import { ThemeContext, ThemeProvider } from "./themeContext";

const AppProvider = ({ children }: { children: any }) => {
  return (
    <CodeProvider>
      <ThemeProvider>{children}</ThemeProvider>
    </CodeProvider>
  );
};

export { AppProvider, CodeContext, ThemeContext };
